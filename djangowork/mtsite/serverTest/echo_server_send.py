# -*- coding: utf-8 -*-
import socket, pickle, threading, _thread      
import pymysql

# DB 접속
con = pymysql.connect(
    host = "3.34.98.103",
    user = "totalSOM", 
    password = "rhdgkdrlavh4536",
    database = "tsDB",
    charset = 'utf8'
)

#커서 생성
cur = con.cursor()

#민선아 여기는 각각의 테이블에서 제일 최근 레코드 가져오는 코드를 조건문 안에 다 넣어 줘야 돼 
def recvDB(senserId):
    if senserId == 1: #미세먼지
        sql = "Select * from airSensorInfo ORDER BY date DESC LIMIT 1" #air 최근 행 1개 가져오기
        cur.execute(sql)
        data = cur.fetchone()
        db_auto = data[2]

    elif senserId == 2: #움직임
        sql = "Select * from motionSensorInfo ORDER BY date DESC LIMIT 1" #motion 최근 행 1개 가져오기
        cur.execute(sql)
        data = cur.fetchone()
        db_auto = data[2]   

    elif senserId == 3: #냉난방기
        sql = "Select * from tempSensorInfo ORDER BY date DESC LIMIT 1" #temp 최근 행 1개 가져오기
        cur.execute(sql)
        data = cur.fetchone()
        db_auto = data[2]

    elif senserId == 4: #비
        sql = "Select * from rainSensorInfo ORDER BY date DESC LIMIT 1" #rain 최근 행 1개 가져오기
        cur.execute(sql)
        data = cur.fetchone()
        db_auto = data[2]

    elif senserId == 5: #가스 
        sql = "Select * from gasSensorInfo ORDER BY date DESC LIMIT 1" #gas 최근 행 1개 가져오기 
        cur.execute(sql)
        data = cur.fetchone()
        db_auto = data[2]
        
    return db_auto

def compareDB(db_auto, is_auto):
    if db_auto == 1 and is_auto == -1:
        is_auto = 1
    elif db_auto == -1 and is_auto == 1:
        is_auto = -1
    elif db_auto == 0:
        is_auto = -1
    return is_auto

def sendDB(userid, data_arr):
    if data_arr[0] == 1: #미세먼지
        sql = "insert into airSensorInfo (user_id, situation, is_auto, air1_value, air2_value) VALUES( %s, %s, %s, %s, %s)"
        val = (userid, data_arr[1], data_arr[2], data_arr[3], data_arr[4])
        cur.execute(sql, val)
        con.commit()

    elif data_arr[0] == 2: #움직임
        sql = "insert into motionSensorInfo (user_id, situation, is_auto, motion_value) VALUES( %s, %s, %s, %s)"
        val = (userid, data_arr[1], data_arr[2], data_arr[3])
        cur.execute(sql, val)
        con.commit()

    elif data_arr[0] == 3: #냉난방기
        sql = "insert into tempSensorInfo (user_id, situation, is_auto, temp_value, humid_value) VALUES( %s, %s, %s, %s, %s)"
        val = (userid, data_arr[1], data_arr[2], data_arr[3], data_arr[4])
        cur.execute(sql, val)
        con.commit()

    elif data_arr[0] == 4: #비
        sql = "insert into rainSensorInfo (user_id, situation, is_auto, rain_value) VALUES( %s, %s, %s, %s)"
        val = (userid, data_arr[1], data_arr[2], data_arr[3])
        cur.execute(sql, val)
        con.commit()

    elif data_arr[0] == 5: #가스
        sql = "insert into gasSensorInfo (user_id, situation, is_auto, gas_value) VALUES( %s, %s, %s, %s)"
        val = (userid, data_arr[1], data_arr[2], data_arr[3])
        cur.execute(sql, val)
        con.commit()
        


def handler (client_socket, addr) :
    while 1 :
        #echo-client에서 보낸 리스트
        data = client_socket.recv(1024)
    
        if not data:
            break
        
        data_arr = pickle.loads(data)
        print('server data ', data_arr) 
        #echo-client에게서 받은 리스트 출력
        
        #DB코드 추가
        db_auto = recvDB(data_arr[0])
        is_auto = compareDB(db_auto, data_arr[2])
        data_arr[2] = is_auto
        sendDB(1, data_arr)
               
    client_socket.close()
    
#멀티 쓰레드 코드
if __name__ == '__main__':
    HOST = '192.168.35.195' #연결하는 와이파이에 따라 변경해야 됨
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