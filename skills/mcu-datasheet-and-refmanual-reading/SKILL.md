---
name: mcu-datasheet-and-refmanual-reading
description: "Datasheet and reference manual reading skill for embedded engineers. Use when extracting pinouts, electrical limits, register maps, clock trees, or timing from MCU documentation. Activates on queries about reading STM32 RM, extracting register bits, finding errata, or navigating reference manual sections."
---

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# Datasheet and Reference Manual Reading

## Purpose

Teach agents a systematic methodology for reading MCU datasheets and reference manuals: which sections matter for firmware, how to cross-reference pin tables with register maps, and how to avoid documentation pitfalls (errata, footnotes, conditional fields). **Not merged** with `skills/mcu-peripherals-from-datasheet` — this skill covers **how to read docs**; that skill covers **how to write drivers** from them.

## When to Use

- Starting driver work on unfamiliar silicon
- Resolving ambiguous register bit behavior
- Verifying electrical and timing constraints before PCB/firmware sign-off
- Complementing `skills/mcu-peripherals-from-datasheet` (implementation focus)
- Answering "where in the RM do I find X?"

## Workflow

### 1. Document types

| Document | Primary use |
|----------|-------------|
| Datasheet | Pinout, max ratings, package, brief features |
| Reference Manual (RM) | Register maps, bit fields, clock trees, peripheral behavior |
| Programming Manual (PM) | Cortex-M core, NVIC, MPU, debug (ARM doc) |
| Errata sheet | Silicon bugs that affect firmware workarounds |

Read the datasheet for **what exists**; read the RM for **how to program it**.

### 2. First-pass reading order (RM)

```
1. Memory and bus architecture (address map)
2. Reset and clock control (RCC / CGU)
3. GPIO / pin multiplexing
4. Target peripheral chapter (e.g. USART, SPI, DMA)
5. NVIC / EXTI interrupt mapping table
6. Electrical characteristics (only if timing-critical)
7. Errata — search peripheral name
```

### 3. Register map extraction checklist

For each register:

- Offset from peripheral base (verify against memory map table)
- Reset value (affects read-modify-write defaults)
- Read-only / write-only / write-1-to-clear bits
- Fields that depend on mode (check "Notes" under table)
- Side effects: clearing flags, auto-clear bits, reserved must-write-0

```c
/* Good — named constants from RM bit table */
#define USART_CR1_UE   (1U << 13)
#define USART_CR1_TE   (1U << 3)

/* Bad — magic numbers without RM citation */
*(volatile uint32_t *)0x40011000 = 0x2000;
```

### 4. Pin / signal cross-reference

```
Schematic net → Datasheet pin table (AF number)
             → RM GPIO chapter (MODER, AFR)
             → Peripheral chapter (USART_TX on PA2 = AF7)
```

Always confirm **default state after reset** (analog mode, pull, JTAG pins).

### 5. Timing and electrical traps

- Setup/hold for external bus modes (FSMC, SDIO)
- ADC sampling time vs source impedance (datasheet graph)
- Maximum GPIO toggle rate vs load capacitance
- Boot mode pins sampled only at reset

### 6. Errata workflow

```
Symptom matches errata?
├── Yes → apply documented workaround in driver
└── No  → verify silicon revision (DBGMCU_IDCODE / UID)
```

### 7. Agent usage

```
/datasheet-and-refmanual-reading Find STM32F4 USART baud rate formula and required clock source
```

## Common Problems

| Symptom | Cause | Fix |
|---------|-------|-----|
| Wrong register behavior | Read wrong silicon rev errata | Check ERRATA sheet first |
| AF does not work | Confused DS pin name with RM AF table | Cross-check both tables |
| Intermittent DMA | Missed footnote on buffer alignment | RM DMA chapter notes |
| Clock mismatch | Used max frequency from DS banner, not voltage range table | Use operating conditions table |

## Related Skills

- `skills/mcu-peripherals-from-datasheet` — driver implementation workflow
- `skills/mcu-mmio-and-bit-manipulation` — safe register access
- `skills/mcu-gpio-baremetal` — pin mux from RM tables
- `skills/kernel-dev/device-tree` — bindings mirror RM capabilities for Linux

## 来源与修改 / Provenance

- Upstream: [mohitmishra786/low-level-dev-skills — skills/baremetal/datasheet-and-refmanual-reading](https://github.com/mohitmishra786/low-level-dev-skills/tree/bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608/skills/baremetal/datasheet-and-refmanual-reading)
- Pinned commit: `bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
