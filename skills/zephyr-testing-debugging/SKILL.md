---
name: zephyr-testing-debugging
description: "Testing and debugging for Zephyr RTOS. Covers the Ztest framework for unit and integration tests, the Twister test runner for automated HIL/SIM validation, and advanced tracing/debugging techniques (SystemView, Thread Analyzer, Stack analysis). Trigger when writing unit tests, setting up CI/CD pipelines, or analyzing system performance and latency."
---

## Version contract

Pin the project Zephyr revision and board target. Verify Kconfig symbols, devicetree bindings and API signatures against that revision; templates do not prove compatibility. Device PM must coordinate active users and transfers.

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# Zephyr Testing & Debugging

Ensure code quality and system reliability using Zephyr's comprehensive testing framework and observability tools.

## Core Workflows

### 1. Ztest Framework
Write robust unit and integration tests for native simulation and real hardware.
- **Reference**: **[ztest_framework.md](references/ztest_framework.md)**
- **Key Tools**: `ZTEST_SUITE`, `ZTEST`, `zassert_equal`.

### 2. Twister Test Runner
Automate test execution across multiple platforms and generate professional reports.
- **Reference**: **[twister_testing.md](references/twister_testing.md)**
- **Key Tools**: `twister` script, `testcase.yaml`, hardware mapping.

### 3. Tracing & Debugging
Analyze system behavior, timing, and memory usage with advanced tracing tools.
- **Reference**: **[tracing_debugging.md](references/tracing_debugging.md)**
- **Key Tools**: `CONFIG_TRACING`, Segger SystemView, Thread Analyzer.

## Quick Start (Ztest)
```c
#include <zephyr/ztest.h>

ZTEST_SUITE(basic_test, NULL, NULL, NULL, NULL, NULL);

ZTEST(basic_test, test_pass) {
    zassert_true(true, "Boolean evaluation failed");
}
```

## Professional Patterns (Reliability)
- **Continuous Integration**: Integrate Twister reports (`twister.json`) into CI/CD pipelines for automated regression testing.
- **HIL Validation**: Use hardware maps to consistently run critical hardware tests on real devices during every release cycle.
- **Stack Safety**: Always enable `CONFIG_STACK_SENTINEL` and the Thread Analyzer during development to catch memory issues early.

## Automation Tools
- **[twister_smoke.py](scripts/twister_smoke.py)**: Run a small Twister suite and print result summary.

## Examples & Templates
- **[testcase.yaml.template](assets/testcase.yaml.template)**: Starter testcase metadata for Twister.

## Validation Checklist
- [ ] `twister` executes selected test suites with no unexpected failures.
- [ ] At least one `ZTEST` suite runs in simulation and reports pass/fail correctly.
- [ ] Tracing or thread-analyzer output is captured and reviewed for hotspots.
- [ ] CI artifacts include machine-readable reports (for example `twister.json`).

## Resources

- **[References](references/)**:
  - `ztest_framework.md`: Writing tests with expectations and suites.
  - `twister_testing.md`: Using the test runner and metadata.
  - `tracing_debugging.md`: Tracing, stack analysis, and debugging backends.
- **[Scripts](scripts/)**:
  - `twister_smoke.py`: Lightweight Twister runner with summary output.
- **[Assets](assets/)**:
  - `testcase.yaml.template`: Reusable testcase metadata template.

## 来源与修改 / Provenance

- Upstream: [beriberikix/zephyr-agent-skills — skills/testing-debugging](https://github.com/beriberikix/zephyr-agent-skills/tree/ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce/skills/testing-debugging)
- Pinned commit: `ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce`
- License: `Apache-2.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
