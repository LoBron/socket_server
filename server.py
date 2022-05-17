import socket


s = socket.socket()
s.bind(('127.0.0.1', 4000))
s.listen(3)
print('жду подключений')
while True:
    client_socket, client_address = s.accept()
    print('connected', client_address)
    data = client_socket.recv(1024)
    print(data)
    client_socket.sendall(data)
    client_socket.close()
s.close()

