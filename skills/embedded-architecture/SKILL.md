---
name: embedded-architecture
description: "Use when creating a new embedded firmware project, adding a module, refactoring firmware, reviewing architecture, or generating project structure. Enforces mandatory architecture rules for maintainable, portable, testable, hardware-independent firmware targeting STM32, GD32, ESP32, RP2040, NXP, Nordic, and similar MCU platforms. Covers project structure, dependency management, module boundaries, platform abstraction, and architecture validation.\n"
---

## Architecture scope

The upstream APP/MODULE/INTERFACE/BSP/PLATFORM layering is an example architecture. Respect an existing project architecture and adapt its principles instead of imposing a repository-wide rewrite.

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# Embedded Architecture

## Purpose

Define the mandatory architecture rules for embedded firmware projects.

The goal is to generate maintainable, portable, testable, and hardware-independent firmware
suitable for STM32, GD32, ESP32, RP2040, NXP, Nordic, and similar MCU platforms.

This skill focuses on:

- project structure
- dependency management
- module boundaries
- platform abstraction
- code ownership
- architecture validation

## Architecture Principles

Generated firmware must follow:

1. Single responsibility
2. Low coupling
3. High cohesion
4. Explicit interfaces
5. Hardware abstraction
6. Platform portability
7. Testability
8. Deterministic behavior

The application layer must never depend directly on MCU vendor libraries.

Business logic must remain independent from STM32 HAL, CMSIS, FreeRTOS internals, or peripheral registers.

## Required Project Structure

Firmware projects must use the following layout:

```text
project/
├── app/
├── module/
├── interface/
├── bsp/
├── platform/
├── middleware/
├── docs/
├── tools/
└── tests/
```

### `app/` — Application Entry Points

Contains:

- state machines
- application orchestration
- system startup sequence
- task creation

Must not contain:

- register access
- HAL calls
- peripheral drivers

### `module/` — Business Logic

Examples: `motor/`, `imu/`, `control/`, `telemetry/`, `navigation/`, `power/`

Modules may depend only on `interface/`.

Modules must not access directly: HAL, CMSIS, GPIO registers, UART registers, SPI registers.

### `interface/` — Hardware Abstraction Contracts

Examples: `gpio_if.h`, `uart_if.h`, `spi_if.h`, `pwm_if.h`, `timer_if.h`

Defines contracts only. Must not contain implementation.

### `bsp/` — Board-Specific Implementation

Examples: `led`, `button`, `buzzer`, `oled`, `imu_board`

Responsible for mapping interfaces to hardware. May use platform layer.

### `platform/` — Vendor-Specific Code

```text
platform/
└── stm32f407/
    ├── core/
    ├── hal/
    ├── cmsis/
    ├── startup/
    └── linker/
```

Contains: CubeMX generated code, HAL drivers, CMSIS, startup files, linker scripts.

Must never contain business logic.

### `middleware/` — Third-Party Middleware

Examples: `freertos/`, `lwip/`, `fatfs/`, `usb/`

Should remain isolated from application logic.

## Dependency Rules

Allowed direction (top-down only):

```text
APP → MODULE → INTERFACE → BSP → PLATFORM
```

Forbidden:

- `APP → HAL`
- `APP → STM32_GPIO / STM32_UART`
- `MODULE → HAL`
- `MODULE → Register Access`
- `MODULE → CMSIS`
- `MODULE → FreeRTOS Internal APIs`
- `PLATFORM → MODULE`
- `PLATFORM → APP`
- `BSP → APP`

Dependencies must always point downward. Circular dependencies are forbidden.

## Platform Isolation Rules

All MCU vendor files must reside inside `platform/<target>/`:

```text
platform/stm32f407/
platform/stm32h743/
platform/gd32f450/
platform/esp32s3/
```

Never place generated vendor code directly in project root.

Forbidden at repository root: `/Core`, `/Drivers` — move them into the platform directory.

## Interface Rules

Every hardware service must expose an interface.

Example:

```c
typedef struct {
    int32_t (*write)(const uint8_t *data, uint32_t len);
    int32_t (*read)(uint8_t *data, uint32_t len);
} uart_if_t;
```

Modules interact only with interfaces. Modules must not know: UART instance, GPIO port, DMA channel, MCU family.

## Module Rules

Each module should own one responsibility.

Good: `motor`, `imu`, `control`, `telemetry`, `storage`

Bad: `system_manager`, `all_in_one`, `utility`, `misc`

Avoid god-modules.

## RTOS Separation

RTOS task creation belongs to `app/`. Business logic belongs to `module/`.

Bad — task function contains sensor reading, control algorithm, logging, and communication all mixed together.

Good — task calls module API, which calls interface, which calls driver:

```text
TASK → MODULE API → INTERFACE → DRIVER
```

## Architecture Validation Checklist

Before accepting generated code, verify:

- [ ] Project follows required directory layout
- [ ] No HAL usage in `app/`
- [ ] No HAL usage in `module/`
- [ ] No register access outside `platform/`
- [ ] No CubeMX code outside `platform/`
- [ ] All peripherals abstracted through interfaces
- [ ] No circular dependencies
- [ ] No business logic inside BSP
- [ ] No business logic inside platform
- [ ] Modules have single responsibility
- [ ] Interfaces contain declarations only
- [ ] Dependency direction is correct

If violations are found:

1. Report the violation
2. Explain why it is harmful
3. Suggest the corrected architecture
4. Refactor generated code accordingly

Architecture correctness takes precedence over implementation convenience.

## 来源与修改 / Provenance

- Upstream: [rovinax/embedded-skills — skills/embedded-architecture](https://github.com/rovinax/embedded-skills/tree/022ce31b469b1a1d0c1261c2c8d0f3e07b2c0bbc/skills/embedded-architecture)
- Pinned commit: `022ce31b469b1a1d0c1261c2c8d0f3e07b2c0bbc`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
