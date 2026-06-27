# secure_code.py
# FIXED VERSION - All vulnerabilities patched
# CodeAlpha Cybersecurity Internship - Task 3

import sqlite3
import hashlib
import os
import re
import secrets
import subprocess

# FIX 1: No hardcoded credentials
SECRET_KEY = os.environ.get("SECRET_KEY", secrets.token_hex(32))

# FIX 2: Parameterized query - No SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchone()

# FIX 3: Strong hashing SHA256 with salt
def hash_password(password):
    salt = secrets.token_hex(16)
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return f"{salt}:{hashed}"

def verify_password(password, stored_hash):
    salt, hashed = stored_hash.split(":")
    return hashlib.sha256(
        (password + salt).encode()).hexdigest() == hashed

# FIX 4: Input validation added
def login(username, password):
    if not username or not password:
        print("Invalid input!")
        return False
    if len(username) > 50 or len(password) > 100:
        print("Input too long!")
        return False
    user = get_user(username)
    if user and verify_password(password, user[2]):
        print("Login successful!")
        return True
    print("Login failed!")
    return False

# FIX 5: No command injection
def ping_host(host):
    pattern = r'^[a-zA-Z0-9\.\-]+$'
    if not re.match(pattern, host):
        print("Invalid host!")
        return
    subprocess.run(["ping", "-c", "1", host],
                   capture_output=True)
    print(f"Pinged {host} safely.")

# FIX 6: Never log passwords
def log_activity(username):
    with open("activity.log", "a") as f:
        f.write(f"Login attempt - User: {username}\n")

if __name__ == "__main__":
    print("=== Secure Code Demo ===")
    print("Secret Key: Hidden via environment variable")
    hashed = hash_password("admin123")
    print("Password Hash (SHA256+salt):", hashed)
    log_activity("admin")
    print("Log saved - Password NOT stored!")
    ping_host("google.com")
