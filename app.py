import sqlite3
import os
from flask import Flask, request, render_template
from detector import is_suspicious, log_attack

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "users.db")

@app.route("/")
def home():
    return render_template("login.html",message="")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    ip_address = request.remote_addr
    
    suspicious_username, pattern1 = is_suspicious(username)
    suspicious_password, pattern2 = is_suspicious(password)
    
    if suspicious_username or suspicious_password:
        matched = pattern1 if pattern1 else pattern2
        log_attack(username, password, matched, ip_address)
        return render_template("login.html", message="Invalid input detected.")

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    
    # query ="SELECT * FROM users WHERE username= '" + username + "' AND password = '" + password + "'"
    query = "SELECT * FROM users WHERE username= ? AND password = ?"
    print("Query being run:", query)
    
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    connection.close()

    if result:
        message ="Login successful! Welcome, " + username + "."
    else:
        message ="Login failed. Invalid username or password."
        
    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)