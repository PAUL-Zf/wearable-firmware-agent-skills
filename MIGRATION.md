# 迁移与技术纠错

迁移日期：2026-10-15。来源固定到提交；逐项见 SOURCE.json，全量见 sources.lock.json。

## 迁移方式

- `selected-copy`：保留相关叶子 Skill 与其必要 references/scripts/assets，调整名称、平台边界和导航。超长工作流放入按需读取的 reference。
- `adapted-extract`：从上游提取 C/MCU 相关设计步骤，重写成可移植指南；不保留无关平台或未经验证的寄存器/镜像代码。与上游逐字一致的副本应从固定来源获取。
- 每个目录均保留 LICENSE，适用时保留 NOTICE，安装时不得删除。摘编并未改变上游许可证。
- Skill 只保留 name/description frontmatter 以提高可移植性；原工具专有元数据不作为 Codeagent 功能承诺。CMSIS 工具依赖在入口说明。

## 已处理的具体问题

| 上游或范围 | 处理 |
|---|---|
| embedded-systems ISR 单字节标志示例 | 移除可能丢失连续数据、无条件开中断的模板，明确缓冲与原屏蔽状态恢复 |
| low-level low-power | 修正 STM32F4 PDDS 选择 Standby 的说明，移除错误 Stop 模板和通用 SystemInit 恢复假设 |
| low-level FreeRTOS | 移除通用 xTaskCreateSecure 假设、错误 API 版本归属，明确 stream buffer ISR 接口与栈单位差异 |
| ARM Cortex expert / DMA | 移除 DTCM 一律适合 DMA、每次 MMIO 必须固定 barrier 的泛化，增加内存可达域与 cache ownership |
| embedded-isr-design | 不套用固定微秒预算；区分 FreeRTOS、CMSIS-RTOS2 和 Zephyr ISR 契约；移除不可靠清标志模板 |
| C ASan / libFuzzer / coverage / harness | 移除 Rust 专用流程，修正虚拟地址与 RSS 混淆；不关闭 RSS 上限；移除任意字节转宽整数解引用与空 vector 索引示例 |
| Zephyr BLE 参数 | 移除 interval=2s、latency=5、timeout=10s 的无效组合；写明严格超时约束、单位和请求/实际参数差异 |
| Zephyr 连续采样发送 | 改为容量、空闲和最大批次年龄共同触发，避免不断重排空闲定时器导致永不发送 |
| Zephyr PM | 移除未定义 DTS state 与不可靠 pm_state_set 签名；区分 SoC hook、system PM 和 runtime PM |
| Zephyr sensor | 移除混淆 sensor_read/decode context 的伪代码，按锁定版本选择 fetch/get 或 RTIO/read/decode |
| OpenOCD | 将两套 probe/target 配置拆为互斥示例，去掉固定速度/仅单目标 SWD 的泛化 |
| LibreEmbed 模式库 | 保留 C/MCU 的设计契约，移除跨芯片固定寄存器/镜像代码；明确软件 A/B slots 与硬件 Flash dual-bank 不同 |
| 功耗/BLE 辅助脚本 | 校验有限数值、有效范围及参数组合；功耗模型要求互斥状态占空比完整 |

官方核对入口（实际项目应选择对应版本）：

- [ST STM32F4 PWR HAL](https://github.com/STMicroelectronics/stm32f4xx-hal-driver/blob/master/Src/stm32f4xx_hal_pwr.c)
- [Clang ASan](https://clang.llvm.org/docs/AddressSanitizer.html)、[libFuzzer](https://llvm.org/docs/LibFuzzer.html)
- [Zephyr connection API](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html)
- [Zephyr PM hooks](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__hooks.html)
- [Zephyr sensor Read and Decode](https://docs.zephyrproject.org/latest/hardware/peripherals/sensor/read_and_decode.html)

## 边界

这批内容是经筛选和纠错的工程指导，未取得对特定公司 SDK、芯片型号或穿戴板卡的兼容性认证。模板仍需交叉构建、按手册核对，并在目标板上验证时序、功耗和恢复行为。没有将 Star 数等同于技术正确性。
