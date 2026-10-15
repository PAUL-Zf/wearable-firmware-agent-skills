# libFuzzer for firmware C modules

Adapted from the pinned Trail of Bits libfuzzer skill; this reference remains CC-BY-SA-4.0. See the parent SOURCE.json and LICENSE.

## Scope and dependencies

Run on a supported host using a Clang toolchain with libFuzzer and sanitizer runtimes. Link the actual C parser/state machine with a narrow harness; replace only hardware/time boundaries with deterministic stubs. Never fuzz MMIO on a host.

## Build and run

For C source, define `int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)` and include stdint.h/stddef.h. C++ harnesses need C linkage for both the fuzz entrypoint and the C target API.

Example commands, replacing filenames with real project files:

```sh
clang -std=c11 -O1 -g -fno-omit-frame-pointer -fsanitize=fuzzer,address,undefined parser.c fuzz_parser.c -o fuzz_parser
mkdir -p corpus artifacts
./fuzz_parser corpus -max_total_time=60 -timeout=2 -rss_limit_mb=512 -artifact_prefix=artifacts/
./fuzz_parser artifacts/crash-example
```

The final command is a placeholder for an actual artifact name. Record compiler version, command, exit status, stderr and input. A time-limited run without a crash is not proof of safety.

## Harness correctness

- Accept empty and malformed input according to the target API; do not filter out the error paths being tested.
- Validate bounds before multi-byte decoding. Use byte assembly or memcpy and explicit endianness, never a cast-and-dereference of arbitrary byte input.
- Reset state and release allocations each iteration. Bound operations, recursion, allocation size and output size.
- In C++, use vector.data() and size(), respecting the callee's empty-input contract; avoid indexing element zero of an empty vector.
- Assertions represent target invariants, not arbitrary assumptions about well-formed input.

## Sanitizers and resources

Use [the local sanitizer skill](../../c-address-sanitizer/SKILL.md) and [harness guidance](../../c-harness-writing/SKILL.md).
ASan's virtual address reservation varies by platform and is not RSS. Keep a measured finite RSS limit; do not disable RSS limits to accommodate shadow address space. `rss_limit_mb` is a libFuzzer option, not a generic ASAN_OPTIONS option.

Check available flags with the installed binary's `-help=1`; use its documented sanitizer options. If address-space policy prevents execution, report that limitation instead of changing unrelated runtime flags.

## Evaluation

Confirm coverage reaches target parsing/state transitions rather than only the harness. Minimize reproducible crash inputs and preserve both the original and minimized versions. Add the regression to ordinary host tests, then separately verify target ABI differences and hardware behavior.

Corpus/dictionary design can use [local dictionary guidance](../../c-fuzzing-dictionary/SKILL.md). Other fuzzing engines and standalone UBSan material are external prerequisites, not installed Skills.
