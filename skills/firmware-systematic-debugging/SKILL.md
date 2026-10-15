---
name: firmware-systematic-debugging
description: "定位 C 固件崩溃、HardFault、DMA 数据损坏、RTOS 卡死、外设失效或功耗回归时使用。"
---

# Systematic firmware debugging

## 先找原因

1. 固定可复现步骤、硬件/SDK/工具链版本、ELF、输入与现象。保留错误全文和最早失败证据。
2. 找到已知正常版本或最小正常示例，逐项比较时钟、引脚、内存、IRQ、初始化与数据契约。
3. 跨任务、驱动和硬件边界记录输入/输出、时间戳和错误计数；选择不会破坏目标问题的观测手段。
4. 每次提出一个可被否证的假设，用最小实验验证；不能同时改多个无关设置再把恢复归因于猜测。
5. 从错误现场追踪到最初破坏不变量的位置，而不是仅修正最后一次空指针或延长超时。
6. 若连续尝试不能解释结果，回看系统假设与架构，停止叠加无证据补丁。

## 修复与验证

为真正根因建立失败用例；纯 C 模块优先主机回归，硬件/并发问题记录板上重现步骤。
最小修复后执行原失败场景、相关回归及最坏负载，报告哪些结论来自主机、哪些来自硬件。

## 来源与修改 / Provenance

- Upstream: [obra/superpowers — skills/systematic-debugging](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/systematic-debugging)
- Pinned commit: `bb92a77741419a4ab5f06e711a283343f1ada0c3`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
