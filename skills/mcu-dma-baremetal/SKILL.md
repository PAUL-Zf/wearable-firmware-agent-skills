---
name: mcu-dma-baremetal
description: "配置 UART/SPI/ADC DMA、循环或双缓冲，排查 MCU DMA 不启动、丢数或 Cortex-M7 cache 一致性时使用。"
---

# DMA setup and ownership

1. 从器件手册核对外设 DMA 请求映射、控制器/通道/stream、DMAMUX、IRQ 及存储器可达性。
2. 列出方向、宽度、元素数、对齐、递增、循环方式、half/full/error 事件和溢出策略。
3. 按硬件规定停用并等待完成，再改描述符或寄存器；清理当前请求和错误状态，随后按规定顺序启动。
4. 明确 CPU 与 DMA 对每块缓冲区的所有权；DMA 使用时 CPU 不得修改或消费尚未完成的区间。
5. ISR 仅确认本次事件并移交已完成区间；循环模式必须防止处理端落后一圈而静默覆盖。

## Cortex-M7 cache

- 优先选择该 DMA 可达的 SRAM；DTCM 不是通用 DMA 内存。在 STM32H7，DMA1/2 与 MDMA 可达域不同。
- 非 cacheable 区也要满足 DMA 总线、对齐和排序约束。
- cacheable TX：CPU 写入后，在交给 DMA 前 clean 对应 cache lines。
- cacheable RX：交给 DMA 前按 SDK 的 DMA ownership 协议处理已有 cache lines，完成后、CPU 读取前 invalidate。
- 缓冲区独占完整 cache lines，按实际 cache line 向外对齐维护范围，避免丢失邻近对象的脏数据。
- barrier 解决顺序，不替代 cache 维护；具体调用签名和长度要求以 SDK/CMSIS 版本为准。

## 验证

检查 map 文件中的地址与 alignment，读取剩余传输计数和错误状态；以递增数据模式检测缺失、重复、乱序。
覆盖连续流、短包、边界回绕、CPU 高负载和 cache 开关；保留计数与逻辑分析仪证据。

## 来源与修改 / Provenance

- Upstream: [mohitmishra786/low-level-dev-skills — skills/baremetal/dma-baremetal](https://github.com/mohitmishra786/low-level-dev-skills/tree/bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608/skills/baremetal/dma-baremetal)
- Pinned commit: `bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
