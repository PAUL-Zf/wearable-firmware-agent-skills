---
name: mcu-openocd-jtag
description: "OpenOCD skill for embedded hardware debugging. Use when configuring OpenOCD for JTAG or SWD targets, flashing firmware, connecting GDB to bare-metal targets, setting hardware watchpoints, or using J-Link with OpenOCD. Activates on queries about OpenOCD, JTAG, SWD, GDB remote target, flash programming, hardware breakpoints, J-Link, or connecting GDB to an MCU."
---

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# OpenOCD / JTAG Debugging

## Purpose

Guide agents through configuring OpenOCD for JTAG and SWD targets, flashing firmware to microcontrollers, attaching GDB for bare-metal debugging, setting hardware watchpoints, and configuring J-Link and CMSIS-DAP adapters.

## Triggers

- "How do I connect GDB to my MCU with OpenOCD?"
- "How do I flash firmware using OpenOCD?"
- "How do I set up J-Link with OpenOCD?"
- "What's the difference between JTAG and SWD?"
- "How do I set a hardware watchpoint in GDB?"
- "OpenOCD says 'Error: unable to find JTAG device' — how do I fix it?"

## Workflow

### 1. Select one probe and one target

JTAG and SWD support, multidrop, transport naming and maximum clock depend on the probe,
MCU and OpenOCD version. SWD is common on Cortex-M; neither fixed speed limits nor a blanket
“no multitarget SWD” claim is a portable rule. Verify the target voltage and wiring first.

### 2. OpenOCD configuration

These are mutually exclusive examples. CMSIS-DAP is not synonymous with ST-Link; for ST-Link
use the interface/transport scripts supplied by the installed OpenOCD version.
Select the transport after the interface and before loading the target configuration.

Example A — CMSIS-DAP and STM32F4, only if that matches the board:

```tcl
source [find interface/cmsis-dap.cfg]
transport select swd
adapter speed 1000
source [find target/stm32f4x.cfg]
```

Example B — J-Link and nRF52, only if that matches the board:

```tcl
source [find interface/jlink.cfg]
transport select swd
adapter speed 1000
source [find target/nrf52.cfg]
```

Run `openocd -f openocd.cfg` after choosing exactly one configuration. Locate scripts from
the installed package documentation or its documented search paths; OpenOCD help output
is not a reliable shell path. Probe serial selection syntax is version-specific.

### 3. Connecting GDB

```bash
# In terminal 1: start OpenOCD
openocd -f openocd.cfg

# In terminal 2: start GDB
arm-none-eabi-gdb firmware.elf

# GDB commands
(gdb) target extended-remote :3333   # connect to OpenOCD
(gdb) monitor reset halt              # reset and halt target
(gdb) load                            # flash ELF to target
(gdb) monitor reset init             # re-initialize after flash
(gdb) break main                      # set software breakpoint
(gdb) continue

# One-liner for quick debugging
arm-none-eabi-gdb -ex "target extended-remote :3333" \
                  -ex "monitor reset halt" \
                  -ex "load" \
                  -ex "break main" \
                  -ex "continue" \
                  firmware.elf
```

### 4. Flashing firmware

```bash
# Flash via OpenOCD telnet interface
telnet localhost 4444

# OpenOCD telnet commands
> reset halt
> program firmware.elf verify reset
> exit

# Or via GDB
(gdb) monitor flash write_image erase firmware.bin 0x08000000
(gdb) monitor reset run

# Flash only (no debug) — script mode
openocd -f openocd.cfg \
        -c "program firmware.elf verify reset exit"

# For raw binary
openocd -f openocd.cfg \
        -c "program firmware.bin 0x08000000 verify reset exit"
```

### 5. Hardware breakpoints and watchpoints

Software breakpoints (`break`) patch instruction memory with trap instructions — they don't work in flash-execute-in-place without debug registers. Use hardware breakpoints instead:

```bash
# Hardware breakpoint (uses debug register, limited count: 4-8 on Cortex-M)
(gdb) hbreak function_name
(gdb) hbreak *0x08001234

# Hardware watchpoint — triggers on memory read/write
(gdb) watch global_variable         # write watchpoint
(gdb) rwatch some_buffer            # read watchpoint
(gdb) awatch sensor_value           # read OR write watchpoint

# List breakpoints/watchpoints
(gdb) info breakpoints

# Cortex-M typically has: 4–8 hardware breakpoints, 2–4 watchpoints
```

### 6. OpenOCD commands reference

```bash
# Via telnet (port 4444) or GDB monitor
monitor reset halt          # reset and hold at reset vector
monitor reset init          # reset and run init scripts
monitor reset run           # reset and run freely
monitor halt                # halt running target
monitor resume              # resume execution
monitor mdw 0x20000000      # memory display word at address
monitor mww 0x40021000 0x1  # memory write word
monitor reg r0              # read register
monitor arm disassemble 0x08000000 16  # disassemble 16 instructions

# Flash operations
monitor flash list
monitor flash erase_sector 0 0 0   # erase sector 0
monitor flash write_bank 0 firmware.bin 0
```

### 7. Common errors

| Error | Cause | Fix |
|-------|-------|-----|
| `unable to find JTAG device` | Wrong interface, cable, or power | Check USB connection; power target; verify interface config |
| `JTAG scan chain interrogation failed` | Wrong target config or bad SWD mode | Match config to exact MCU; try `transport select swd` |
| `flash 'stm32f4x' is not supported` | Wrong target | Check MCU part number; use correct `.cfg` |
| `Error: timed out while waiting for target halted` | Target running, not halted | `monitor halt`; check BOOT pins |
| `Cannot access memory at address` | MMU, memory protection, or wrong address | Check MPU config; use correct flash/RAM address |
| `Warn: target not examined yet` | OpenOCD not connected to target | Check power and connections |

### 8. Debug session boundaries

Attaching, resetting, halting and loading are distinct actions. Use the operations authorized
for the task and preserve the agreed target state; an observation-only session must not load
firmware automatically. Verify image identity and flash regions before programming.

J-Link GDB Server can be an alternative to OpenOCD; select its exact device and probe using
the installed SEGGER documentation. Do not start both servers against the same probe.

## Related skills

- Use `skills/mcu-freertos` for FreeRTOS-aware debugging with OpenOCD
- Use `skills/mcu-zephyr` for Zephyr's `west debug` integration
- Use `skills/mcu-gdb` for GDB session management
- Use `skills/mcu-linker-scripts` for understanding memory map for flash addresses

## 来源与修改 / Provenance

- Upstream: [mohitmishra786/low-level-dev-skills — skills/embedded/openocd-jtag](https://github.com/mohitmishra786/low-level-dev-skills/tree/bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608/skills/embedded/openocd-jtag)
- Pinned commit: `bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
