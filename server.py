import socket
import select
import time
import random

def coroutine(func):
    generator = func
    next(generator)
    return generator


def handle(client, address):
    try:
        data = client.recv(1024)
        if not data:
            connections.remove(client)
            client.close()
            print("return")
            return
        print(data)
        print(address, 'connect к базе')
        yield time.sleep(random.randrange(0, 3))
        print(address, 'Подключился к базе')
        yield time.sleep(random.randrange(0, 3))
        print(address, 'Данные из базы получены')
        client.sendall(data)
        print(address, 'Данные отправлены')
    except Exception as ex:
        connections.remove(client)
        client.close()
        print(ex)

def test_handle(client):
    try:
        data = client.recv(1024).decode(encoding='UTF-8')
        if not data:
            connections.remove(client)
            client.close()
            print("return")
            return
        print(data)
        client.sendall('Да прибудет с тобой сила!'.encode(encoding="UTF-8"))
    except Exception as ex:
        connections.remove(client)
        client.close()
        print(ex)

def HTTP_handle(request):
    """Упрощённая модель контроллера"""
    ...
    db = yield connect() # неблокирующее соединение с базой
    ...
    row = yield db.query() #какие-то данные из бвзы
    ...
    db.close()
    return render(row)

s = socket.socket()
s.setblocking(False)
s.bind(('127.0.0.1', 4000))
s.listen(5)
connections = {s: ''}
workers = {}
print('жду подключений')
try:
    while True:
        read_sockets, _, _ = select.select(connections, [], [])
        print('получен список готовых сокетов')
        for r_socket in read_sockets:
            if r_socket == s:
                client, address = s.accept()
                print('connected', address)
                connections[client] = address
            else:
                if r_socket not in workers:
                    workers[r_socket] = handle(client=r_socket, address=connections[r_socket][0])
                    next(workers[r_socket])
                else:
                    next(workers[r_socket])
finally:
    s.close()

