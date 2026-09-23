# ADR-0002: Pinned Notes Policy for v1

**Date:** 2026-09-23
**Status:** Accepted

## Context

Users need a way to keep a small set of important notes easy to find. The Notes app is a local, single-user service with SQLite persistence (ADR-0001). Unlimited pinning would weaken list usefulness; the product needs a clear, enforceable cap and stable ordering.

## Decision

Adopt the following pinned-notes policy for v1:

- A note may be pinned or unpinned.
- At most **3** notes may be pinned at the same time.
- Attempting to pin a 4th note must fail with HTTP **409** and a clear error message.
- When listing notes, pinned notes appear first, then unpinned notes.
- Pin state must persist across process restarts using the existing SQLite persistence approach (ADR-0001). Do not introduce a second store for pin state.

## Consequences

- **Positive:** List view keeps a small, predictable set of important notes at the top.
- **Positive:** Overflow is explicit (409), so clients can show a clear message instead of silent failure.
- **Positive:** Pin state survives restarts without new infrastructure.
- **Negative:** Users cannot pin more than three notes without unpinning another first.
- **Negative:** List/query logic must account for pin ordering and the cap check on every pin.

## Alternatives Considered

1. **Unlimited pins** — Rejected. Dilutes the value of “pinned” and makes the default list harder to scan.
2. **Soft cap (warn but allow)** — Rejected. Ambiguous product behavior; harder for clients to handle consistently.
3. **Separate pin store / second database** — Rejected. Violates the single persistence approach already chosen for v1; unnecessary complexity for a local app.