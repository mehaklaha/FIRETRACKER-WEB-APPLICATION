import sqlite3

conn = sqlite3.connect("fires.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fire_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL,
    longitude REAL,
    risk REAL
)
""")
conn.commit()

def insert_fire_data(lat, lon, risk):
    cursor.execute(
        "INSERT INTO fire_data (latitude, longitude, risk) VALUES (?, ?, ?)",
        (lat, lon, risk)
    )
    conn.commit()

def fetch_fire_data():
    cursor.execute("SELECT latitude, longitude, risk FROM fire_data")
    return cursor.fetchall()
