import socket
import threading

def handle(client, address):
    try:
        while True:
            data = client.recv(1024)
            if data == b'':
                client.close()
                print("break")
                break
            print(data)
            client.sendall(data)
    except Exception as ex:
        client.close()
        print(f'{ex} {address}')


s = socket.socket()
s.bind(('127.0.0.1', 4000))
s.listen(5)
print('жду подключений')
try:
    while True:
        client, address = s.accept()
        print('connected', address)
        t = threading.Thread(target=handle, args=(client, address))
        t.start()
finally:
    s.close()

