import socket
import threading

def handle(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if data == b'':
                client_socket.close()
                print("break")
                break
            else:
                print(data)
                client_socket.sendall(data)
    except:
        client_socket.close()
        print("Ошибка разорвала соединение")


s = socket.socket()
s.bind(('127.0.0.1', 4000))
s.listen(3)
print('жду подключений')
while True:
    client_socket, client_address = s.accept()
    print('connected', client_address)

    t = threading.Thread(target=handle, args=(client_socket, ))
    t.start()

s.close()

