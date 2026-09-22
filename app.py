import sqlite3
import os

from flask import Flask, g, jsonify, request

DATABASE = os.environ.get("DATABASE", "notes.db")

app = Flask(__name__)


def get_db():
    pass


def close_db(e=None):
    pass


def init_db():
    pass


app.teardown_appcontext(close_db)


if __name__ == "__main__":
    app.run(debug=True)
