---
name: embedded-systems
description: "开发 MCU C 固件、外设驱动、RTOS 应用或优化穿戴设备的 RAM、Flash、实时性与功耗时使用。"
---

# Embedded systems for wearable firmware

## 建立约束

先读取项目 AGENTS.md、构建入口、MCU 完整型号与修订、SDK/RTOS 版本、原理图和勘误。
列出 Flash/RAM、栈、采样率、最大延迟、丢包容忍度、唤醒时间和电池预算；缺失项明确写未知。

## 实施流程

1. 画清传感器 → DMA/ISR → 缓冲区 → 工作任务 → BLE/存储的数据流和所有权。
2. 先确定中断与任务边界、超时、缓冲容量和溢出策略，再写驱动。
3. ISR 仅完成必要的确认、采集和移交；数据流使用有界队列或环形缓冲区，不能用单字节加标志替代。
4. 使用目标 RTOS 的同步与临界区接口；裸机需保存并恢复此前屏蔽状态。volatile 本身不提供原子性或同步。
5. 检查对象创建、启动任务、驱动调用和队列发送的返回值；定义失败恢复与可观测计数。
6. 按项目编译选项构建；主机验证纯 C 算法、协议和状态机，板上测量 ISR 时延、数据完整性与功耗。
7. 报告实际构建和量测结果，区分已验证、估算和待验证。水位值不是最坏栈占用的证明。

## 按需参考

- [微控制器与外设](references/microcontroller-programming.md)
- [RTOS](references/rtos-patterns.md)
- [功耗](references/power-optimization.md)
- [通信](references/communication-protocols.md)
- [内存](references/memory-optimization.md)

这些是平台示例；芯片手册、项目 SDK 和端口契约决定寄存器、时钟和 API 的具体用法。

## 来源与修改 / Provenance

- Upstream: [Jeffallan/claude-skills — skills/embedded-systems](https://github.com/Jeffallan/claude-skills/tree/1be15d8064f88fc25216442406d40add8fd23b53/skills/embedded-systems)
- Pinned commit: `1be15d8064f88fc25216442406d40add8fd23b53`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
