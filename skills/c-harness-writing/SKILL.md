---
name: c-harness-writing
description: "为 C 固件协议解析、配置存储、状态机或算法编写 libFuzzer/AFL++ 主机 harness 时使用。"
---

## Firmware scope

Use for host-testable C firmware modules and C++ harnesses around C APIs. MCU hardware, DMA,
ISR timing and power need separate on-target verification. Rust/Python fuzzing integrations are
outside this port. External fuzzers, compilers and runtimes are prerequisites, not bundled tools.

# Fuzz harness for C firmware

1. 选择接收不可信字节的真正入口：BLE/UART 帧、升级元数据、NVM 记录、长度解码与状态迁移。
2. 把硬件访问隔离为确定性 stub；每次迭代重置状态、释放分配和恢复 mock，避免跨轮污染。
3. 设置资源上限与必要长度检查；不要过滤掉本应由目标处理的非法协议输入。
4. 解码宽整数时先检查剩余长度，使用字节移位或 memcpy，再按协议转换端序。禁止未对齐且违反别名规则的 `*(uint32_t *)data`。
5. 不把 C++ 容器的空向量 `&v[0]` 传入函数；按 API 空输入契约使用 data() 和长度。
6. 对输入驱动的多步骤 API 保留操作序列，限定操作次数与分配预算，覆盖 reset、重试、取消和失败路径。
7. 链接目标实际 C 实现，在主机支持时开启 ASan/UBSan；保留随机种子、corpus、构建版本与原始 crash。
8. 用覆盖率检查是否经过目标路径，而非只覆盖 harness；把最小失败输入纳入回归。

## 最小入口

C 源文件可以定义 `int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)`，包含 stdint.h 和 stddef.h，调用已隔离的目标 API 并返回 0。
如入口位于 C++ 文件则使用 `extern "C"`；C 目标头文件需要适当的 C linkage。libFuzzer 构建方式参见 [c-libfuzzer](../c-libfuzzer/SKILL.md)。

交付目标选择理由、harness、编译/运行命令、资源预算、覆盖证据和崩溃复现方式。主机 fuzz 不能替代板上 DMA/时序测试。

## 来源与修改 / Provenance

- Upstream: [trailofbits/skills — plugins/testing-handbook-skills/skills/harness-writing](https://github.com/trailofbits/skills/tree/8e54050ae63c2f62224c35b1616efe71865b4777/plugins/testing-handbook-skills/skills/harness-writing)
- Pinned commit: `8e54050ae63c2f62224c35b1616efe71865b4777`
- License: `CC-BY-SA-4.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
