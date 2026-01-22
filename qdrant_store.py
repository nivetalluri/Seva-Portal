# vectorstore/qdrant_store.py
import json
import os

DATA_FILE = "vectorstore/citizens.json"

# Initialize storage if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def save_citizen_profile(profile: dict):
    """Save a citizen profile (name, email, phone, password)"""
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    
    # Avoid duplicate email/phone
    for p in data:
        if p["email"] == profile["email"] or p["phone"] == profile["phone"]:
            raise ValueError("User already exists")
    
    data.append(profile)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_citizen_by_login(identifier: str, password: str):
    """Find citizen by email/phone and password"""
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    
    for p in data:
        if (p["email"] == identifier or p["phone"] == identifier) and p["password"] == password:
            return p
    return None
