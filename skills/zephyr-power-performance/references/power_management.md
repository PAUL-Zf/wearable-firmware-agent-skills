# Zephyr power management for wearable firmware

Adapted from the upstream power-management reference; Apache-2.0, see parent SOURCE.json and LICENSE.

## Version and board contract

Pin the Zephyr revision and exact board/SoC. Inspect its supported power states, DTS power-state nodes, PM policy, driver runtime-PM support and wake sources. Do not paste an overlay referencing an undefined state node or invent a state for unsupported hardware.

System PM and device runtime PM are distinct. Enable only the Kconfig options supported by the project revision and its drivers. Use the board/SoC PM implementation rather than overriding a low-level SoC hook from application code.

## Application workflow

1. Establish active users and pending DMA/bus transfers before releasing a peripheral.
2. Use the documented runtime get/put lifecycle for that revision, check returns and balance every acquired reference.
3. Coordinate sensor readiness, asynchronous completion and bus/controller power references; direct device suspend can break other clients.
4. Observe entry/exit through the revision's PM notifier API where appropriate. A notifier is not a replacement for driver suspend/resume handling.
5. Validate actual residency, wake latency, clock/tick restoration and data integrity. Document debugger and logging effects.

`pm_state_set` is a SoC hook; current documentation uses `void pm_state_set(enum pm_state state, uint8_t substate_id)`. Do not copy an invented `pm_state_info` signature into an application.

## Acceptance

Measure complete duty cycles with an appropriate current probe. Verify pending-work sleep races, sensor IRQ wake, BLE reconnection, bus errors and repeated suspend/resume. Power-budget estimates must name assumptions and cannot replace measurements.

Official references: [system PM hooks](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__hooks.html), [runtime device PM](https://docs.zephyrproject.org/latest/services/pm/device_runtime.html). Use the corresponding versioned documentation for the project.
