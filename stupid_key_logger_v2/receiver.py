import socket 
import threading

port = 8181
server = socket.gethostbyname(socket.gethostname())
address = (server, port)
encrypt_format = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)

def handle_client(client, addr):
    while True:
        try:
            print(client.recv(4096).decode(encrypt_format))
        except:
            print(f"{addr} has been disconnected.")
            break
    client.close()
        

def start():
    server.listen()
    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

start()
