---
name: resolve-official-device-documentation
description: "Recover or conclusively account for an unavailable vendor device-documentation URL by finding the current official source and returning a traceable retrieval result. Use when a CMSIS device, debug, trace, board, or Pack research workflow has a broken, moved, or inaccessible vendor document reference."
---

## Wearable / MCU adaptation

Use the project MCU, SDK/RTOS version, datasheet, errata and AGENTS.md as the platform contract.
Treat code samples as illustrative until built against that target. Check API returns, timeouts,
buffer bounds, interrupt priorities and ownership. volatile is not synchronization. Distinguish
host tests, simulator checks and on-target timing/power evidence; never invent unavailable results.

# Resolve Official Device Documentation

## Target & Persona

- **Role:** Technical Documentation Verification Engineer.
- **Objective:** Return one traceable official-source resolution without interpreting device behavior.

## Prerequisites & Context

- **Expected input:** A failed URL, document title or identifier when known, vendor, product or device family, and the required document type.
- **Dependencies:** Access to the web or supplied vendor documentation. No CMSIS toolchain, target, or hardware is required.
- **Portability:** Support any vendor and MCU family. Do not assume a vendor portal, account, product naming scheme, or document revision.

## Execution Steps (Strict Workflow)

1. **Analysis:** Record the exact failed URL and retrieval result. Extract the vendor, document identifier/title, product family, revision, and document type from the supplied context without guessing missing values.
2. **Processing:** Search official vendor pages or downloads using the known identifier, title, product family, and revision. Prefer the vendor's canonical document page or download. Check that a candidate is for the requested product and document type; retain relevant revision information.
3. **Validation:** Return `Resolved` only when the replacement is an official vendor source and its identity is sufficiently evidenced. Do not replace a missing official source with an unofficial mirror, distributor copy, forum post, or search-result snippet. If no source can be verified, return `Unavailable` with the attempted terms and precise reason.
4. **Formatting:** Return exactly one result row per requested document in the format consumed by knowledge records; do not create or update project artifacts.

## Guardrails & Constraints (Strict Rules)

- **No fabrication:** Do not invent a document identifier, revision, URL, retrieval result, or product applicability.
- **Portability:** Do not introduce vendor-, device-, toolchain-, debugger-, or target-specific assumptions.
- **Critical blockers:** Stop with `Unavailable` when the supplied identity is too ambiguous to distinguish a document or no official replacement can be verified.
- **Scope:** Resolve document provenance only. Do not infer hardware facts, edit a knowledge record, download files into the workspace, or choose PDSC content.
- **Tone and style:** Respond factually and directly. Omit conversational filler.

## Expected Output

Return this Markdown table in conversation:

```markdown
| Title | Failed URL | Retrieval issue and search terms | Replacement official URL | Requested workspace path |
|---|---|---|---|---|
```

Callers copy the returned row into their own document-download table and retain the failed URL even when a replacement is found. For an unavailable source, write `Unavailable` in `Replacement official URL` and state the precise reason in `Retrieval issue and search terms`.

## Validation Resources

Validate every `Resolved` row against the vendor's own domain, document portal, or authenticated vendor download flow, and compare its title/identifier, product applicability, and revision with the supplied context. Record the exact validation limitation for every `Unavailable` row.

## 来源与修改 / Provenance

- Upstream: [Open-CMSIS-Pack/cmsis-skills — generic-mcu-skills/skills/bring-up/resolve-official-device-documentation](https://github.com/Open-CMSIS-Pack/cmsis-skills/tree/25c2085a810ee531cc13df9d34ce2768cd84c421/generic-mcu-skills/skills/bring-up/resolve-official-device-documentation)
- Pinned commit: `25c2085a810ee531cc13df9d34ce2768cd84c421`
- License: `Apache-2.0`; see [LICENSE](LICENSE) and [source record](SOURCE.json).
- Migration: `selected-copy`; adapted for C/wearable MCU firmware. Changes are recorded in SOURCE.json.
