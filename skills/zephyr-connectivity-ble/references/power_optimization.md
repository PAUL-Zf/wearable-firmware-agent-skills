# BLE energy and connection parameters

Adapted from the upstream reference; Apache-2.0, see parent SOURCE.json and LICENSE.

## Connection tradeoffs

Connection interval, peripheral latency and supervision timeout must satisfy the controller/host constraints and the product's latency budget. For conventional LE connections without subrating:

`supervision_timeout_ms > 2 * (1 + peripheral_latency) * max_connection_interval_ms`

The inequality is strict; also check all Bluetooth allowed ranges. A 2 s interval with latency 5 requires timeout greater than 24 s; 10 s is invalid. For a modest illustrative tuple, 100 ms maximum interval, latency 4 and 4 s timeout meets this inequality, but the central may reject or select different parameters.

Zephyr conventional connection interval units are 1.25 ms; timeout units are 10 ms. Confirm whether the specific API expects integer units or provides an explicit conversion macro. Log the accepted parameters rather than assuming the request was applied. Subrating and newer connection modes have additional constraints: use the relevant specification and installed stack.

## Energy workflow

1. Measure advertising, connection events, sampling, processing and sleep separately.
2. Bound batching by payload capacity and maximum sample age, not only inactivity.
3. Handle subscription, disconnection, notification errors, backpressure and negotiated MTU. A notification call returning success is not application-level acknowledgment.
4. Optimize radio/event frequency and data movement based on actual traces while retaining required responsiveness.
5. Verify battery-life assumptions with real current measurements and realistic connected/disconnected duty cycles.

Reference: [Zephyr connection API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html), using the project's versioned documentation.
