import sqlite3

connection = sqlite3.connect("monitoring.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS metrics (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 node TEXT,
 cpu INTEGER,
 memory INTEGER,
 disk INTEGER,
 uptime INTEGER,
 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 node TEXT,
 message TEXT,
 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()
connection.close()

print("Database created successfully")