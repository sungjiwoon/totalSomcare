# -*- coding: utf-8 -*-
'''
Created on 2020. 8. 9.

@author: jakim
'''

import RPi.GPIO as GPIO
import time

red = 16
green = 20
blue = 21
       
def outputValue(getMsg):
    try:
        GPIO.setmode(GPIO.BCM)       # GPIO BCM 모드 설정         
        GPIO.setwarnings(False)                            
        GPIO.setup(red, GPIO.OUT)   # 핀 모드를 출력으로 설정
        GPIO.setup(green, GPIO.OUT)
        GPIO.setup(blue, GPIO.OUT)
        GPIO.output(red, GPIO.LOW)  # 사용할 led 초기화
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)
        if getMsg == 0:
            print("off")
            GPIO.cleanup()
        if getMsg == 1: #기준보다 낮으면 안전하니까 파란색으로 설정
            print("safety")
            GPIO.output(red, True)
            GPIO.output(blue, True)
        elif getMsg == 2: #기준 근처면 초록색
            print("caution")
            GPIO.output(green, True)
            GPIO.output(red, True)
        elif getMsg == 3: #기준보다 높으면 빨간색
            print("warning")
            GPIO.output(green, True)
            GPIO.output(blue, True)
        elif getMsg == -1: #error
            print("error")
    finally:
        time.sleep(1)
        GPIO.cleanup()   


