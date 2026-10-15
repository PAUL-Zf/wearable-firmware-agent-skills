---
name: embedded-isr-design
description: "设计或评审 MCU ISR、DMA 回调、RTOS ISR 到任务通信、数据丢失与中断延迟问题时使用。"
---

# Embedded ISR design

ISR 应具有明确、可测量的有界工作量。先确定硬件事件语义、最坏到达频率、可丢失性与系统实时预算。

## 设计步骤

1. 从手册确认事件确认顺序、标志清除方式、FIFO 深度与错误恢复；只处理属于本次事件的状态。
2. 捕获必要时间戳和有限数据，再交给任务或主循环。一般避免 ISR 内解析、日志、堆分配、阻塞和复杂数学。
3. 极短且有确定时限的控制动作可在 ISR 中完成，前提是完整响应时间分析与测量支持；不要把应用类型当成绝对禁令。
4. FreeRTOS 使用适用的 FromISR 接口及该 port 的优先级/yield 规则。CMSIS-RTOS2、Zephyr 的命名和允许接口不同，查各自契约；例如 CMSIS 队列 ISR timeout 必须为 0。
5. 单标志只能表示可合并事件；UART/采样数据用有界队列或 ring buffer，并明确满时丢新、丢旧、停流或背压策略和计数。
6. 双缓冲也需要明确切换同步和所有权；volatile 不提供原子性、内存顺序或完整结构体快照。
7. 临界区恢复原中断屏蔽状态；RTOS 中使用 port 接口。NVIC 优先级由截止期和内核 API 限制共同决定。
8. 用逻辑分析仪、trace 或可用的周期计数器测最坏 ISR 时间、嵌套时延和任务唤醒时延；不能套用固定 GPIO 5μs 等预算。

## 验收

覆盖峰值连续流、缓冲回绕/溢出、总线错误、同时到达、任务迟滞和重入。
检查 W1C/W0C/read-to-clear 寄存器，不能用通用 `|=` 清除任意中断标志。
交付 IRQ → handoff → consumer 的路径、容量推导、错误计数和真实测试证据。

## 来源与修改 / Provenance

- Upstream: [rovinax/embedded-skills — skills/embedded-isr-design](https://github.com/rovinax/embedded-skills/tree/022ce31b469b1a1d0c1261c2c8d0f3e07b2c0bbc/skills/embedded-isr-design)
- Pinned commit: `022ce31b469b1a1d0c1261c2c8d0f3e07b2c0bbc`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
