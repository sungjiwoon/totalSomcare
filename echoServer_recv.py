import socket, time
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

def autoCheck(data):
    try:
        is_auto = data[2]
        
        if is_auto == 1 or is_auto == 0:
            return [data[0], data[1]]
        else:
            if data[0] == 1:
                sql = 'Select * from airSensorInfo ORDER BY date DESC LIMIT 2'
                cur.execute(sql)
                i = cur.fetchall()
                db_auto = i[1][2]
            
            elif data[0] == 2:
                sql = 'Select * from motionSensorInfo ORDER BY date DESC LIMIT 2'
                cur.execute(sql)
                i = cur.fetchall()
                db_auto = i[1][2]

            elif data[0] == 3:
                sql = 'Select * from tempSensorInfo ORDER BY date DESC LIMIT 2'
                cur.execute(sql)
                i = cur.fetchall()
                db_auto = i[1][2]

            elif data[0] == 4:
                sql = 'Select * from rainSensorInfo ORDER BY date DESC LIMIT 2'
                cur.execute(sql)
                i = cur.fetchall()
                db_auto = i[1][2]

            elif data[0] == 5:
                sql = 'Select * from gasSensorInfo ORDER BY date DESC LIMIT 2'
                cur.execute(sql)
                i = cur.fetchall()
                db_auto = i[1][2]
            
            if db_auto == 0:
                return [data[0], data[1]]
            else:
                return -1
    except:
         return -1
        

def socketProgramming(host, portNum, getMsg):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, portNum)) 
    c.send(str(getMsg[1]).encode())
    c.close() 

while True :
    con = pymysql.connect(
    host = "3.34.98.103",
    user = "totalSOM", 
    password = "rhdgkdrlavh4536",
    database = "tsDB",
    charset = 'utf8'
    ) 

    sql = "Select * from airSensorInfo ORDER BY date DESC LIMIT 1" #air 최근 행 1개 가져오기
    cur.execute(sql)
    data1 = cur.fetchone()
    list1 = list(data1)
    list1[0] = 1
    data1 = tuple(list1)

    sql = "Select * from motionSensorInfo ORDER BY date DESC LIMIT 1" #air 최근 행 1개 가져오기
    cur.execute(sql)
    data2 = cur.fetchone()
    list2 = list(data2)
    list2[0] = 2
    data2 = tuple(list2)

    sql = "Select * from tempSensorInfo ORDER BY date DESC LIMIT 1" #air 최근 행 1개 가져오기
    cur.execute(sql)
    data3 = cur.fetchone()
    list3 = list(data3)
    list3[0] = 3
    data3 = tuple(list3)

    sql = "Select * from rainSensorInfo ORDER BY date DESC LIMIT 1" #air 최근 행 1개 가져오기
    cur.execute(sql)
    data4 = cur.fetchone()
    list4 = list(data4)
    list4[0] = 4
    data4 = tuple(list4)

    sql = "Select * from gasSensorInfo ORDER BY date DESC LIMIT 1" #air 최근 행 1개 가져오기
    cur.execute(sql)
    data5 = cur.fetchone()
    list5 = list(data5)
    list5[0] = 5
    data5 = tuple(list5)   
    
    getMsg1 = autoCheck(data1)
    getMsg2 = autoCheck(data2)
    getMsg3 = autoCheck(data3)
    getMsg4 = autoCheck(data4)
    getMsg5 = autoCheck(data5)
    
    print(getMsg1)
    print(getMsg2)
    print(getMsg3)
    print(getMsg4)
    print(getMsg5)
    
    if getMsg1 != -1 :
        if getMsg1[0] == 1 :
            socketProgramming('192.168.1.16', 10002, getMsg1)     
            
    if getMsg2 != -1 :
        if getMsg2[0] == 2 :
            socketProgramming('192.168.1.13', 10012, getMsg2)
    
    if getMsg3 != -1 :
        if getMsg3[0] == 3 :
            socketProgramming('192.168.1.18', 10022, getMsg3)
        
    if getMsg4 != -1 :
        if getMsg4[0] == 4 :
            socketProgramming('192.168.1.17', 10032, getMsg4)
            
    if getMsg5 != -1 :
        if getMsg5[0] == 5 :
            socketProgramming('192.168.1.15', 10042, getMsg5)
    
    time.sleep(3)