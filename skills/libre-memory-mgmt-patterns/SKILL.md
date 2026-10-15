---
name: libre-memory-mgmt-patterns
description: "处理MCU 静态对象、内存池、栈/堆预算或内存区域放置时使用；仅适用于 MCU C 固件。"
---

# MCU 静态对象、内存池、栈/堆预算或内存区域放置

从上游模式库提取 MCU/C 相关设计步骤，移除了未经目标验证的固定地址、寄存器与完整镜像示意代码。

1. 根据实时性采用静态 RTOS 对象或有界内存池，记录初始化失败和耗尽策略。
2. 区分 CPU-only 与 DMA-accessible 区域；链接地址以具体芯片 map 和总线矩阵为准。
3. 内存池必须验证指针来源、重复归还与索引；不能先对任意指针做数组指针相减。
4. 明确对象所有权与共享上下文，临界区要遵守 RTOS port。
5. 用实际 map/size 和最坏路径栈观测评估资源；不套用固定 printf 栈占用估值。

先读取项目约束与目标 SDK；输出设计契约、最小实现计划、错误处理与可复现验证。区分主机测试、模拟器结果和真实板上证据。

## 来源与修改 / Provenance

- Upstream: [Ormus-Solutions/LibreEmbed-Claude-Code — plugins/memory-management/skills/memory-mgmt-patterns](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/tree/b3840586de7181db1cfb04214f8fbdb49a63ab09/plugins/memory-management/skills/memory-mgmt-patterns)
- Pinned commit: `b3840586de7181db1cfb04214f8fbdb49a63ab09`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
