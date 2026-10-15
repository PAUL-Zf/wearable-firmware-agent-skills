---
name: libre-bare-metal-patterns
description: "处理MCU 裸机启动、寄存器、时间基准或中断接收时使用；仅适用于 MCU C 固件。"
---

# MCU 裸机启动、寄存器、时间基准或中断接收

从上游模式库提取 MCU/C 相关设计步骤，移除了未经目标验证的固定地址、寄存器与完整镜像示意代码。

1. 核对 startup、向量表、链接脚本及 .data 搬运/.bss 清零。
2. 按 MMIO 寄存器的 W1C/W0C/read-to-clear 属性操作，不能套用通用 read-modify-write 宏。
3. 轮询必须有超时与错误处理；计时考虑回绕、时钟变更和中断屏蔽。
4. UART 环形缓冲需要同步、可见性、容量及溢出策略；volatile 并不是完整的 SPSC 协议。
5. 使用项目 CMSIS device header，不把某一 STM32 的地址和位定义推广到其他芯片。

先读取项目约束与目标 SDK；输出设计契约、最小实现计划、错误处理与可复现验证。区分主机测试、模拟器结果和真实板上证据。

## 来源与修改 / Provenance

- Upstream: [Ormus-Solutions/LibreEmbed-Claude-Code — plugins/bare-metal/skills/bare-metal-patterns](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/tree/b3840586de7181db1cfb04214f8fbdb49a63ab09/plugins/bare-metal/skills/bare-metal-patterns)
- Pinned commit: `b3840586de7181db1cfb04214f8fbdb49a63ab09`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
