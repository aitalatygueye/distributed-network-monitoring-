import sqlite3

DB = "monitoring.db"

def insert_metric(data):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO metrics(node,cpu,memory,disk,uptime) VALUES (?,?,?,?,?)",
        (
            data["node"],
            data["cpu"],
            data["memory"],
            data["disk"],
            data["uptime"]
        )
    )

    conn.commit()
    conn.close()