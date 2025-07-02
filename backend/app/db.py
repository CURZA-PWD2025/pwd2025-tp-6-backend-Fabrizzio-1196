# filepath: c:\Users\Fabrizzio\Desktop\TP6_PWD\pwd2025-tp-6-backend-Fabrizzio-1196\app\db.py
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    print("Conectando a:", os.getenv("DB_HOST"), os.getenv("DB_NAME"))
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )