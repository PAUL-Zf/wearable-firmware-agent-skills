# 上游来源与筛选范围

上游均固定到 sources.lock.json 中的提交，不跟随 main/master 自动变化。Star 数未写入，避免将易变的热度当作质量证明。

| 上游 | 固定版本 | 迁移数 | 范围 |
|---|---|---:|---|
| [claude-skills](https://github.com/Jeffallan/claude-skills) | [1be15d8064f8](https://github.com/Jeffallan/claude-skills/commit/1be15d8064f88fc25216442406d40add8fd23b53) | 1 | MCU |
| [superpowers](https://github.com/obra/superpowers) | [bb92a7774141](https://github.com/obra/superpowers/commit/bb92a77741419a4ab5f06e711a283343f1ada0c3) | 3 | 开发流程 |
| [embedded-skills](https://github.com/rovinax/embedded-skills) | [022ce31b469b](https://github.com/rovinax/embedded-skills/commit/022ce31b469b1a1d0c1261c2c8d0f3e07b2c0bbc) | 6 | 固件设计 |
| [low-level-dev-skills](https://github.com/mohitmishra786/low-level-dev-skills) | [bdc58472fa9f](https://github.com/mohitmishra786/low-level-dev-skills/commit/bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608) | 27 | C 工具链与裸机 |
| [zephyr-agent-skills](https://github.com/beriberikix/zephyr-agent-skills) | [ed63cdfb8cdf](https://github.com/beriberikix/zephyr-agent-skills/commit/ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce) | 16 | Zephyr |
| [cmsis-skills](https://github.com/Open-CMSIS-Pack/cmsis-skills) | [25c2085a810e](https://github.com/Open-CMSIS-Pack/cmsis-skills/commit/25c2085a810ee531cc13df9d34ce2768cd84c421) | 14 | CMSIS 与 bring-up |
| [CMSIS-Developer-Assistant](https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant) | [29d444ce38a6](https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/commit/29d444ce38a6574a7763566a9c32902ac3181fca) | 9 | CMSIS MCP 集成 |
| [agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | [a3072641b750](https://github.com/sickn33/agentic-awesome-skills/commit/a3072641b750a1fb2f6ce695a5f984ea3d4c3ec1) | 2 | C 与 Cortex-M |
| [trailofbits-skills](https://github.com/trailofbits/skills) | [8e54050ae63c](https://github.com/trailofbits/skills/commit/8e54050ae63c2f62224c35b1616efe71865b4777) | 7 | C 主机测试 |
| [embedded-agent-skills](https://github.com/iharhl/embedded-agent-skills) | [1f46f2c4409e](https://github.com/iharhl/embedded-agent-skills/commit/1f46f2c4409e8179864babc87b8d38e24294336c) | 3 | 固件评审 |
| [embedded-systems-architect](https://github.com/Zachariah9420/embedded-systems-architect) | [623f09b2f82b](https://github.com/Zachariah9420/embedded-systems-architect/commit/623f09b2f82bcbbb2516f0cb79a7bbc49bd13be0) | 1 | 架构与证据 |
| [LibreEmbed-Claude-Code](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code) | [b3840586de71](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/commit/b3840586de7181db1cfb04214f8fbdb49a63ab09) | 11 | MCU 模式库 |

## 没有整体搬入的内容

- 各大合集中的前端、云平台、数据库、Rust/Zig/Python、GPU、FPGA、Linux 内核等非本次 MCU C 固件主题。
- Trail of Bits `c-review` 原工作流明确不适用于无 libc 的 bare-metal/embedded，未作为 MCU 审查流程搬入；使用 review-embedded 与本仓库 C 测试 Skills。
- Zephyr 工业协议、Matter/Thread、IP 云连接与原 zephyr-cli 安装路由不纳入；保留穿戴相关的叶子 Skills。
- CMSIS 厂商 PDSC 打包维护、Ethos-U/NPU 与 vendored 重复项不纳入；项目与 bring-up Skills 保留必要的配套知识项。
- LibreEmbed 的 embedded Linux、FPGA、云协议及安全认证模式不纳入；升级部分仅保留本地镜像/分区/恢复设计。
- 架构 Skill 中的 Jetson/Raspberry Pi 与模型转换/上传移除；仅提取 MCU 资源、BSP、数据流和验证方法。
- Golioth 专用云集成不属于本次底软范围，且此前未确认其内容许可，不复制。

本目录按此前已审阅来源构建。仅出现在搜索结果、尚未核对正文和许可证的候选项目不算已迁移；后续新增应先完成许可与技术核对。
