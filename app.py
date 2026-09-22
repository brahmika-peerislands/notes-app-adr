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


if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)
