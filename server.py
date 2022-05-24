import socket
import threading

def handle(client):
    try:
        while True:
            data = client.recv(1024)
            if data == b'':
                client.close()
                print("break")
                break
            else:
                print(data)
                client.sendall(data)
    except:
        client.close()
        print("Ошибка разорвала соединение")


s = socket.socket()
s.bind(('127.0.0.1', 4000))
s.listen(3)
print('жду подключений')

while True:
    client, address = s.accept()
    print('connected', address)
    t = threading.Thread(target=handle, args=(client,))
    t.start()


