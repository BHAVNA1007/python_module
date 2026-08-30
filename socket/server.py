'''import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))
server.listen(1)

print("Waiting for client...")

conn, addr = server.accept()

print("Connected:", addr)

message = conn.recv(1024)
print("Client says:", message.decode())

conn.sendall(b"Hello Client!")

conn.close()
server.close()'''


import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("192.168.1.45", 5000))

server.listen(1)

print("Waiting for client...")

conn, addr = server.accept()

print("Connected:", addr)

message = conn.recv(1024)

print("Client says:", message.decode())

conn.sendall(b"Hello Client!")

conn.close()
server.close()
server