---
name: libre-communication-buses
description: "处理I2C/SPI/UART 总线驱动或传感器通信故障时使用；仅适用于 MCU C 固件。"
---

# I2C/SPI/UART 总线驱动或传感器通信故障

从上游模式库提取 MCU/C 相关设计步骤，移除了未经目标验证的固定地址、寄存器与完整镜像示意代码。

1. 明确 7/10-bit 地址和 HAL 是否要求左移；读寄存器需要 repeated START 时不能拆成不符合器件协议的事务。
2. 依据总线电容、上升时间和器件灌电流确定 I2C pull-up；不使用固定电阻表代替计算与测量。
3. 从传感器手册核对 SPI 模式、CS setup/hold、dummy byte、多字节自动递增与最大频率。
4. UART RX 使用有界 FIFO/环形缓冲或 DMA，核算峰值吞吐、消费者迟滞、溢出计数和背压。
5. 确认超时、取消、总线恢复和错误状态机；恢复时考虑其他总线主机及器件复位语义。

先读取项目约束与目标 SDK；输出设计契约、最小实现计划、错误处理与可复现验证。区分主机测试、模拟器结果和真实板上证据。

## 来源与修改 / Provenance

- Upstream: [Ormus-Solutions/LibreEmbed-Claude-Code — plugins/communication-buses/skills/communication-buses](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/tree/b3840586de7181db1cfb04214f8fbdb49a63ab09/plugins/communication-buses/skills/communication-buses)
- Pinned commit: `b3840586de7181db1cfb04214f8fbdb49a63ab09`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
