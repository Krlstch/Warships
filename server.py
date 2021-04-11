import socket
import threading
import os

clients = set()


def handle_client(client_socket, client_address):
    """handles connection with client"""

    print(f"Client {client_address} connected")
    clients.add((client_socket, client_address))
    
    while True:
        # recieve 1 byte and sends it back, To be change later
        message = client_socket.recv(1)
        if message == b'':
            break
        print(f"Client {client_address} send: {message}")
        client_socket.send(message)

    print(f"Client {client_address} disconnected")
    clients.remove((client_socket, client_address))


def handle_accept(server_socket):
    """Accepts clients trying to connect to server and starts new thread to handle connection"""
    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True).start()


def main():
    ip_address = "127.0.0.1"
    port = 6666

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server_socket.bind((ip_address, port))
    server_socket.listen()

    threading.Thread(target=handle_accept, args=(server_socket,), daemon=True).start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

    for client_socket, client_address in clients:
        client_socket.shutdown(socket.SHUT_WR) 
        print(f"Client {client_address} disconnected")
    server_socket.close()
    os._exit(0)


if __name__ == "__main__":
    main()