# ADR-0099: Use PostgreSQL for Persistence

**Date:** 2026-09-22
**Status:** Rejected

## Context

Evaluated PostgreSQL as a persistence layer for the Notes API.

## Decision

Do NOT use PostgreSQL.

## Rationale

PostgreSQL requires a running database server separate from the application process. For a local, single-user notes application this introduces unnecessary operational complexity (install, configure, start, authenticate). The current deployment model does not benefit from the concurrency or scalability features PostgreSQL provides.

The accepted decision is recorded in docs/adr/ADR-0001-local-persistence.md.

## Consequences

This ADR is intentionally left as a rejected alternative to document that PostgreSQL was considered and explicitly ruled out for v1.
