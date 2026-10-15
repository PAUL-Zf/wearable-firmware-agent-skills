---
name: libre-debug-trace-patterns
description: "处理MCU HardFault、栈破坏、watchpoint 或 trace 排查时使用；仅适用于 MCU C 固件。"
---

# MCU HardFault、栈破坏、watchpoint 或 trace 排查

从上游模式库提取 MCU/C 相关设计步骤，移除了未经目标验证的固定地址、寄存器与完整镜像示意代码。

1. 保存同一构建的 ELF/map、芯片与固件版本和最初故障现场。
2. 按 EXC_RETURN、MSP/PSP 及 FPU/安全扩展选择异常帧；有效位不成立时不能解释故障地址。
3. 用 addr2line、反汇编、调用上下文与访问权限逐步验证根因。
4. watchpoint/ITM/DWT 要核对核支持、资源数和调试影响，不默认所有板都可用。
5. 避免在故障上下文调用复杂日志或读有副作用的外设寄存器。

先读取项目约束与目标 SDK；输出设计契约、最小实现计划、错误处理与可复现验证。区分主机测试、模拟器结果和真实板上证据。

## 来源与修改 / Provenance

- Upstream: [Ormus-Solutions/LibreEmbed-Claude-Code — plugins/debug-trace/skills/debug-trace-patterns](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/tree/b3840586de7181db1cfb04214f8fbdb49a63ab09/plugins/debug-trace/skills/debug-trace-patterns)
- Pinned commit: `b3840586de7181db1cfb04214f8fbdb49a63ab09`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
