# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import pickle

sensor = Adafruit_DHT.DHT11
inputPin = 17
outputPin1 = 4
outputPin2 = 27

def inputValue() :    
    setMsg = [3, 0, -1, 0, 0]
    try :                
        humid, temp = Adafruit_DHT.read_retry(sensor, inputPin)
        if temp is not None and humid is not None:
            print('Temperature={0:0.1f}*C Humidity={1:0.1f}%'.format(temp, humid))
            setMsg[3] = temp
            setMsg[4] = humid
            
        if temp is not None:            
            if temp > 20.0: 
                setMsg[1] = 2 
            elif temp < 10.0: 
                setMsg[1] = 1 
            else :
                setMsg[1] = 0 
        time.sleep(2)    
    except KeyboardInterrupt:
        setMsg[1] = -1    
    return setMsg


def outputValue(getMsg):
    try :
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(outputPin1,GPIO.OUT)
        GPIO.setup(outputPin2,GPIO.OUT)
        if getMsg == 2:  #불빛 여러번 깜빡이게 할려고 한거임
            i = 0
            while i < 2:
                GPIO.output(outputPin1, True)
                time.sleep(1)
                i = i + 1
                
        elif getMsg == 1: #불빛 여러번 깜빡이게 할려고 한거임
            i = 0
            while i < 2:
                GPIO.output(outputPin2, True)
                time.sleep(1)
                i = i + 1
         
        elif getMsg == 0: #기본
            print("default")
            
        elif getMsg == -1:
            print("error")
                
    except KeyboardInterrupt:
        print("error") 
        GPIO.cleanup()   
        
    GPIO.cleanup()  
        



            

        
        

