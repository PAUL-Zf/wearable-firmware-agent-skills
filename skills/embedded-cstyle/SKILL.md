---
name: embedded-cstyle
description: "Use when generating, modifying, reviewing, or refactoring C code for embedded firmware projects (STM32, GD32, ESP32, FreeRTOS, bare-metal, driver development, robotics). Enforces engineering coding standards — naming, types, functions, variables, macros, headers, memory, concurrency, error handling, and documentation. Catches AI-common mistakes: global variables, magic numbers, missing static/const, volatile abuse, ignored return values, unchecked null pointers, and HAL calls leaking into business logic.\n"
---

## Workflow reference

Read [the scoped workflow](references/upstream-workflow.md) when this task matches. Its external tool dependencies must be available before executing tool-specific steps.

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.


## 来源与修改 / Provenance

- Upstream: [rovinax/embedded-skills — skills/embedded-cstyle](https://github.com/rovinax/embedded-skills/tree/022ce31b469b1a1d0c1261c2c8d0f3e07b2c0bbc/skills/embedded-cstyle)
- Pinned commit: `022ce31b469b1a1d0c1261c2c8d0f3e07b2c0bbc`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
