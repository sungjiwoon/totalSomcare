# -*- coding: utf-8 -*-

import serial
from PMS7003 import PMS7003
import RPi.GPIO as GPIO
# from echo_client_send import setMsg

#sensor
dust = PMS7003()
     
# Baud Rate
Speed = 9600
     
# UART / USB Serial
USB0 = '/dev/ttyUSB0'
UART = '/dev/ttyAMA0'
     
# USE PORT
SERIAL_PORT = USB0
      
#serial setting
ser = serial.Serial(SERIAL_PORT, Speed, timeout = 1)
 
#led
GPIO.setmode(GPIO.BCM)
     
red = 19
green = 26
blue = 21
     
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
 
#fan
POWER = 20
IN = 4
GPIO.setup(IN, GPIO.OUT)
GPIO.setup(POWER, GPIO.OUT)
     
GPIO.output(POWER, 1)
pwm_in = GPIO.PWM(IN, 500)
pwm_in.start(0)

def inputValue():
    try :
        #sensor
        dust = PMS7003()
    
        # Baud Rate
        Speed = 9600
    
        # UART / USB Serial
        USB0 = '/dev/ttyUSB0'
        UART = '/dev/ttyAMA0'
    
        # USE PORT
        SERIAL_PORT = USB0
     
        #serial setting
        ser = serial.Serial(SERIAL_PORT, Speed, timeout = 1)
        
        buffer = ser.read(1024)
                
        if(dust.protocol_chk(buffer)):
            data = dust.unpack_data(buffer)
            pm10 = data[dust.DUST_PM10_0_ATM]
            pm2_5 = data[dust.DUST_PM2_5_ATM]
                    
#             if pm10 >= 151 or pm2_5 >= 76:
#                 setMsg = 2 #매우나쁨 빨강
#             elif pm10 >= 81 or pm2_5 >= 36:
#                 setMsg = 1 #나쁨 노랑
#             else:
#                 setMsg = 0 #좋음 초록

            if pm10 >= 25 or pm2_5 >= 20:
                situation = 3 #매우나쁨 빨강
            elif pm10 >= 21 or pm2_5 >= 15:
                situation = 2 #나쁨 노랑
            elif pm10 >= 17 or pm2_5 >= 10:
                situation = 1 #좋음 초록
            else:
                situation = 0 #꺼짐
                    
        else:
            print ("data read Err")
            situation = -1
            pm2_5 = -1;
            pm10 = -1;
            
        setMsg = [1, situation, -1, pm2_5, pm10]
            
        return setMsg
    except :
        GPIO.output(red, 1)
        GPIO.output(green, 1)
        GPIO.output(blue, 1)
        GPIO.output(POWER, 0)
#         GPIO.cleanup()
    finally:
        ser.close()
def outputValue(getMsg):
    try :
        #led
        GPIO.setmode(GPIO.BCM)
             
        red = 19
        green = 26
        blue = 21
             
        GPIO.setup(red, GPIO.OUT)
        GPIO.setup(green, GPIO.OUT)
        GPIO.setup(blue, GPIO.OUT)
         
        #fan
        POWER = 20
        IN = 4
        GPIO.setup(IN, GPIO.OUT)
        GPIO.setup(POWER, GPIO.OUT)
             
        GPIO.output(POWER, 1)
#         pwm_in = GPIO.PWM(IN, 500)
        pwm_in.start(0)
        
        if getMsg == 0:
            GPIO.output(red, 1)
            GPIO.output(green, 1)
            GPIO.output(blue, 1)
            pwm_in.ChangeDutyCycle(0)
        elif getMsg == 1:
            GPIO.output(red, 1)
            GPIO.output(green, 0)
            GPIO.output(blue, 1)
            pwm_in.ChangeDutyCycle(30)
        elif getMsg == 2:
            GPIO.output(red, 0)
            GPIO.output(green, 0)
            GPIO.output(blue, 1)
            pwm_in.ChangeDutyCycle(50)
        elif getMsg == 3:
            GPIO.output(red, 0)
            GPIO.output(green, 1)
            GPIO.output(blue, 1)
            pwm_in.ChangeDutyCycle(100)
        else:
            pass
    except:
        GPIO.output(red, 1)
        GPIO.output(green, 1)
        GPIO.output(blue, 1)
        GPIO.output(POWER, 0)
        GPIO.cleanup()
    finally:
        ser.close()
