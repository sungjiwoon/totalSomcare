# -*- coding: utf-8 -*-
import socket, pickle, threading, _thread      

HOST = '127.0.0.1'
PORT = 40008
ADDR = (HOST, PORT)
   
#웹서버와의 로컬통신
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

client_socket, addr = server_socket.accept()
print ('Connected with ' + addr[0] + ':' + str(addr[1]))

while True:
    
    data = client_socket.recv(1024) # 웹서버값
    
    if not data:
        break
        
    data_arr = pickle.loads(data)
    print('web server data ', data_arr)
        
   #라즈베리파이와의 소켓 통신
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    if data_arr[0] == 1: #id 값이 1번이면
        c_host = '192.168.35.133' #IP값은 추후에 각각의 라즈베리파이 ip로 수정
        c_portNum = 40001
    elif data_arr[0] == 2:
        c_host = '192.168.35.133'
        c_portNum = 40002
    elif data_arr[0] == 3:
        c_host = '192.168.35.133'
        c_portNum = 40003
    elif data_arr[0] == 4:
        c_host = '192.168.35.133'
        c_portNum = 7777
    elif data_arr[0] == 5:
        c_host = '192.168.35.133'
        c_portNum = 6666
        
    c.connect((c_host, c_portNum)) 
        
    c.send(str(data_arr[1]).encode()) #동작값 전송
        
    c.close()
     
    
client_socket.close()    
server_socket.close()

