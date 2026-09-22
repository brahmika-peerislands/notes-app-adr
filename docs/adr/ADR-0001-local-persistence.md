# ADR-0001: Local Persistence for Notes

**Date:** 2026-09-22
**Status:** Accepted

## Context

The Notes API is a single-user, locally-deployed HTTP service. Data must survive process restarts. The operator constraint prohibits cloud services and mandates a single-module, single-package Python application with no heavyweight dependencies.

## Decision

Use SQLite for note persistence in v1.

SQLite is bundled with Python's standard library (`sqlite3` module) and requires no additional installation. A single `.db` file satisfies all persistence requirements for the local, single-user deployment model. No separate database server is required.

## Consequences

- **Positive:** Zero external dependencies for persistence; simplest possible deployment (single file).
- **Positive:** Python's `sqlite3` module provides full SQL support including parameterised queries.
- **Negative:** Not suitable for concurrent multi-writer scenarios, but this is not a requirement for v1.
- **Negative:** Migrating to a different store in future versions would require changes to the persistence layer.

## Alternatives Considered

- **PostgreSQL:** Rejected — see scratch/random/ADR-0099-use-postgres.md. Overkill for a local single-user application; requires a running database server.
- **JSON file store:** Considered but rejected — SQLite provides ACID guarantees, structured queries, and better atomicity than a flat JSON file.
