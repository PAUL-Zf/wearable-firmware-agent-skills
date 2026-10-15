---
name: zephyr-specialized
description: "Specialized hardware interfaces and system reliability for Zephyr RTOS. Covers LVGL GUI development, Audio I2S/Codecs, Watchdog timers, and Fault Injection. Trigger when building human-machine interfaces (HMI), audio devices, or high-reliability mission-critical systems."
---

## Version contract

Pin the project Zephyr revision and board target. Verify Kconfig symbols, devicetree bindings and API signatures against that revision; templates do not prove compatibility. Device PM must coordinate active users and transfers.

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# Zephyr Specialized Hardware & Reliability

Integrate complex peripherals and build resilient systems that recover gracefully from unexpected failures.

## Core Workflows

### 1. LVGL GUI Development
Build sophisticated graphical user interfaces for LCD and TFT displays.
- **Reference**: **[lvgl_gui.md](references/lvgl_gui.md)**
- **Key Tools**: Widgets, Styles, Double Buffering, `native_sim` simulator.

### 2. Audio I2S & Codecs
Implement high-quality digital audio streaming and codec management.
- **Reference**: **[audio_i2s.md](references/audio_i2s.md)**
- **Key Tools**: `CONFIG_I2S`, DMA streaming, Ping-pong buffering.

### 3. Watchdog & Reliability
Ensure your system never hangs in the field using hardware watchdog timers.
- **Reference**: **[watchdog_reliability.md](references/watchdog_reliability.md)**
- **Key Tools**: `wdt_feed()`, Windowed watchdog, Health checks.

### 4. Fault Injection & Resilience
Test your system's ability to recover from unexpected software and hardware errors.
- **Reference**: **[fault_injection.md](references/fault_injection.md)**
- **Key Tools**: Chaos testing, `k_oops()`, Reset reason diagnostics.

## Quick Start (Watchdog Feed)
```kconfig
# Enable watchdog support
CONFIG_WATCHDOG=y
```
```c
// Feed the dog in your main loop
while (1) {
    // Perform application work
    wdt_feed(wdt_dev, wdt_channel);
    k_sleep(K_MSEC(1000));
}
```

## Professional Patterns (Reliability & UX)
- **Safe Boot Animation**: Use a simple, non-interactive LVGL screen to show system status while critical subsystems (e.g., cloud connectivity) are initializing.
- **Zero-Pop Audio**: Always use volume ramping when starting or stopping I2S streams to protect hardware and improve user experience.
- **Bitmask Health Monitoring**: Use a bitmask to track the health of all background threads; the watchdog monitor only feeds the timer if ALL bits are set periodically.

## Automation Tools
- **[watchdog_window_check.py](scripts/watchdog_window_check.py)**: Verify feed interval timing against watchdog window constraints.

## Examples & Templates
- **[watchdog_health_map_template.h](assets/watchdog_health_map_template.h)**: Starter health-bit definitions for watchdog supervision.

## Validation Checklist
- [ ] GUI render loop maintains target frame behavior without starving control tasks.
- [ ] I2S audio stream starts/stops without underruns or audible artifacts.
- [ ] Watchdog feed policy resets the system when health criteria are not met.
- [ ] Fault-injection scenarios produce expected reset reason and recovery behavior.

## Resources

- **[References](references/)**:
  - `lvgl_gui.md`: GUI widgets and performance tuning.
  - `audio_i2s.md`: Audio streaming and DMA patterns.
  - `watchdog_reliability.md`: Watchdog setup and health checks.
  - `fault_injection.md`: System resilience and chaos testing.
- **[Scripts](scripts/)**:
  - `watchdog_window_check.py`: Feed-window timing checker.
- **[Assets](assets/)**:
  - `watchdog_health_map_template.h`: Health-mask template header.

## 来源与修改 / Provenance

- Upstream: [beriberikix/zephyr-agent-skills — skills/specialized](https://github.com/beriberikix/zephyr-agent-skills/tree/ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce/skills/specialized)
- Pinned commit: `ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce`
- License: `Apache-2.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
