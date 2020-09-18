import socket, pickle, threading, _thread      
        
def handler (client_socket, addr) :
    while 1 :
        #echo-client에서 보낸 리스트
        data = client_socket.recv(1024)
    
        if not data:
            break
        
        data_arr = pickle.loads(data)
        print('server data ', data_arr) #echo-client에게서 받은 리스트 출력
        
        #local network/ 웹서버와 소켓프로그래밍 하는 부분
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 40007)) 
        
        s.send(data)    
        num = s.recv(1024) #웹서버에서 받은 숫자(동작값)
        
        client_socket.send(num) 
        #이 부분은 echo-client와의 통신 코드, echo-client로 보내는 코드(동작값을 파이로  보낸다)
        s.close()
               
    client_socket.close()
    
#멀티 쓰레드 코드
if __name__ == '__main__':
    HOST = '192.168.0.9' #연결하는 와이파이에 따라 변경해야 됨
    PORT = 8888 
    ADDR = (HOST, PORT)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5) #클라이언트를 최대 5개까지 받을 수 있다
 
while True:
    client_socket, addr = server_socket.accept()
    _thread.start_new_thread(handler, (client_socket, addr)) 
    #쓰레드 생성 코드, 생성 이후 각각의 클라이언트가 통신될 때마다 handler 함수가 작동됨
    print('Connected by', addr)
    
server_socket.close()



