import socket, pickle, time
 
HOST = '192.168.35.195'   
 
PORT = 8888       
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
client_socket.connect((HOST, PORT))
 
while True :
    setMsg = [3, 2, 1, 30, 90]
    setMsg_string = pickle.dumps(setMsg)
    print('client setMsg : ', pickle.loads(setMsg_string))
    client_socket.send(setMsg_string)
            
    time.sleep(5)

    
    
client_socket.close()