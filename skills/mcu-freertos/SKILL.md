---
name: mcu-freertos
description: "设计 FreeRTOS 任务、队列、互斥、ISR 通知、栈与堆预算，或定位穿戴固件调度与并发问题时使用。"
---

# FreeRTOS firmware workflow

1. 读取实际 FreeRTOSConfig.h、内核与厂商 port 版本。核对优先级范围、tick 频率、静态分配、断言和中断屏蔽配置。
2. 根据采样周期、响应期限及阻塞关系分配任务；避免固定认为某一外设一定最高优先级。
3. 创建任务、队列、互斥量并检查失败；动态内存需预算，优先使用已有项目的分配策略。
4. 队列传值；传指针时记录生产者到消费者的所有权、释放时机和超时清理。
5. ISR 使用对应 FromISR API，并满足该 port 的系统调用中断优先级限制与 yield 约定；不能获取 mutex。
6. Task notification/二值信号量可合并事件，连续字节流需队列、stream buffer 或有界环形缓冲。
7. 互斥量的优先级继承不能消除所有反转；缩短临界区并分析完整等待链与锁顺序。
8. 周期任务采用绝对周期接口并检测超期；tickless idle 交由正确的 port/PM 集成实现。

## 栈、错误与调试

上游 FreeRTOS 常以 StackType_t 元素计任务栈深度；厂商 fork 可能以字节计，必须查项目接口。
打开适用的 configASSERT、malloc-failed 与 stack-overflow hook；水位观测要覆盖最坏路径，不能套用固定 20 words 阈值。
调试器的 RTOS awareness 依赖 GDB server 与符号配置；不要假设存在一个通用 FreeRTOS.cfg。
不在被调试目标上随意 `call vTaskList`，因为目标函数执行可能改变状态、阻塞或再次故障。

## API 纠错

任务索引通知与 stream buffer 不是统一从 v11 才出现；按头文件检查。
`xStreamBufferSend` 是任务上下文接口，中断应使用 `xStreamBufferSendFromISR`。
不要使用上游示例中的 `xTaskCreateSecure` 作为通用 FreeRTOS API；TrustZone/MPU 必须按实际 port 的示例接入。
[配置项参考](references/freertos-config.md)为说明材料，具体值需匹配工程。

## 来源与修改 / Provenance

- Upstream: [mohitmishra786/low-level-dev-skills — skills/embedded/freertos](https://github.com/mohitmishra786/low-level-dev-skills/tree/bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608/skills/embedded/freertos)
- Pinned commit: `bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
