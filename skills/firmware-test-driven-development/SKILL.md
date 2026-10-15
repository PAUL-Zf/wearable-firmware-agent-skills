---
name: firmware-test-driven-development
description: "为可测试 C 模块添加功能或修复 bug，或设计 MCU 驱动的主机回归与板上验证边界时使用。"
---

# Test-driven C firmware changes

1. 选择一个可观测行为和最小失败例：协议长度、状态迁移、超时、错误恢复或资源释放。
2. 先运行用例，确认因预期缺陷失败，而非测试框架、路径或编译错误。
3. 编写使行为成立的最小实现，再运行该用例与相关回归。
4. 在测试保护下重构；避免测试只复述内部实现或只检查 mock 被调用。
5. 通过 HAL 接口注入总线返回、时间与故障；真实协议/状态机逻辑不能全部被 mock 替换。
6. 覆盖空输入、边界、溢出、部分传输、队列满、设备断开、重试和取消。
7. 主机测试不能证明 MMIO、DMA cache、ISR 时序或功耗；为这些保留最小板上验证步骤与测量标准。

对于尚未具备测试接缝的遗留驱动，先建立特征测试与最小硬件重现，再提取可测纯逻辑，避免为满足形式扩大修改。

## 来源与修改 / Provenance

- Upstream: [obra/superpowers — skills/test-driven-development](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/test-driven-development)
- Pinned commit: `bb92a77741419a4ab5f06e711a283343f1ada0c3`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
