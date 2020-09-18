# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
inputPin = 17
outputPin1 = 4
outputPin2 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(outputPin1,GPIO.OUT)
GPIO.setup(outputPin2,GPIO.OUT)
i = 0
while i < 2:
    GPIO.output(outputPin1, True)
    time.sleep(1)
    i = i + 1
    
i = 0
while i < 2:
    GPIO.output(outputPin2, True)
    time.sleep(1)
    i = i + 1
GPIO.cleanup() 



            

        
        

