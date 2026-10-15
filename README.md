# Wearable Firmware Agent Skills

为 **Codeagent / Claude Code 类 CLI Agent** 整理的智能穿戴底层固件 Skills，聚焦 **C、MCU、RTOS、驱动、BLE、低功耗、调试与测试**。

目前收录 **100 个 Skill，来自 12 个 GitHub 上游仓库**。只迁移相关叶子 Skill 或相关内容摘编；每项含来源、固定提交、许可证与修改记录。中文用于导读和重点适配，部分保留的上游参考资料为英文。

[完整索引](docs/CATALOG.md) · [来源与排除范围](SOURCES.md) · [迁移与纠错记录](MIGRATION.md) · [验证记录](docs/VALIDATION.md)

## 从这几项开始

| 场景 | 建议 Skill |
|---|---|
| 写/审查 C 模块 | [c-pro](skills/c-pro/SKILL.md)、[review-embedded](skills/review-embedded/SKILL.md) |
| 驱动与 ISR | [embedded-systems](skills/embedded-systems/SKILL.md)、[embedded-isr-design](skills/embedded-isr-design/SKILL.md) |
| MCU DMA/HardFault | [mcu-dma-baremetal](skills/mcu-dma-baremetal/SKILL.md)、[arm-cortex-expert](skills/arm-cortex-expert/SKILL.md) |
| FreeRTOS | [mcu-freertos](skills/mcu-freertos/SKILL.md) |
| Zephyr 传感器 + BLE | [zephyr-hardware-io](skills/zephyr-hardware-io/SKILL.md)、[zephyr-connectivity-ble](skills/zephyr-connectivity-ble/SKILL.md) |
| 功耗与待机 | [mcu-low-power-embedded](skills/mcu-low-power-embedded/SKILL.md)、[zephyr-power-performance](skills/zephyr-power-performance/SKILL.md) |
| 没有硬件，先测 C 逻辑 | [c-harness-writing](skills/c-harness-writing/SKILL.md)、[c-libfuzzer](skills/c-libfuzzer/SKILL.md)、[c-address-sanitizer](skills/c-address-sanitizer/SKILL.md) |
| 先定位再修改 | [firmware-systematic-debugging](skills/firmware-systematic-debugging/SKILL.md) |

同一任务挑一套主工作流即可。`mcu-*` 偏工具链/裸机，`zephyr-*` 用于 Zephyr；`libre-*` 是精简模式指南，可按需补充。

## 安装与使用

仓库采用 `skills/<name>/SKILL.md` 结构，不依赖专有安装器。**Codeagent 是内部改造版本，其 Skill 目录和启用方式以公司文档为准**，不能保证所有 Claude Code 命令都通用。

```sh
git clone https://github.com/PAUL-Zf/wearable-firmware-agent-skills.git
cd wearable-firmware-agent-skills
python3 scripts/install_skills.py --list
```

将选中的整个 Skill 目录复制到实际配置的目录，必须一并保留 references/scripts/assets、LICENSE、NOTICE（如有）和 SOURCE.json。安装器要求显式指定目标，不覆盖已有同名目录：

```sh
# 示例：仅当你的 Codeagent 确实使用该项目级目录时
python3 scripts/install_skills.py --dest /path/to/project/.claude/skills c-pro embedded-isr-design firmware-systematic-debugging

# Zephyr 配套项建议成组复制，避免缺少交叉引用的同伴 Skill
python3 scripts/install_skills.py --dest /path/to/project/.claude/skills --group Zephyr
```

选用后，以自然语言说明任务并让 Agent 读取对应 SKILL.md；自动触发/显式调用是否可用，取决于内部 Codeagent 的实现。

示例任务：

> 按 c-pro 和 c-harness-writing 审查这个 C 帧解析器。先列长度与所有权契约，再设计主机边界测试和 fuzz harness；实际运行可用检查，明确尚未验证的部分。

> 按 mcu-dma-baremetal 排查 SPI DMA 偶发错数。先核对芯片总线矩阵、缓冲区链接位置和 cache ownership，再提出一个最小验证实验。

> 按 zephyr-hardware-io、zephyr-connectivity-ble 和 zephyr-power-performance 设计传感器采样上报。先确认 Zephyr/SDK 版本，再给出有界缓冲、最大批次年龄、BLE 参数与功耗测量计划。

## 运行条件

- C 主机测试：需支持的编译器、运行时及实际 C 模块；ASan/libFuzzer 不默认运行在裸机 MCU 上。
- 交叉构建、仿真、调试：需对应 SDK、工具链、板卡配置；板上测试另需硬件和探针。
- **CMSIS MCP 集成组**：需 CMSIS Developer Assistant MCP、匹配的 VS Code 扩展及 CMSIS-Toolbox。独立 CLI 不会自动提供这些工具。
- CMSIS 项目与 bring-up 组存在配套知识依赖，安装器会一起复制该组。遇到未提供的外部工具应报告依赖，不能模拟成功输出。
- Zephyr 的 Python 辅助检查中，board/module YAML 检查需 PyYAML；其他工具依赖见对应 Skill。

所有平台代码和模板都需要按具体芯片、勘误、SDK 和 RTOS port 核对。当前检查包括结构、来源、链接、脚本及指定样例验证；**尚未在具体穿戴板卡上验证**。

## 更新与校验

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
```

上游版本与文件哈希记录在 [sources.lock.json](sources.lock.json)。更新时对照旧版与新版逐项审阅，更新 SOURCE.json、纠错记录和哈希后再提交；不要用上游整目录覆盖已经修正的适配版本。

## 许可证

这是多许可证汇编，**没有将所有上游内容统一改成 MIT**。每个 Skill 及其适配内容按目录内 LICENSE / SOURCE.json 标明的许可证分发；Trail of Bits 摘编保留 CC-BY-SA-4.0。保留上游版权及 Apache NOTICE。

本仓库原创的安装/校验脚本、测试和导读按根目录 [LICENSE](LICENSE) 中明确的 MIT 部分使用。
