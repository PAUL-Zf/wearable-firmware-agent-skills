---
name: c-aflpp
description: "Sets up and runs AFL++ for multi-core fuzzing of C/C++ projects built with afl-clang-fast or afl-gcc-fast. Covers instrumentation modes, parallel main and secondary campaigns, persistent mode, corpus minimization, and crash triage. Use when scaling fuzzing across cores, fuzzing a mature C/C++ codebase, reading the afl-fuzz status screen, or moving on after libFuzzer has plateaued."
---

## Workflow reference

Read [the scoped workflow](references/upstream-workflow.md) when this task matches. Its external tool dependencies must be available before executing tool-specific steps.

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

## Firmware scope

Use for host-testable C firmware modules and C++ harnesses around C APIs. MCU hardware, DMA,
ISR timing and power need separate on-target verification. Rust/Python fuzzing integrations are
outside this port. External fuzzers, compilers and runtimes are prerequisites, not bundled tools.


## 来源与修改 / Provenance

- Upstream: [trailofbits/skills — plugins/testing-handbook-skills/skills/aflpp](https://github.com/trailofbits/skills/tree/8e54050ae63c2f62224c35b1616efe71865b4777/plugins/testing-handbook-skills/skills/aflpp)
- Pinned commit: `8e54050ae63c2f62224c35b1616efe71865b4777`
- License: `CC-BY-SA-4.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
