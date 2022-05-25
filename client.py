import socket
import time
from threading import Thread


def client(k:int):
    s = socket.socket()
    s.connect(('127.0.0.1', 4000))
    print('connected')
    n = 1
    while True:
        s.sendall(f'client_{k} - {str(n)}'.encode(encoding='UTF-8'))
        data = s.recv(1024)
        print(data)
        time.sleep(2)
        n += 1


amount = 2
clients = [Thread(target=client, args=(i,)).start() for i in range(amount)]
