# vulnerable_code.py
# WARNING: Intentional security vulnerabilities for educational purpose
# CodeAlpha Cybersecurity Internship - Task 3

import sqlite3
import hashlib
import os

#VULNERABILITY 1:LHardcoded credentials
SECRET_KEY = "admin123"
DB_PASSWORD = "password123"

#VULNERABILITY 2:SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone

#VULNERABILITY 3:Weak Password hashing(MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

#VULNERABILITY 4:No Input bValidation
def login(username, password):
    user = get_user(username)
    hashed = hash_password(password)
    if user and user[2] == hashed:
        print("Login successful!")
        return True
    print("Login failed!")
    return False

#VULNERABILITY 5:Command Injection
def ping_host(host):
    os.system("ping -c 1 " + host)

#VULNERABILITY 6:Sensitive data in log
def log_activity(username, password):
    with open("activity.log", "a") as f:
        f.write(f"User: {username}, Password: {password}\n")

if __name__ == "__main__":
    print("=== Vulnerable Code Demo ===")
    print("Hardcoded Key:", SECRET_KEY)
    log_activity("admin", "admin123"
    print("Password Hash (MD5):", hash_password("admin123"))
    print("Log saved with plain text password!")
