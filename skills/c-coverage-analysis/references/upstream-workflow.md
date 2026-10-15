# Coverage analysis for host-tested C firmware

Adapted from Trail of Bits coverage-analysis; CC-BY-SA-4.0. See parent SOURCE.json and LICENSE.

## Establish an instrumented build

Use a separate host coverage build of the actual C module and its tests. GCC gcov and LLVM source-based coverage use different instrumentation; do not mix their outputs or stale objects. Pin compiler/tool versions.

For Clang, add `-fprofile-instr-generate -fcoverage-mapping -g -O0` to compilation and final linking. Run the test executable with a unique `LLVM_PROFILE_FILE`, merge the resulting profiles with `llvm-profdata merge`, then use the matching `llvm-cov report/show` with the exact executable. Preserve commands, exit codes and reports.

For GCC, use `--coverage` in compilation and linking, run the tests, then use the matching gcov/gcovr/lcov tooling against the associated object files. A failed or unexecuted test is not a valid coverage run.

## Fuzz coverage

Use a separate coverage binary/harness to replay the saved corpus with finite resource limits. Keep fuzz-discovery and coverage-report configurations identifiable. Verify target functions and error branches are reached, not merely the harness or stubs.

## Interpret the result

- Inspect branch and condition paths for length boundaries, error cleanup, allocation failure, state transitions, retries and reset.
- Exclude generated/platform code only with an explicit reason. Do not conceal uncovered target error paths by excluding them.
- Coverage indicates execution, not assertion quality or correctness. Strengthen behavior tests for important paths.
- Host coverage says nothing about real MMIO, DMA coherence, IRQ latency or power. Record separate on-target requirements.

Use [local harness guidance](../../c-harness-writing/SKILL.md) and [ASan](../../c-address-sanitizer/SKILL.md) for the associated memory-safety run.
