# Run Quality Gates

Use this skill when you want to run all quality gates locally before committing or opening a PR.

## Commands (run in this order)

```bash
# 1. Formatting check
ruff format --check .

# 2. Lint
ruff check .

# 3. Type check
mypy app.py --ignore-missing-imports

# 4. Tests with 80% diff coverage gate
pytest --cov=app --cov-fail-under=80

# 5. Dependency vulnerability audit
pip-audit --requirement requirements.txt
```

All gates must pass before merging. The 80% diff coverage threshold is a merge blocker per the project's testing standard.
