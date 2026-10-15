---
name: libre-firmware-update-patterns
description: "处理穿戴 MCU 固件升级、分块写入、镜像确认或失败回滚时使用；仅适用于 MCU C 固件。"
---

# 穿戴 MCU 固件升级、分块写入、镜像确认或失败回滚

从上游模式库提取 MCU/C 相关设计步骤，移除了未经目标验证的固定地址、寄存器与完整镜像示意代码。

1. 采用项目支持的 MCUboot/厂商打包工具生成镜像，不手写一个示意 header 当成有效签名镜像。
2. 核对分区、擦除/编程粒度、slot/trailer、工作空间、升级模式和链接地址。
3. CRC 检测传输损坏不能替代签名认证；完整验证边界、版本策略及可信根。
4. 设计断电恢复、下载中断、首次启动健康检查与确认/回滚流程，保护工厂校准和用户数据。
5. 用版本匹配的模拟或测试板覆盖分块边界、掉电点和坏镜像；未实测的回滚明确标记。

先读取项目约束与目标 SDK；输出设计契约、最小实现计划、错误处理与可复现验证。区分主机测试、模拟器结果和真实板上证据。

## 来源与修改 / Provenance

- Upstream: [Ormus-Solutions/LibreEmbed-Claude-Code — plugins/firmware-update/skills/firmware-update-patterns](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/tree/b3840586de7181db1cfb04214f8fbdb49a63ab09/plugins/firmware-update/skills/firmware-update-patterns)
- Pinned commit: `b3840586de7181db1cfb04214f8fbdb49a63ab09`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
