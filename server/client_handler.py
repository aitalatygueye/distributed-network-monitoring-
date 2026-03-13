import json
from database.database import insert_metric
from server.alert_manager import check_alerts
from server.node_monitor import update_node

def handle_client(conn):

    buffer = ""

    while True:

        data = conn.recv(1024).decode()

        if not data:
            break

        buffer += data

        if "\n" in buffer:

            message, buffer = buffer.split("\n",1)

            metrics = json.loads(message)

            insert_metric(metrics)

            update_node(metrics["node"],metrics)

            alerts = check_alerts(metrics)

            for alert in alerts:
                print("ALERT:",alert)