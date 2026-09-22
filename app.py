import sqlite3
import os

from flask import Flask, g, jsonify, request

DATABASE = os.environ.get("DATABASE", "notes.db")

app = Flask(__name__)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(app.config.get("DATABASE", DATABASE))
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.execute(
        "CREATE TABLE IF NOT EXISTS notes "
        "(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, body TEXT NOT NULL)"
    )
    db.commit()


app.teardown_appcontext(close_db)


@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json(silent=True)
    if not data or not str(data.get("title", "")).strip():
        return jsonify({"error": "title is required and must not be empty"}), 400
    db = get_db()
    cursor = db.execute(
        "INSERT INTO notes (title, body) VALUES (?, ?)",
        (data["title"], data.get("body", "")),
    )
    db.commit()
    return jsonify({"id": cursor.lastrowid, "title": data["title"], "body": data.get("body", "")}), 201


@app.route("/notes", methods=["GET"])
def list_notes():
    db = get_db()
    rows = db.execute("SELECT id, title, body FROM notes ORDER BY id ASC").fetchall()
    return jsonify([{"id": r["id"], "title": r["title"], "body": r["body"]} for r in rows]), 200


@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    db = get_db()
    row = db.execute(
        "SELECT id, title, body FROM notes WHERE id = ?", (note_id,)
    ).fetchone()
    if row is None:
        return jsonify({"error": "Note not found"}), 404
    return jsonify({"id": row["id"], "title": row["title"], "body": row["body"]}), 200


if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)
