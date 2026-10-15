---
name: wearable-architecture-evidence
description: "评估智能穿戴 MCU 方案、BSP/SDK、固件架构、RAM/Flash/功耗可行性，或整理资料与设计验证实验时使用。"
---

# Wearable firmware architecture and evidence

继承上游“建立认知 → 选择模块 → 最小实验 → 收集结果 → 更新认知”的证据驱动方法，仅保留 MCU 固件适用部分。

1. 优先读取项目已有的约束文档，确认板卡 revision、芯片、SDK/BSP、RTOS、工具链、存储器、传感器、无线和电源域。
2. 将每个影响决策的判断标为已确认、工程推论、估算、待验证或资料不足，并附代码、手册页或测量依据。
3. 从采样到消费画清数据流、线程/ISR 边界、缓冲所有权、峰值吞吐及背压；分别估算静态 RAM、栈、堆和 DMA 缓冲区。
4. 检查 SDK sample 的芯片/板卡/版本与许可证；不能把“示例编译通过”写成产品可行性证明。
5. 资源评估包括时钟、带宽、数据搬运、cache、外设竞争和唤醒时限；MHz 和容量不能单独证明能满足需求。
6. 每个关键未知量设计一个最小实验，记录前置条件、命令、输入、日志、成功/失败条件和结果如何改变方案。
7. 部署或升级计划包含镜像版本、分区、恢复入口、失败保留日志和读回验证；只在当前任务授权范围内操作硬件。
8. 交付按证据组织的约束表、方案取舍、实验卡和待验证事项，复用项目已有记录格式。

本迁移排除了 Jetson/Raspberry Pi、NPU 模型转换和模型上传流程，也未带入需要这些资料的脚本。

## 来源与修改 / Provenance

- Upstream: [Zachariah9420/embedded-systems-architect — .](https://github.com/Zachariah9420/embedded-systems-architect/tree/623f09b2f82bcbbb2516f0cb79a7bbc49bd13be0/.)
- Pinned commit: `623f09b2f82bcbbb2516f0cb79a7bbc49bd13be0`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
