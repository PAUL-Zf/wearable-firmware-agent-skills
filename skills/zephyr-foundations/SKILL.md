---
name: zephyr-foundations
description: "Foundational skills for Zephyr RTOS development. Covers essential Embedded C patterns (BIT, CONTAINER_OF), real-time concurrency primitives (mutexes, semaphores, spinlocks), hardware literacy (datasheet-to-DTS mapping), and defensive programming. Trigger when writing core application logic, drivers, or troubleshooting foundational behavior."
---

## Version contract

Pin the project Zephyr revision and board target. Verify Kconfig symbols, devicetree bindings and API signatures against that revision; templates do not prove compatibility. Device PM must coordinate active users and transfers.

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# Zephyr Foundations

Mastering the bedrock of Zephyr is essential for writing efficient, robust, and idiomatic code.

## Core Workflows

### 1. Idiomatic C Patterns
Zephyr uses specific macros to manage memory and hardware-software mapping.
- **Reference**: **[zephyr_macros.md](references/zephyr_macros.md)**
- **Key Tools**: `CONTAINER_OF`, `BIT()`, `GENMASK()`, `ARRAY_SIZE`.

### 2. Real-Time Concurrency
Safe multi-threading and interrupt handling are critical for stability.
- **Reference**: **[concurrency.md](references/concurrency.md)**
- **Key Tools**: `k_mutex`, `k_sem`, `k_spinlock`, `atomic_t`, ISR safety rules.

### 3. Hardware Literacy (Devicetree)
Understanding how code interacts with the hardware description.
- **Reference**: **[devicetree_basics.md](references/devicetree_basics.md)**
- **Key Tools**: Nodes, properties, phandles, overlays, and advanced deletion.

### 4. Robust Error Handling
Preventing crashes through defensive programming.
- **Reference**: **[error_handling.md](references/error_handling.md)**
- **Key Tools**: `errno.h`, `BUILD_ASSERT`, validation patterns, return code checking.

## Quick Start (Defensive Pattern)
```c
int sensor_read_checked(const struct device *dev)
{
  if (dev == NULL || !device_is_ready(dev)) {
    return -ENODEV;
  }

  return 0;
}
```

## Validation Checklist
- [ ] Shared bit-field logic uses Zephyr macros (`BIT`, `GENMASK`) instead of raw literals.
- [ ] Thread-shared state is protected with mutex/spinlock/atomic primitives.
- [ ] Error paths return standard negative `errno` codes.
- [ ] Defensive guards exist for null pointers, bounds, and device readiness checks.

## Automation Tools
- **[errno_return_check.py](scripts/errno_return_check.py)**: Detect likely non-negative `errno` return statements in C/C++ code.

## Examples & Templates

- **[template_driver.c](assets/foundation_examples/template_driver.c)**: A complete skeleton showing how to combine DT macros, mutexes, and config-data separation.

## Resources

- **[References](references/)**:
  - `zephyr_macros.md`: Essential macros (BIT, CONTAINER_OF, etc.).
  - `concurrency.md`: Mutexes, Semaphores, Spinlocks, and ISR safety.
  - `devicetree_basics.md`: Devicetree syntax and overlay patterns.
  - `error_handling.md`: Error codes and defensive programming.
- **[Scripts](scripts/)**:
  - `errno_return_check.py`: Return-code sign checker.
- **[Assets](assets/)**:
  - `foundation_examples/`: Working code templates for drivers and logic.

## 来源与修改 / Provenance

- Upstream: [beriberikix/zephyr-agent-skills — skills/zephyr-foundations](https://github.com/beriberikix/zephyr-agent-skills/tree/ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce/skills/zephyr-foundations)
- Pinned commit: `ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce`
- License: `Apache-2.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
