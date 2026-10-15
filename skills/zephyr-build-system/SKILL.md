---
name: zephyr-build-system
description: "Build system management for Zephyr RTOS. Covers West workspace initialization, manifest management, Sysbuild multi-image builds, Kconfig symbols, and CMake integration. Trigger when setting up workspaces, configuring builds, or troubleshooting build-time errors."
---

## Version contract

Pin the project Zephyr revision and board target. Verify Kconfig symbols, devicetree bindings and API signatures against that revision; templates do not prove compatibility. Device PM must coordinate active users and transfers.

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# Zephyr Build System

Efficiently manage the complex build and configuration stack of Zephyr RTOS.

## Core Workflows

### 1. West Workspace & Manifests
Manage multi-repo projects and dependency allow-lists.
- **Reference**: **[west.md](references/west.md)**
- **Key Tools**: `west init`, `west update`, `west manifest --resolve`, `name-allowlist`.

### 2. Kconfig Configuration
Tune software features and hardware parameters.
- **Reference**: **[kconfig.md](references/kconfig.md)**
- **Key Tools**: `west build -t menuconfig`, symbol searching (`/`), help (`?`).

### 3. Sysbuild & Multi-Image
Configure complex projects like MCUboot + Application.
- **Reference**: **[cmake.md](references/cmake.md)**
- **Key Tools**: `west build --sysbuild`, `sysbuild.conf`.

### 4. CMake & Project Structure
Core build logic for applications and modules.
- **Reference**: **[cmake.md](references/cmake.md)**
- **Key Tools**: `CMakeLists.txt`, `zephyr_library()`, `target_sources()`.

## Quick Start (Workspace + Build)
```bash
west init -m <manifest-repo-url> zephyr-workspace
cd zephyr-workspace
west update
west build -b native_sim samples/hello_world
```

## Validation Checklist
- [ ] `west update` resolves all manifest projects without errors.
- [ ] `west build` succeeds for at least one known target board.
- [ ] Required Kconfig symbols are present in `build/zephyr/.config`.
- [ ] `scripts/find_modules.sh` reports module names that match the current manifest allow-list.

## Automation Tools

- **[find_modules.sh](scripts/find_modules.sh)**: Scan your `build/` directory to automatically identify which modules you should add to your manifest's `name-allowlist`.

## Examples & Templates

- **[west_manifest_template.yml](assets/west_manifest_template.yml)**: Minimal starter manifest for west workspaces.

## Resources

- **[References](references/)**:
  - `west.md`: West commands, manifests, and allow-lists.
  - `kconfig.md`: Project configuration and menuconfig usage.
  - `cmake.md`: Sysbuild and CMake API integration.
- **[Scripts](scripts/)**:
  - `find_modules.sh`: Automated allow-list discovery utility.
- **[Assets](assets/)**:
  - `west_manifest_template.yml`: Base west manifest template.

## 来源与修改 / Provenance

- Upstream: [beriberikix/zephyr-agent-skills — skills/build-system](https://github.com/beriberikix/zephyr-agent-skills/tree/ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce/skills/build-system)
- Pinned commit: `ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce`
- License: `Apache-2.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
