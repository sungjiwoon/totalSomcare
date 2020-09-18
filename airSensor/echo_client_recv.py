import socket
import time
import air

HOST = '192.168.1.16' 
PORT = 10002

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(0)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(1)

while True:
    print(2)
    client_socket, addr = server_socket.accept()
    print(3)
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    print(4)

    getMsg = client_socket.recv(1024).decode()
    
    if not getMsg:
        break

    print('air data :' + getMsg)
    air.outputValue(int(getMsg))

client_socket.close()
server_socket.close()