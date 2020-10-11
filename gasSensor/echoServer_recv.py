# -*- coding: utf-8 -*-
'''
Created on 2020. 8. 28.

@author: jakim
'''

import socket
import time
import gas_in
import gas_out

HOST = '192.168.1.15'
PORT = 10042 #가스 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))

    getMsg = client_socket.recv(1024).decode()

    # 빈 문자열을 수신하면 루프를 중지합니다. 
    if not getMsg:
        break
    
    gas_out.outputValue(int(getMsg))

                        
client_socket.close()
server_socket.close()                     
