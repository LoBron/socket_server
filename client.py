import socket
import time

s = socket.socket()
s.connect(('127.0.0.1', 4000))
print('connected')
n = 1
while True:
    s.sendall(str(n).encode(encoding='UTF-8'))
    data = s.recv(1024)
    print(data)
    time.sleep(2)
    n += 1