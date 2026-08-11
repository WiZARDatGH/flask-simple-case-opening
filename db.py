import sqlite3

DB_NAME = "database.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def conn_db():
    return sqlite3.connect(DB_NAME)

def init_db():
    db = get_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    db.commit()
    db.close()

def login(username, password):
    db = conn_db()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        db.close()

        if result is None:
            return False
        if result[0] == password:
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False


