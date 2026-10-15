---
name: arm-cortex-expert
description: "开发或调试 Cortex-M C 固件，涉及 NVIC、中断屏蔽、HardFault、MMIO、DMA 与 cache 时使用。"
---

# Arm Cortex-M C firmware

先固定核型号、芯片型号/修订、CMSIS/SDK、ABI、FPU 与 RTOS port；用厂商手册校验所有地址和位域。

## 中断与共享状态

- CMSIS NVIC 优先级数值通常越小越紧急；实现的位数、分组和 RTOS 可调用阈值由目标决定。
- 共享数据需要明确的原子操作、RTOS 原语或临界区。volatile 不能代替同步。
- 临界区保存并恢复原有 PRIMASK/BASEPRI；在 RTOS 中使用 port 提供的接口，避免与其屏蔽规则冲突。
- ISR 时限来自系统预算与测量；事件移交、缓冲满处理、外设确认必须完整。

## MMIO、DMA 与 cache

- 按寄存器属性区分普通读写、W1C、W0C、只读及 read-to-clear；W1C 只写需要清除的位。
- 不能给每次 MMIO 读写机械地加 DMB/DSB；按架构与外设规定选择 barrier。barrier 不等于 cache flush。
- DMA 内存必须对所用控制器可达，不能一律放 DTCM。STM32H7 DMA1/2 通常无法访问 DTCM，需核对具体总线矩阵。
- cacheable buffer 的对齐、独占 cache lines、TX clean、RX ownership 与完成后 invalidate 必须配套。

## 故障定位

保存构建版本、ELF、寄存器与停止原因，再读取与本核匹配的状态寄存器。
在有相关寄存器的核上，解码 HFSR/CFSR，并先检查有效位再解释 BFAR/MMFAR。
通过 EXC_RETURN、MSP/PSP 与浮点/安全扩展状态确定真正异常帧；不要假设栈损坏后仍可直接解引用。
用同一构建的 addr2line/反汇编核对 PC 和上下文；M0/M0+ 不具有 M3/M4 的完整故障寄存器。
输出可证实的故障链、最小改动与重现验证，不从单个异常地址猜定根因。

## 来源与修改 / Provenance

- Upstream: [sickn33/agentic-awesome-skills — plugins/agentic-awesome-skills-claude/skills/arm-cortex-expert](https://github.com/sickn33/agentic-awesome-skills/tree/a3072641b750a1fb2f6ce695a5f984ea3d4c3ec1/plugins/agentic-awesome-skills-claude/skills/arm-cortex-expert)
- Pinned commit: `a3072641b750a1fb2f6ce695a5f984ea3d4c3ec1`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
