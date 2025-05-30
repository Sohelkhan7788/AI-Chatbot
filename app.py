from flask import Flask, render_template, request
from chatbot import get_response
from database import log_message
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        response = get_response(user_input)
        log_message("user", user_input, response)

    # Get last 10 messages
    conn = sqlite3.connect("chat.db")
    cur = conn.cursor()
    cur.execute("SELECT message, response FROM logs ORDER BY id DESC LIMIT 10")
    history = cur.fetchall()
    conn.close()

    return render_template("chat.html", response=response, history=history)

if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)

