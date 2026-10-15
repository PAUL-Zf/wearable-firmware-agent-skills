---
name: firmware-verification-before-completion
description: "准备宣称固件问题已修复、构建已通过、性能或功耗已达标，或提交 C/MCU 变更前使用。"
---

# Verification before completion

每项完成声明都要有本次变更之后取得的对应证据。

1. 确定声明：“构建通过”“主机用例通过”“板上运行”“电流达标”分别需要不同的命令与观测。
2. 执行项目规定的检查，读取完整退出码与结果；此前的通过记录不能证明当前代码通过。
3. C 模块检查告警、边界/错误路径和适用的 sanitizer；固件检查交叉构建、链接 map、目标配置与镜像版本。
4. 硬件功能、实时性、DMA 完整性和功耗要用板上证据，模拟器或主机成功不能代替。
5. 检查 diff 与交付物，确保没有遗留临时日志、无关改动或意外生成物。
6. 没有板卡/SDK/探针时明确列为未验证，并给出可执行的验证步骤，不能编造结果。

交付变更、原因、实际验证命令和结果，以及仍缺少的证据。

## 来源与修改 / Provenance

- Upstream: [obra/superpowers — skills/verification-before-completion](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion)
- Pinned commit: `bb92a77741419a4ab5f06e711a283343f1ada0c3`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
