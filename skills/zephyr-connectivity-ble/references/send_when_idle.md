# Bounded BLE batching

Adapted from the upstream send-when-idle concept; Apache-2.0, see parent SOURCE.json and LICENSE.

An inactivity timer alone never fires during continuous sampling. Wearable streaming therefore needs three triggers: idle time, maximum batch age and maximum payload/queue size.

1. Use a bounded queue or buffer with explicit ownership and synchronization. Zbus channels may represent latest state, not an unlimited lossless history.
2. On the first sample of an empty batch, establish a maximum-age deadline that subsequent samples cannot postpone.
3. Optionally maintain a separate idle timer. Send when idle expires, the fixed age deadline arrives, or the batch reaches its payload threshold.
4. Schedule transmission outside sensor/ISR critical paths. Do not block a shared system workqueue with a long send or retry loop.
5. Observe actual MTU, subscription and connection state. Handle backpressure and retry with bounds; preserve or drop samples according to an explicit policy and expose overflow counts.
6. Test continuous input, burst input, sparse input, disconnect/reconnect and a slow consumer; verify maximum sample age and memory usage.

Choose relevant `k_work_delayable` scheduling APIs from the pinned Zephyr version. Initialize work before scheduling it, define cancellation/shutdown ownership and protect buffers against simultaneous producers and work handlers.
