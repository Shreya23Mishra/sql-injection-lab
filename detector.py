import re
import logging
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "attack_log.txt")

logging.basicConfig(
    
    filename=LOG_PATH, 
    level=logging.WARNING, 
    format="%(message)s"
    
)

SUSPICIOUS_PATTERNS = [
    
    r"'",
    r"--",
    r"\bOR\b",
    r"\bAND\b",
    r"\bUNION\b",
    r"\bSELECT\b",
    r"\bINSERT\b",
    r"\bDROP\b",
    r"1=1",
    r"1 = 1",

]

def is_suspicious(user_input):
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            return True, pattern
    return False, None

def log_attack(username_input, password_input, matched_pattern, ip_address):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"""
    --- ATTACK DETECTED ---
    Time            : {timestamp} 
    IP Address      : {ip_address} 
    Username        : {username_input} 
    Password        : {password_input}
    Pattern         : {matched_pattern}
    -----------------------"""
    
    logging.warning(log_entry)
    print(log_entry)
    