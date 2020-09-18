import socket, pickle, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind(('127.0.0.1', 40007))
except socket.error as msg:
    print ('Bind Failed. Error code: ' + str(msg[0]) + ' Message: ' + msg[1])
    sys.exit()
s.listen(1)
    
while 1 :  
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))

    data = conn.recv(1024)
    
    data_arr = pickle.loads(data)
    print('server data ', data_arr)
    conn.send(str(1).encode())
    
conn.close()
s.close() 
