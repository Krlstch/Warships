import socket
import threading
import os

def handle_send(client_socket):
    while True:
        message = input()
        client_socket.send(bytes(message, encoding="UTF-8"))

def handle_recv(client_socket):
    while True:
        # recieve 1 byte and sends it back, To be change later
        message = str(client_socket.recv(1), encoding="UTF-8")
        print(f"Recieved: {message}")


def main():
    server_ip = "127.0.0.1"
    server_port = 6666
    
    client_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    client_socket.connect((server_ip, server_port))

    threading.Thread(target=handle_send, args=(client_socket,), daemon=True).start()
    threading.Thread(target=handle_recv, args=(client_socket,), daemon=True).start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

    client_socket.close()
    os._exit(0)

if __name__ == "__main__":
    main()