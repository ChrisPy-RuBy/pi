import socket

HOST = '192.168.1.145'
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    command = input("Enter command: ")
    s.send(command.encode())
    reply = s.recv(1024)
    if reply == "Terminate":
        break
    print(reply.decode())

