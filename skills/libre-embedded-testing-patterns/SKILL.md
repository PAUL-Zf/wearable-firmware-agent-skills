---
name: libre-embedded-testing-patterns
description: "处理C 驱动单元测试、Ceedling/CMock 或板上测试时使用；仅适用于 MCU C 固件。"
---

# C 驱动单元测试、Ceedling/CMock 或板上测试

从上游模式库提取 MCU/C 相关设计步骤，移除了未经目标验证的固定地址、寄存器与完整镜像示意代码。

1. 分离纯业务逻辑与可注入的 HAL 接口，真实目标逻辑参与测试。
2. 用 mock 注入超时、部分传输、队列满与设备错误；断言可观测行为和状态清理。
3. 记录 Ceedling/Unity/CMock 版本、依赖、配置和可复现命令。
4. 主机运行边界测试与适用 sanitizer；板上验证寄存器、DMA、ISR 时序和实际硬件错误。
5. 覆盖率说明未执行路径，不能把覆盖率数字当成正确性证明。

先读取项目约束与目标 SDK；输出设计契约、最小实现计划、错误处理与可复现验证。区分主机测试、模拟器结果和真实板上证据。

## 来源与修改 / Provenance

- Upstream: [Ormus-Solutions/LibreEmbed-Claude-Code — plugins/embedded-testing/skills/embedded-testing-patterns](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/tree/b3840586de7181db1cfb04214f8fbdb49a63ab09/plugins/embedded-testing/skills/embedded-testing-patterns)
- Pinned commit: `b3840586de7181db1cfb04214f8fbdb49a63ab09`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
