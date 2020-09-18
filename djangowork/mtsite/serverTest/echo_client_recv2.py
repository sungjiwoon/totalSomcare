import socket
import time

HOST = '192.168.35.195' 
PORT = 9998

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))

    getMsg = client_socket.recv(1024).decode()
    
    if not getMsg:
        break

    print('gas data :' + getMsg)

client_socket.close()
server_socket.close()
