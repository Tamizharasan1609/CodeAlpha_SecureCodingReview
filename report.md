# Secure Coding Review Report
## CodeAlpha Cybersecurity Internship — Task 3
### Reviewed by: Tamizharasan

---

## Summary
A Python login application was audited for security vulnerabilities.
6 critical vulnerabilities were found and fixed.

---

## Vulnerabilities Found & Fixed

### 1. Hardcoded Credentials [CRITICAL]
- File: vulnerable_code.py (Line 10-11)
- Issue: SECRET_KEY and DB_PASSWORD hardcoded in source code
- Risk: Anyone with code access gets credentials
- Fix: Use environment variables with os.environ.get()

### 2. SQL Injection [CRITICAL]
- File: vulnerable_code.py (Line 17)
- Issue: User input directly concatenated in SQL query
- Risk: Attacker can bypass login or dump entire database
- Fix: Use parameterized queries with ? placeholder

### 3. Weak Password Hashing [HIGH]
- File: vulnerable_code.py (Line 22)
- Issue: MD5 used for password hashing
- Risk: MD5 is broken, passwords can be cracked easily
- Fix: Use SHA-256 with random salt

### 4. No Input Validation [HIGH]
- File: vulnerable_code.py (Line 25)
- Issue: No validation on username/password input
- Risk: Injection attacks possible
- Fix: Added length checks and format validation

### 5. Command Injection [CRITICAL]
- File: vulnerable_code.py (Line 32)
- Issue: User input directly passed to os.system()
- Risk: Attacker can run any system command
- Fix: Use subprocess with list, validate with regex

### 6. Sensitive Data in Logs [HIGH]
- File: vulnerable_code.py (Line 37)
- Issue: Password logged in plain text
- Risk: Log files expose user passwords
- Fix: Log only username, never passwords

---

## Risk Summary

| Vulnerability        | Severity | Status   |
|----------------------|----------|----------|
| Hardcoded Credentials| CRITICAL | Fixed    |
| SQL Injection        | CRITICAL | Fixed    |
| Weak Password Hash   | HIGH     | Fixed    |
| No Input Validation  | HIGH     | Fixed    |
| Command Injection    | CRITICAL | Fixed    |
| Sensitive Data Logs  | HIGH     | Fixed    |

---

## Tools Used
- Manual Code Review
- Static Analysis
- Python Security Best Practices (OWASP)

---

## Conclusion
All 6 vulnerabilities were identified and fixed.
Secure version follows OWASP secure coding guidelines.
