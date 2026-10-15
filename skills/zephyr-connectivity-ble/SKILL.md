---
name: zephyr-connectivity-ble
description: "Bluetooth Low Energy (BLE) integration for Zephyr RTOS. Covers GATT Services/Characteristics, GAP advertising, connection parameters, power optimization strategies, and the professional Send-When-Idle design pattern. Trigger when adding BLE connectivity, optimizing battery life for wireless devices, or implementing custom GATT profiles."
---

## Version contract

Pin the project Zephyr revision and board target. Verify Kconfig symbols, devicetree bindings and API signatures against that revision; templates do not prove compatibility. Device PM must coordinate active users and transfers.

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# Zephyr Connectivity: BLE

Implement robust, low-power Bluetooth Low Energy applications using Zephyr's industry-standard BLE stack.

## Core Workflows

### 1. BLE Fundamentals
Set up advertising, define GATT services, and manage connections.
- **Reference**: **[ble_fundamentals.md](references/ble_fundamentals.md)**
- **Key Tools**: `BT_GATT_SERVICE_DEFINE`, `bt_le_adv_start`, `BT_CONN_CB_DEFINE`.

### 2. Send-When-Idle Pattern
Optimize radio usage by bundling data and transmitting only during idle periods.
- **Reference**: **[send_when_idle.md](references/send_when_idle.md)**
- **Key Tools**: `k_work_delayable`, Workqueues, SMF integration.

### 3. Power Optimization
Fine-tune intervals and connection parameters for maximum battery life.
- **Reference**: **[power_optimization.md](references/power_optimization.md)**
- **Key Tools**: `bt_le_conn_param`, Advertising intervals, PHY selection.

## Quick Start (Advertising)
```kconfig
CONFIG_BT=y
CONFIG_BT_PERIPHERAL=y
```
```c
#include <zephyr/bluetooth/bluetooth.h>

void start_simple_adv(void) {
    bt_enable(NULL);
    bt_le_adv_start(BT_LE_ADV_CONN_NAME, NULL, 0, NULL, 0);
}
```

## Professional Patterns (Wireless Design)
- **Aggressive Latency**: Increase peripheral latency to allow the radio to stay off longer during quiet periods.
- **Decoupled Messaging**: Use Zbus to feed data into the BLE module, keeping the radio logic separate from the application logic.
- **Idle Bundling**: Use the "Send-When-Idle" pattern specifically to reduce the number of wake-ups for the radio controller.

## Automation Tools
- **[ble_timing_helper.py](scripts/ble_timing_helper.py)**: Convert advertising/connection intervals from ms to BLE timing units.

## Examples & Templates
- **[gatt_service_template.c](assets/gatt_service_template.c)**: Starter custom GATT service definition.

## Validation Checklist
- [ ] Device advertises with expected name/flags and is discoverable by a BLE scanner.
- [ ] Central can connect, exchange GATT data, and disconnect without stack errors.
- [ ] Configured connection parameters are reflected after negotiation.
- [ ] Send-When-Idle flow batches traffic instead of transmitting every sample immediately.

## Resources

- **[References](references/)**:
  - `ble_fundamentals.md`: GATT, GAP, and connection basics.
  - `send_when_idle.md`: Implementing the idle-bundle pattern.
  - `power_optimization.md`: Parameter tuning and power-saving Kconfigs.
- **[Scripts](scripts/)**:
  - `ble_timing_helper.py`: BLE interval conversion helper.
- **[Assets](assets/)**:
  - `gatt_service_template.c`: Custom service template for GATT.

## 来源与修改 / Provenance

- Upstream: [beriberikix/zephyr-agent-skills — skills/connectivity-ble](https://github.com/beriberikix/zephyr-agent-skills/tree/ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce/skills/connectivity-ble)
- Pinned commit: `ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce`
- License: `Apache-2.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
