from app.db.db import get_db
from app.security.password_hash import generate_salt, hash_password

def create_table():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()


def add_user(username: str, password: str):
    conn = get_db()
    cursor = conn.cursor()

    salt = generate_salt()
    password_hash = hash_password(password, salt)

    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
            (username, password_hash, salt)
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def get_user(username: str):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    return user
