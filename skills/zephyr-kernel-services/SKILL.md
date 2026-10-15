---
name: zephyr-kernel-services
description: "Advanced Zephyr RTOS kernel services. Covers inter-thread communication using Zbus (pub/sub), behavioral management with the State Machine Framework (SMF), background processing via work queues, and persistent configuration with the Settings subsystem. Trigger when building modular application architectures, complex state-driven logic, or requiring persistent data storage."
---

## Version contract

Pin the project Zephyr revision and board target. Verify Kconfig symbols, devicetree bindings and API signatures against that revision; templates do not prove compatibility. Device PM must coordinate active users and transfers.

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# Zephyr Kernel Services

Move beyond basic threading and logging to build modular, event-driven, and robust Zephyr applications.

## Core Workflows

### 1. Event-Driven Communication (Zbus)
Decouple your modules using a lightweight publish-and-subscribe bus.
- **Reference**: **[zbus.md](references/zbus.md)**
- **Key Tools**: `ZBUS_CHAN_DEFINE`, `ZBUS_SUBSCRIBER_DEFINE`, `zbus_chan_pub`.

### 2. Behavioral Logic (SMF)
Manage complex system states and transitions using the State Machine Framework.
- **Reference**: **[smf.md](references/smf.md)**
- **Key Tools**: `smf_set_state`, `SMF_CREATE_STATE`, Hierarchical states.

### 3. Background Processing (Work Queues)
Defer long-running or non-critical tasks to prevent blocking interrupts or high-priority threads.
- **Reference**: **[settings_workqueue.md](references/settings_workqueue.md)**
- **Key Tools**: `k_work_submit`, `k_work_delayable`, Custom work queues.

### 4. Persistence (Settings)
Save and restore configuration data and state across reboots.
- **Reference**: **[settings_workqueue.md](references/settings_workqueue.md#settings-subsystem)**
- **Key Tools**: `settings_load`, `settings_save_one`, NVS backends.

## Quick Start (Zbus)
```c
// Define a channel for sensor data
ZBUS_CHAN_DEFINE(sensor_data_chan, struct sensor_msg, NULL, NULL, ZBUS_OBSERVERS_EMPTY, ZBUS_CHAN_DEFAULTS);

// Publish from a thread
zbus_chan_pub(&sensor_data_chan, &msg, K_NO_WAIT);
```

## Professional Patterns (Asset Tracker Style)
- **Modularity**: Use Zbus as the backbone for inter-module communication.
- **Predictability**: Use SMF to define clear lifecycle states for each module (e.g., Uninitialized -> Ready -> Active -> Error).
- **Responsiveness**: Use custom work queues for sensor data ingestion to keep the main thread responsive for cloud communication.
- **Sensor Integration**: For sensor data ingestion patterns, see the **[hardware-io](../zephyr-hardware-io/SKILL.md)** skill.

## Automation Tools
- **[zbus_channel_lint.py](scripts/zbus_channel_lint.py)**: Detect duplicate `ZBUS_CHAN_DEFINE` names across source files.

## Examples & Templates
- **[smf_state_table_template.c](assets/smf_state_table_template.c)**: Starter SMF state table and lifecycle wiring.

## Validation Checklist
- [ ] Zbus publishers and subscribers exchange messages without deadlock or missed updates.
- [ ] SMF transitions follow expected state graph under normal and error conditions.
- [ ] Deferred work executes on intended queue context with bounded execution time.
- [ ] Settings values persist across reboot and reload successfully at startup.

## Resources

- **[References](references/)**:
  - `zbus.md`: Publish/Subscribe patterns and subscriber types.
  - `smf.md`: Finite and Hierarchical state machine implementation.
  - `settings_workqueue.md`: Background work and persistent storage.
- **[Scripts](scripts/)**:
  - `zbus_channel_lint.py`: Zbus channel name collision checker.
- **[Assets](assets/)**:
  - `smf_state_table_template.c`: State-machine template.

## 来源与修改 / Provenance

- Upstream: [beriberikix/zephyr-agent-skills — skills/kernel-services](https://github.com/beriberikix/zephyr-agent-skills/tree/ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce/skills/kernel-services)
- Pinned commit: `ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce`
- License: `Apache-2.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
