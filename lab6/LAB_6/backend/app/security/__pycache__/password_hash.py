import hashlib
import os

def generate_salt():
    return os.urandom(16).hex()

def hash_password(password: str, salt: str):
    return hashlib.sha256((password + salt).encode()).hexdigest()
