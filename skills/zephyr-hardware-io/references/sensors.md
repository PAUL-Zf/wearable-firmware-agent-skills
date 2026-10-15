# Zephyr sensor access

Adapted from the upstream sensors reference; Apache-2.0, see parent SOURCE.json and LICENSE.

## Initial bring-up

Confirm devicetree bus, address/chip-select, interrupt pin, power supply and driver Kconfig. Check device readiness, identity and startup timing against the sensor datasheet.

## Fetch/get path

For drivers supporting it, use `sensor_sample_fetch(dev)` followed by `sensor_channel_get(dev, channel, &value)`, checking each return. Serialize fetch/get pairs where shared driver state requires it; a second client must not overwrite samples between the two operations.

Choose the actual channel and output array shape from the driver contract. A vector channel needs storage for all returned axes. Sensor value units and conversion must follow channel documentation; include calibration, range and overflow handling.

## Triggered and streaming paths

Check the driver and pinned Zephyr revision before choosing trigger, FIFO, RTIO or Read/Decode. The former example `sensor_read(dev, &ctx, SENSOR_CHAN_ALL)` was removed because it does not represent a reliable API contract.

Read/Decode uses an encoded sample buffer and a compatible decoder, with RTIO/iodev configuration depending on the version and driver. Follow the same-version official sample rather than inventing a decode-context layout or mixing fetch/get and async semantics.

## Acceptance

Validate rate, timestamp origin, dropped samples, FIFO overflow, bus failures, startup and resume. Use continuous-load tests to bound ISR-to-consumer delay and buffer capacity. Record on-target evidence separately from host mock tests.

Official references: [sensor API](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html), [Read and Decode](https://docs.zephyrproject.org/latest/hardware/peripherals/sensor/read_and_decode.html).
