---
name: libre-power-mgmt-patterns
description: "处理穿戴设备休眠、RTC 唤醒、tickless idle 或功耗预算时使用；仅适用于 MCU C 固件。"
---

# 穿戴设备休眠、RTC 唤醒、tickless idle 或功耗预算

从上游模式库提取 MCU/C 相关设计步骤，移除了未经目标验证的固定地址、寄存器与完整镜像示意代码。

1. 记录各模式的电流、持续时间、峰值与唤醒成本，并按占空比估算平均值。
2. 核对传感器、无线、显示、Flash、GPIO 和调试域的状态；不能只优化 CPU。
3. 优先使用项目 PM/tickless 集成；入睡与事件检查必须无丢失唤醒窗口。
4. RTC/LPTIM 的保留时钟、精度和补偿依具体器件核对，不能笼统关闭全部 GPIO/外设时钟。
5. 测量真实波形并覆盖周期工作和唤醒；日志、调试器、量程与采样率写进记录。

先读取项目约束与目标 SDK；输出设计契约、最小实现计划、错误处理与可复现验证。区分主机测试、模拟器结果和真实板上证据。

## 来源与修改 / Provenance

- Upstream: [Ormus-Solutions/LibreEmbed-Claude-Code — plugins/power-management/skills/power-mgmt-patterns](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/tree/b3840586de7181db1cfb04214f8fbdb49a63ab09/plugins/power-management/skills/power-mgmt-patterns)
- Pinned commit: `b3840586de7181db1cfb04214f8fbdb49a63ab09`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
