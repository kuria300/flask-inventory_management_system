import os
import json

DB_FILE="products.json"

def load_db():
    """"Deserializer (convert from json to python dict)"""

    if not os.path.exists(DB_FILE):
        return []

    with open(DB_FILE, 'r') as f:
        try:
            data=json.load(f)
            return data
        except json.JSONDecodeError:
            return []

def save_db(products):
    """"serializer (convert from python dict to json)"""
    with open(DB_FILE, 'w') as f:
        json.dump(products, f, indent=4)


    
