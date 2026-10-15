---
name: libre-bootloader-patterns
description: "处理MCU bootloader、应用跳转、Flash 分区或升级恢复时使用；仅适用于 MCU C 固件。"
---

# MCU bootloader、应用跳转、Flash 分区或升级恢复

从上游模式库提取 MCU/C 相关设计步骤，移除了未经目标验证的固定地址、寄存器与完整镜像示意代码。

1. 从具体 Flash bank/sector/page 几何和擦写期间取指限制设计分区；软件 A/B slots 不等于硬件 dual-bank。
2. 不要把 STM32F407 1MB 的两个软件区域描述成可独立读写的 dual-bank 硬件。
3. 验证镜像边界、入口、初始栈、向量对齐和真实性，保留恢复入口及工厂数据。
4. 交接应用时按 SDK 处理 IRQ、pending 状态、tick、DMA、cache、栈和向量表；TrustZone 需专门契约。
5. 覆盖坏镜像、掉电和看门狗恢复；记录何时确认升级及如何回滚，不能用一次跳转演示代替完整启动协议。

先读取项目约束与目标 SDK；输出设计契约、最小实现计划、错误处理与可复现验证。区分主机测试、模拟器结果和真实板上证据。

## 来源与修改 / Provenance

- Upstream: [Ormus-Solutions/LibreEmbed-Claude-Code — plugins/bootloader-design/skills/bootloader-patterns](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/tree/b3840586de7181db1cfb04214f8fbdb49a63ab09/plugins/bootloader-design/skills/bootloader-patterns)
- Pinned commit: `b3840586de7181db1cfb04214f8fbdb49a63ab09`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
