import socket 

HOST = '192.168.1.145' # server ip or hostname
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")

try:
    s.bind((HOST, PORT))
except socket.error:
    print("Bind failed")

s.listen(1)
print("Socket awaiting messages")
(conn, addr) = s.accept()
print("Connected")

while True:
    data = conn.recv(1024).decode()
    print("I sent  message in response to: " + data)

    # process message
    if data == 'Hello':
        reply = 'Hi, back!'
    elif data == 'This is important':
        reply = 'OK, fuck shit bum'

    elif data == 'quit':
        conn.send('Terminating')
        break
    else:
        reply = 'Unknown command'

    conn.send(reply.encode())
conn.close()
