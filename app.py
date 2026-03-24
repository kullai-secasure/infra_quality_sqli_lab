from flask import Flask, request, jsonify
import sqlite3
from utils import helper_function

app = Flask(__name__)

DB = "users.db"

def get_db():
    return sqlite3.connect(DB)

@app.route("/user")
def get_user():
    username = request.args.get("username")

    conn = get_db()
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()

    return jsonify(result)

@app.route("/")
def home():
    return "Infra + Quality + SQLi Lab"

if __name__ == "__main__":
    app.run(debug=True)
