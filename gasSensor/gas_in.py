# -*- coding: utf-8 -*- 

import spidev
import time

CONST_STANDARD = 100  #가스 감지 값

#adc랑 라즈베리파이 spi 통신하는 코드 
#read_spi_adc를 통해서 센서값 읽음
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 100000

def read_spi_adc(adcChannel):
    buff = spi.xfer2([1, (8 + adcChannel) << 4, 0])
    adcValue = ((buff[1] & 3) << 8) + buff[2]
    return adcValue

def inputValue():
    try:
        setMsg = [5, 0, -1, 0]
        adcChannel = 0
        adcValue = read_spi_adc(adcChannel)
        setMsg[3] = adcValue
        print("gas {}" .format(adcValue)) #가스센서에서 받은 값 출력해본다. 잘 돌아가면 주석처리 하기
        if adcValue == 0:
            setMsg[1] = 0
        elif adcValue < CONST_STANDARD - 10: #기준보다 낮으면 안전함 defalut값
            setMsg[1] = 1
        elif CONST_STANDARD - 10 <= adcValue <= CONST_STANDARD: #기준 근처
            setMsg[1] = 2
        else: #기준보다 높으면 위험!
            setMsg[1] = 3
            
        time.sleep(1)
    except KeyboardInterrupt: #키보드 누를 경우에도 -1전송
        setMsg[1] = -1

    return setMsg
        

