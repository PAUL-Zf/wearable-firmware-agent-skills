---
name: zephyr-native-sim
description: "Host-based simulation using the Zephyr native_sim board. Covers building for Linux/macOS/Windows, automated testing, host-side debugging (GDB, Valgrind), and host-target integration. Trigger when developing application logic without hardware or setting up CI/CD tests."
---

## Version contract

Pin the project Zephyr revision and board target. Verify Kconfig symbols, devicetree bindings and API signatures against that revision; templates do not prove compatibility. Device PM must coordinate active users and transfers.

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# Zephyr Native Simulation

Develop, test, and debug Zephyr applications with the speed and convenience of your host machine.

## Core Workflows

### 1. Simulation Basics
Understand when to use `native_sim` vs. QEMU and how to map host resources.
- **Reference**: **[simulation_basics.md](references/simulation_basics.md)**
- **Key Tools**: `west build -b native_sim`.

### 2. Host-Side Debugging
Use professional host tools to find the most elusive bugs.
- **Reference**: **[debugging.md](references/debugging.md)**
- **Key Tools**: `gdb`, `valgrind`, `gprof`, `pcap`.

### 3. Automated Testing (CI/CD)
The foundation of modern firmware development.
- **Reference**: See the `testing-debugging` skill (Phase 3) for comprehensive testing workflows.
- **Key Tools**: `twister -p native_sim`.

## Quick Start
```bash
# Build for host
west build -b native_sim samples/hello_world

# Run the app
./build/zephyr/zephyr.exe

# Debug with GDB
west debug
```

## Automation Tools
- **[native_log_scan.py](scripts/native_log_scan.py)**: Scan native simulation logs for common crash/failure signatures.

## Examples & Templates
- **[native_sim_ci_checklist.md](assets/native_sim_ci_checklist.md)**: Starter checklist for CI simulation coverage.

## Validation Checklist
- [ ] `west build -b native_sim` succeeds for at least one sample and one app target.
- [ ] Built binary runs on host and emits expected startup logs.
- [ ] Host debugger (GDB/Valgrind) can attach and surface expected symbols.
- [ ] Simulation test path is integrated into CI (for example Twister native_sim run).

## Resources

- **[References](references/)**:
  - `simulation_basics.md`: Architectural overview and usage patterns.
  - `debugging.md`: GDB, Valgrind, and profiling guide.
- **[Scripts](scripts/)**:
  - `native_log_scan.py`: Failure signature scanner for native_sim logs.
- **[Assets](assets/)**:
  - `native_sim_ci_checklist.md`: CI simulation review checklist.

## 来源与修改 / Provenance

- Upstream: [beriberikix/zephyr-agent-skills — skills/native-sim](https://github.com/beriberikix/zephyr-agent-skills/tree/ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce/skills/native-sim)
- Pinned commit: `ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce`
- License: `Apache-2.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
