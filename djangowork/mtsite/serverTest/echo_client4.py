import socket, pickle, time
 
HOST = '192.168.35.133'   
 
PORT = 8888       
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
client_socket.connect((HOST, PORT))
 
while True :
    setMsg = [4, 1, 40, 90]
    setMsg_string = pickle.dumps(setMsg)
    time.sleep(1)
    client_socket.send(setMsg_string)
    
    print('client setMsg: ' ,pickle.loads(setMsg_string))
    getMsg = client_socket.recv(1024)
    print('Received', repr(getMsg.decode()))
    
    
client_socket.close()