from app.db.users_db import add_user, get_user
from app.security.password_hash import hash_password

def register_user(username: str, password: str):
    return add_user(username, password)

def login_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False

    check_hash = hash_password(password, user["salt"])
    return check_hash == user["password_hash"]
