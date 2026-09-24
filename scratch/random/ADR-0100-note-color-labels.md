# ADR-0100: Note Color Labels for v1

**Date:** 2026-09-24
**Status:** Accepted

## Context

Users want a lightweight way to visually mark notes. The Notes app is local and single-user. Free-form colors (hex, arbitrary strings) create inconsistent UX and weak validation. A small fixed palette is enough for v1.

## Decision

Adopt this note color-label policy for v1:

- A note may have an optional `color` field.
- Allowed values only: `red`, `blue`, `green`, `yellow` (lowercase).
- Omitting `color`, or setting it to `null`, means “no color.”
- Any other value (including uppercase variants like `Red`, hex codes, or empty string) must be rejected with HTTP **400** and a clear error.
- Color must persist across process restarts with the existing persistence approach.
- Listing and get-by-id responses must include `color` when set (or `null` when unset).

## Consequences

- **Positive:** Simple, predictable palette; easy validation and UI.
- **Positive:** Invalid input fails closed with 400.
- **Negative:** No custom colors or hex in v1.
- **Negative:** Callers must use the exact lowercase tokens.

## Alternatives Considered

1. **Free-form / hex colors** — Rejected for v1; too open-ended for a tiny local API.
2. **Case-insensitive aliases** — Rejected; keep a single canonical token set to avoid drift.
3. **Separate color service / second store** — Rejected; unnecessary for this app.