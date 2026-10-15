---
name: c-fuzzing-obstacles
description: "Patches past the barriers that stop a fuzzer making progress — checksum and hash verification, magic-value validation, time-based seeds, and other non-deterministic global state. Covers locating the blocking check, neutering it behind a fuzzing build flag, and avoiding the false positives a patch can introduce. Use when a fuzzer is stuck at validation, when coverage shows large regions behind a checksum, or when valid inputs are impractical to generate."
---

# Fuzzing obstacles in firmware C

适用于校验和、认证、长度字段和状态前置条件阻挡深层 C 解析路径时。此摘编移除 Rust 专用实现；CC-BY-SA-4.0。

1. 先用覆盖率证明确实被前置校验阻挡，不把低覆盖一概归因于 checksum。
2. 优先构造合法最小 seed、字典、结构感知生成器或自定义 mutator，同时保持长度、类型及必要校验一致。
3. 如果必须提供 fuzz-only 旁路，放在明确的独立构建配置中，保留生产校验路径的单独测试。
4. 旁路认证/checksum 后的发现只说明该前提下的缺陷；验证攻击者在真实系统中能否到达，不能直接宣称可利用。
5. 比较修改前后的覆盖率和吞吐，确认没有绕过正在测试的真实逻辑、引入未定义行为或掩盖错误。
6. 测试结束检查生产构建没有 FUZZING 宏或旁路，保存原始与最小化失败输入作为回归。

参见 [harness](../c-harness-writing/SKILL.md)、[coverage](../c-coverage-analysis/SKILL.md) 和 [dictionary](../c-fuzzing-dictionary/SKILL.md)。

## 来源与修改 / Provenance

- Upstream: [trailofbits/skills — plugins/testing-handbook-skills/skills/fuzzing-obstacles](https://github.com/trailofbits/skills/tree/8e54050ae63c2f62224c35b1616efe71865b4777/plugins/testing-handbook-skills/skills/fuzzing-obstacles)
- Pinned commit: `8e54050ae63c2f62224c35b1616efe71865b4777`
- License: `CC-BY-SA-4.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
