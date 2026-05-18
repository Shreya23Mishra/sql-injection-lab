# SQL Injection Lab - Attack & Defense

A Python project that demonstrates how SQL injection attacks work,
and builds a real defense system to detect and block them.

---

## What This Project Does

This project has three layers:

1. **Vulnerable app** — A Flask login system intentionally built
   with an SQL injection vulnerability, exactly like real-world
   insecure applications.

2. **Attack scripts** — Three different SQL injection attacks that
   bypass authentication without knowing any valid credentials.

3. **Defense system** — Parameterized queries that neutralize the
   injection, plus a pattern-detection engine that logs every
   attack attempt with timestamps and IP addresses.

---

## The Vulnerability Demonstrated 

The vulnerable query glues user input directly into SQL:

```python
query = "SELECT * FROM users WHERE username= '"
        + username + "' AND password = '" + password + "'"
```

An attacker can type this into the username field:

' OR '1'='1' --

Which transforms the query into:

```sql
SELECT * FROM users WHERE username= '' OR '1'='1' --' AND password = ''
```

The `--` comments out the password check entirely.
`'1'='1'` is always true — so every user row is returned,
and the attacker is logged in without any valid credentials.

---

## The Defense

Parameterized queries separate SQL structure from user data:

```python
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```

The `?` placeholders are filled by SQLite internally —
user input can never become part of the query structure.

Additionally, a pattern detector screens every input before
it reaches the database, flagging and logging suspicious patterns
like quotes, `--`, `OR`, `UNION`, and `DROP`.

---

## Attack Log Sample

Every detected attack is recorded in `attack_log.txt`:
--- ATTACK DETECTED ---
Time         : 2026-05-18 06:35:56
IP Address   : 127.0.0.1
Username     : ' OR '1'='1' --
Password     :
Pattern      : '

---

## Technologies Used

- Python 3.12
- Flask — web framework
- SQLite — database
- Python `re` module — pattern detection
- Python `logging` module — attack logging

---

## What I Learned

- How SQL injection vulnerabilities are created and exploited
- Three real attack techniques: login bypass, account targeting,
  username enumeration
- How parameterized queries prevent injection at the database level
- How to build an input validation and attack detection layer
- Flask routing, SQLite integration, and Python logging

---

## Project Structure

'''
sql-injection-lab/
├── app.py           Flask backend with defense layer
├── database.py      Database setup and seeding
├── detector.py      Attack detection and logging engine
├── attack_log.txt   Live attack log (auto-generated)
├── users.db         SQLite database
└── templates/
└── login.html       Login page frontend

'''
---

## Future Improvements

- Add XSS (Cross-Site Scripting) detection
- Build a dashboard to visualize attack frequency
- Add rate limiting to block repeated attempts
- Extend to detect UNION-based and blind injection attacks




























































































