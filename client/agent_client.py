import socket
import json
import random
import time

SERVER = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

while True:

    data = {
        "node": "node1",
        "cpu": random.randint(0,100),
        "memory": random.randint(0,100),
        "disk": random.randint(0,100),
        "uptime": random.randint(1000,10000)
    }

    message = json.dumps(data)

    client.send((message+"\n").encode())

    print("Sent:", message)

    time.sleep(5)