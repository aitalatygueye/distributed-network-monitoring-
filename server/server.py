import socket
import threading
from server.client_handler import handle_client

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print("Monitoring Server started on port",PORT)

while True:
 
    print("Server is running and waiting for clients...")

    conn, addr = server.accept()

    print("Client connected:", addr)

    thread = threading.Thread(target=handle_client,args=(conn,))
    thread.start()