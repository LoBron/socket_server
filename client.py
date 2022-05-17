import socket
import time

s = socket.socket()
s.connect(('127.0.0.1', 4000))
print('connected')
time.sleep(5)
s.sendall(b"hello")
data = s.recv(1024)
print(data)
s.close()