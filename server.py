import socket
import select

def handle(client):
    try:
        data = client.recv(1024)
        if not data:
            connections.remove(client)
            client.close()
            print("return")
            return
        print(data)
        client.sendall(data)
    except Exception as ex:
        connections.remove(client)
        client.close()
        print(ex)

def HTTP_handle(request):
    """Упрощённая модель контроллера"""
    ...
    db = connect() # неблокирующее соединение с базой
    return callback_0(db)

def callback_0(db):
    ...
    row = db.query() #какие-то данные из бвзы
    return callback_1(row)

def callback_1(row):
    ...
    db.close()
    return render(row)

s = socket.socket()
s.setblocking(False)
s.bind(('127.0.0.1', 4000))
s.listen(5)
connections = [s]
print('жду подключений')
try:
    while True:
        read_sockets, _, _ = select.select(connections, [], [])
        for r_socket in read_sockets:
            if r_socket == s:
                client, address = s.accept()
                print('connected', address)
                connections.append(client)
            else:
                handle(r_socket)
finally:
    s.close()

