---
name: c-address-sanitizer
description: "在主机验证 C/C++ 固件模块的越界、use-after-free、double-free 或 fuzz 崩溃时使用。"
---

## Firmware scope

Use for host-testable C firmware modules and C++ harnesses around C APIs. MCU hardware, DMA,
ISR timing and power need separate on-target verification. Rust/Python fuzzing integrations are
outside this port. External fuzzers, compilers and runtimes are prerequisites, not bundled tools.

# AddressSanitizer for host-tested firmware C

ASan 是主机测试工具；不要假设裸机 MCU 链接了 ASan 运行时。先将协议解析、状态机和算法与 HAL 隔离，并记录主机与目标的 ABI、端序和内存布局差异。

## 工作流

1. 使用支持的 Clang/GCC 与运行时，在编译和最终链接阶段都加 sanitizer 选项。
2. 示例：`clang -std=c11 -O1 -g -fno-omit-frame-pointer -fsanitize=address,undefined module.c test.c -o test`。
3. 运行测试，保存原始 stderr、退出码、精确命令、编译器版本和输入；读取第一份错误的访问栈与分配/释放栈。
4. 复现并缩小失败输入，修复根因，将输入加入回归测试。
5. 明确 ASan 未覆盖的路径、数据竞争、MMIO、DMA 与目标实时行为。

平台能力以安装的编译器/运行时为准，不应笼统排除 macOS 或 Windows。
ASan shadow memory 的虚拟地址保留不是实际 RSS，大小依平台而异；不要把 20TB 当作通用常量。
libFuzzer 的 `-rss_limit_mb` 限制 RSS，不是虚拟地址；按实测设定有限预算，不能为 shadow memory 默认关掉 RSS 限制。
AFL++ 的内存限制单位及 ASan 支持配置需按安装版本检查，并使用外部资源控制。
LeakSanitizer 支持和默认值依平台/构建而异；关闭泄漏检查需要记录原因，另做适用的泄漏回归。

[Clang 官方文档](https://clang.llvm.org/docs/AddressSanitizer.html)

## 来源与修改 / Provenance

- Upstream: [trailofbits/skills — plugins/testing-handbook-skills/skills/address-sanitizer](https://github.com/trailofbits/skills/tree/8e54050ae63c2f62224c35b1616efe71865b4777/plugins/testing-handbook-skills/skills/address-sanitizer)
- Pinned commit: `8e54050ae63c2f62224c35b1616efe71865b4777`
- License: `CC-BY-SA-4.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
