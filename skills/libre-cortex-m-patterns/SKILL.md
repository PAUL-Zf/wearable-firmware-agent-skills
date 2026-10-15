---
name: libre-cortex-m-patterns
description: "处理Cortex-M SysTick、NVIC、FPU、MPU、DWT 或向量表配置时使用；仅适用于 MCU C 固件。"
---

# Cortex-M SysTick、NVIC、FPU、MPU、DWT 或向量表配置

从上游模式库提取 MCU/C 相关设计步骤，移除了未经目标验证的固定地址、寄存器与完整镜像示意代码。

1. 从核/芯片/SDK 确认功能是否存在，不能假设所有 Cortex-M 都支持 DWT、FPU 或相同 MPU。
2. 核对中断优先级位数、分组和 RTOS 阈值，避免重配其 SysTick/PendSV。
3. 向量表位置与对齐由目标规定；核对初始 SP、复位向量和链接脚本。
4. 浮点 ABI、启动使能与异常上下文必须一致；MPU region 的尺寸、对齐和优先级按架构处理。
5. 用硬件计数器或 trace 测时，并记录计数器可用性、频率、溢出与调试器影响。

先读取项目约束与目标 SDK；输出设计契约、最小实现计划、错误处理与可复现验证。区分主机测试、模拟器结果和真实板上证据。

## 来源与修改 / Provenance

- Upstream: [Ormus-Solutions/LibreEmbed-Claude-Code — plugins/arm-cortex-m/skills/cortex-m-patterns](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/tree/b3840586de7181db1cfb04214f8fbdb49a63ab09/plugins/arm-cortex-m/skills/cortex-m-patterns)
- Pinned commit: `b3840586de7181db1cfb04214f8fbdb49a63ab09`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
