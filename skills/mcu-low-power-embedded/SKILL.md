---
name: mcu-low-power-embedded
description: "调试 MCU Sleep/Stop/Standby、tickless idle、唤醒失败或穿戴设备待机电流异常时使用。"
---

# MCU low power

1. 确认具体器件与低功耗模式：CPU、SRAM、外设、时钟、RTC、GPIO 和调试域分别保留什么。
2. 记录唤醒源、电平/边沿、最坏唤醒时延与状态保存需求。Stop 和 Standby 不是可互换的名字。
3. 检查 PM 所有权、正在进行的总线/DMA、定时器、日志、看门狗、调试器及传感器电源域。
4. 使用 SDK/RTOS 已实现的无竞态入睡协议。不要在“检查无工作”和 WFI 之间留下丢失唤醒窗口。
5. 裸机临界区必须恢复原有屏蔽状态；不能用无条件 enable_irq 结束嵌套临界区。
6. 唤醒后按该 SDK 恢复系统时钟、tick 和所需外设；不能假设调用 SystemInit 就完成运行时恢复。
7. 清除或确认标志前核对手册，不能为了避免立即唤醒而盲目丢弃有效事件。

## STM32F4 纠错

上游曾把 `PWR_CR_PDDS = 1` 描述成 Stop；在 STM32F4 对应 HAL 中该设置选择 Standby。
请以具体芯片的参考手册和 HAL 实现为准，不移植跨系列 PWR 寄存器模板。
参考 [ST 官方 PWR HAL](https://github.com/STMicroelectronics/stm32f4xx-hal-driver/blob/master/Src/stm32f4xx_hal_pwr.c)。

## 测量与验收

用电流分析仪覆盖完整工作周期，记录采样、无线发送、显示、存储及睡眠的电流与占空比。
比较连接/断开调试器、启用/关闭日志、各传感器电源状态；同时验证恢复数据完整性与唤醒时限。
电池寿命估算需列明可用容量、稳压损耗、自放电与峰值负载；估算不能写成实测。

## 来源与修改 / Provenance

- Upstream: [mohitmishra786/low-level-dev-skills — skills/baremetal/low-power-embedded](https://github.com/mohitmishra786/low-level-dev-skills/tree/bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608/skills/baremetal/low-power-embedded)
- Pinned commit: `bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
