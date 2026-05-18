import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
        
    )
     
""")

cursor.execute("INSERT INTO users (username,password) VALUES ('admin', 'supersecret')")
cursor.execute("INSERT INTO users (username,password) VALUES ('shreya', 'mypassword123')")
cursor.execute("INSERT INTO users (username,password) VALUES ('alice', 'alice2024')")

connection.commit()
connection.close()

print("Database created successfully with 3 users.")