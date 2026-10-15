---
name: libre-sensor-patterns
description: "处理MCU 传感器驱动、校准、滤波或数据异常时使用；仅适用于 MCU C 固件。"
---

# MCU 传感器驱动、校准、滤波或数据异常

从上游模式库提取 MCU/C 相关设计步骤，移除了未经目标验证的固定地址、寄存器与完整镜像示意代码。

1. 确认 WHO_AM_I、启动时序、总线协议、ODR/量程、FIFO、IRQ 极性和时间戳来源。
2. 寄存器地址读写位和 auto-increment 不是所有 SPI 传感器通用；依据具体手册实现。
3. 校准表要求输入严格递增、有效范围和版本/CRC；对插值零分母与超界作明确处理。
4. NTC 换算处理 ADC=0、满量程、断路和短路；Beta 参数、分压方向及单位必须来自电路与器件。
5. 滤波明确窗口、初始填充、延迟与采样率；保存原始数据以区分物理异常和软件处理错误。

先读取项目约束与目标 SDK；输出设计契约、最小实现计划、错误处理与可复现验证。区分主机测试、模拟器结果和真实板上证据。

## 来源与修改 / Provenance

- Upstream: [Ormus-Solutions/LibreEmbed-Claude-Code — plugins/sensor-integration/skills/sensor-patterns](https://github.com/Ormus-Solutions/LibreEmbed-Claude-Code/tree/b3840586de7181db1cfb04214f8fbdb49a63ab09/plugins/sensor-integration/skills/sensor-patterns)
- Pinned commit: `b3840586de7181db1cfb04214f8fbdb49a63ab09`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
