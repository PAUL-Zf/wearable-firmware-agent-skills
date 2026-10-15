---
name: libre-rtos-patterns
description: "处理RTOS 优先级反转、ISR 延后处理、任务栈或看门狗策略时使用；仅适用于 MCU C 固件。"
---

# RTOS 优先级反转、ISR 延后处理、任务栈或看门狗策略

从上游模式库提取 MCU/C 相关设计步骤，移除了未经目标验证的固定地址、寄存器与完整镜像示意代码。

1. 按 deadline、阻塞与执行预算划分任务，识别高优先级忙等导致的饥饿。
2. 区分 mutex 保护资源与 semaphore/notification 通知事件；不能在 ISR 获取普通 mutex。
3. 分析完整锁链、持锁时间及优先级继承局限，避免嵌套锁和锁内阻塞。
4. 看门狗依据各关键任务有效进展共同判定，不能由无条件定时器喂狗掩盖任务卡死。
5. 使用最坏路径栈测试与错误注入，结合 port 规则验证 FromISR API 和优先级。

先读取项目约束与目标 SDK；输出设计契约、最小实现计划、错误处理与可复现验证。区分主机测试、模拟器结果和真实板上证据。

## 来源与修改 / Provenance

- Upstream: [Ormus-Solutions/LibreEmbed-Claude-Code — plugins/rtos-patterns/skills/rtos-patterns](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/tree/b3840586de7181db1cfb04214f8fbdb49a63ab09/plugins/rtos-patterns/skills/rtos-patterns)
- Pinned commit: `b3840586de7181db1cfb04214f8fbdb49a63ab09`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
