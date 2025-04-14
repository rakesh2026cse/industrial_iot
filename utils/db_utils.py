import sqlite3
from config import DB_PATH

def insert_sensor_data(temp, vib, pres, timestamp):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            vibration REAL,
            pressure REAL,
            timestamp TEXT
        )
    ''')
    c.execute('''
        INSERT INTO sensor_data (temperature, vibration, pressure, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (temp, vib, pres, timestamp))
    conn.commit()
    conn.close()

def fetch_recent_data(limit=100):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT ?", (limit,))
    data = c.fetchall()
    conn.close()
    return data[::-1]  

