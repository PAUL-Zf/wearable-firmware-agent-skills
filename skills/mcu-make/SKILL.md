---
name: mcu-make
description: "GNU Make skill for C/C++ build systems. Use when writing or debugging Makefiles, understanding pattern rules and automatic dependency generation, managing CFLAGS/LDFLAGS, converting ad-hoc compile commands into maintainable Makefiles, or diagnosing incremental build issues. Activates on queries about Makefiles, make targets, pattern rules, phony targets, dependency tracking, recursive make, or make errors."
---

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# GNU Make

## Purpose

Guide agents through idiomatic Makefile patterns for C/C++ projects: phony targets, pattern rules, automatic dependency generation, and common build idioms.

## Triggers

- "How do I write a Makefile for my C project?"
- "My Makefile rebuilds everything every time"
- "How do I add dependency tracking to Make?"
- "What does `$@`, `$<`, `$^` mean?"
- "I'm getting 'make: Nothing to be done for all'"
- "How do I convert my shell compile script to a Makefile?"

## Workflow

### 1. Minimal correct Makefile for C

```makefile
CC      := gcc
CFLAGS  := -std=c11 -Wall -Wextra -g -O2
LDFLAGS :=
LDLIBS  :=

SRCS    := $(wildcard src/*.c)
OBJS    := $(SRCS:src/%.c=build/%.o)
TARGET  := build/prog

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^ $(LDLIBS)

build/%.o: src/%.c | build
	$(CC) $(CFLAGS) -c -o $@ $<

build:
	mkdir -p build

clean:
	rm -rf build
```

Automatic variables:

- `$@` — target name
- `$<` — first prerequisite
- `$^` — all prerequisites (deduplicated)
- `$*` — stem (the `%` part in a pattern rule)
- `$(@D)` — directory part of `$@`

### 2. Automatic dependency generation

Without this, changing a header doesn't trigger a rebuild of `.c` files that include it.

```makefile
CC      := gcc
CFLAGS  := -std=c11 -Wall -Wextra -g -O2
DEPFLAGS = -MMD -MP            # -MMD: generate .d file; -MP: phony targets for headers

SRCS    := $(wildcard src/*.c)
OBJS    := $(SRCS:src/%.c=build/%.o)
DEPS    := $(OBJS:.o=.d)
TARGET  := build/prog

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^ $(LDLIBS)

build/%.o: src/%.c | build
	$(CC) $(CFLAGS) $(DEPFLAGS) -MF $(@:.o=.d) -c -o $@ $<

-include $(DEPS)    # '-' ignores errors on first build (no .d files yet)

build:
	mkdir -p build

clean:
	rm -rf build
```

### 3. Pattern rules cheatsheet

```makefile
# Compile C
%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

# Compile C++
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Generate assembly
%.s: %.c
	$(CC) $(CFLAGS) -S -o $@ $<

# Run a tool on each file
build/%.processed: src/%.raw | build
	mytool $< > $@
```

### 4. Common Make patterns

#### Debug and release builds

```makefile
BUILD ?= release

ifeq ($(BUILD),debug)
  CFLAGS += -g -Og -DDEBUG
else
  CFLAGS += -O2 -DNDEBUG
endif
```

Usage: `make BUILD=debug`

#### Parallel builds

```bash
make -j$(nproc)     # use all CPUs
make -j4            # exactly 4 jobs
```

Add `-Otarget` (or `-O`) for ordered output: `make -j$(nproc) -O`

#### Verbose output

```makefile
# In Makefile: suppress with @
build/%.o: src/%.c | build
	@echo "  CC  $<"
	@$(CC) $(CFLAGS) -c -o $@ $<
```

Override silence: `make V=1` if you guard with `$(V)`:

```makefile
Q := $(if $(V),,@)
build/%.o: src/%.c
	$(Q)$(CC) $(CFLAGS) -c -o $@ $<
```

#### Installing

```makefile
PREFIX ?= /usr/local

install: $(TARGET)
	install -d $(DESTDIR)$(PREFIX)/bin
	install -m 0755 $(TARGET) $(DESTDIR)$(PREFIX)/bin/
```

### 5. Multi-directory projects

For medium projects, avoid recursive make (fragile, slow). Use a flat Makefile that includes sub-makefiles:

```makefile
# project/Makefile
include lib/module.mk
include src/app.mk
```

```makefile
# lib/module.mk
LIB_SRCS := $(wildcard lib/*.c)
LIB_OBJS := $(LIB_SRCS:lib/%.c=build/lib_%.o)
OBJS      += $(LIB_OBJS)

build/lib_%.o: lib/%.c
	$(CC) $(CFLAGS) -c -o $@ $<
```

### 6. Common errors

| Error | Cause | Fix |
|-------|-------|-----|
| `No rule to make target 'foo.o'` | Missing source or rule | Check source path and pattern rule |
| `Nothing to be done for 'all'` | Targets up to date | Touch a source file or run `make clean` |
| `Circular dependency dropped` | Target depends on itself | Check dependency chain |
| `missing separator` | Tab vs spaces | Recipes must use a tab, not spaces |
| `*** multiple target patterns` | Pattern rule syntax error | Check `%` placement |
| Rebuilds everything every time | Timestamps wrong, or PHONY missing | Check `date`; ensure `all` is `.PHONY` |
| Header change not detected | No dep tracking | Add `-MMD -MP` and `-include $(DEPS)` |

For a full variable and function reference, see [references/cheatsheet.md](references/cheatsheet.md).

## Related skills

- Use `skills/mcu-cmake` for CMake-based projects
- Use `skills/build-systems/ninja` for Ninja as a make backend
- Use `skills/mcu-gcc` for CFLAGS details

## 来源与修改 / Provenance

- Upstream: [mohitmishra786/low-level-dev-skills — skills/build-systems/make](https://github.com/mohitmishra786/low-level-dev-skills/tree/bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608/skills/build-systems/make)
- Pinned commit: `bdc58472fa9f309ed1b3f7d985a0d8e9bd8f4608`
- License: `MIT`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
