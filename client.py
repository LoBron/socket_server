import socket
import time
import random
from threading import Thread


def client(k:int):

    s = socket.socket()
    s.connect(('127.0.0.1', 4000))
    print('connected')
    n = 1
    while True:
        s.sendall(f'client_{k} - {str(n)}'.encode(encoding='UTF-8'))
        data = s.recv(1024)
        print(data.decode(encoding='UTF-8'))
        time.sleep(random.randrange(0, 5))
        n += 1



amount = 2
clients = [Thread(target=client, args=(i,)).start() for i in range(amount)]
