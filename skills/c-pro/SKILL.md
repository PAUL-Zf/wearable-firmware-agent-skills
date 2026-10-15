---
name: c-pro
description: "实现或评审 C99/C11 模块，检查所有权、长度、整数溢出、错误路径和 MCU 资源预算时使用。"
---

# C for wearable firmware

1. 固定 C 标准、编译器、目标 ABI 与资源限制，先读项目风格与模块接口。
2. 为指针注明 owned/borrowed、可空性、有效长度、生命周期与释放方；避免释放后使用、重复释放和栈地址逃逸。
3. 检查指针算术、数组边界、整数转换及分配大小溢出；用 `len > capacity - used` 等经前置条件保护的形式避免加法溢出。
4. 解码字节流使用移位或 memcpy 并明确端序，不把任意 uint8_t 指针强转成宽整数指针读取。
5. 检查错误返回；给超时、截断、队列满和资源耗尽指定明确行为。
6. ISR 不调用通用堆分配、阻塞或非重入库；共享状态使用目标支持的同步机制。
7. 使用项目认可的告警与静态分析；在主机上对可移植 C 模块运行单元测试、ASan/UBSan，板上另验硬件时序。
8. 优化前量测；报告 map/size、栈和性能证据，不能仅凭源代码宣称精确资源占用。

交付清晰的 C 接口、实现、构建方式、边界/错误路径测试与实际验证记录。
本迁移移除了 POSIX/pthreads 专用部分；Valgrind/ASan 属于支持运行时的主机验证环境。

## 来源与修改 / Provenance

- Upstream: [sickn33/agentic-awesome-skills — plugins/agentic-awesome-skills-claude/skills/c-pro](https://github.com/sickn33/agentic-awesome-skills/tree/a3072641b750a1fb2f6ce695a5f984ea3d4c3ec1/plugins/agentic-awesome-skills-claude/skills/c-pro)
- Pinned commit: `a3072641b750a1fb2f6ce695a5f984ea3d4c3ec1`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `adapted-extract`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
