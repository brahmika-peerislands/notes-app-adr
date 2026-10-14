from pathlib import Path


def test_gitignore_ignores_venv_run_logs_and_notes_db() -> None:
    gitignore = Path(__file__).resolve().parents[1] / ".gitignore"
    lines = gitignore.read_text(encoding="utf-8").splitlines()
    assert ".venv/" in lines
    assert "run-aidlc_*.md" in lines
    assert "notes.db" in lines
