import sqlite3

def log_message(user, message, response):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS logs (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user TEXT,
                 message TEXT,
                 response TEXT
             )""")
    c.execute("INSERT INTO logs (user, message, response) VALUES (?, ?, ?)",
              (user, message, response))
    conn.commit()
    conn.close()
