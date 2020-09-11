import RPi.GPIO as GPIO
import time
import pickle

def inputValue():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.IN)
    
    setMsg = 0
    
    try:
        if GPIO.input(25) == True:
            setMsg = 1
        elif GPIO.input(25) == False:
            setMsg = 0
        
        GPIO.cleanup()  
    
    except KeyboardInterrupt:
        setMsg = -1    
        
    return [2, setMsg, -1, setMsg];
        
def outputValue(getMsg):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(13, GPIO.OUT)
    
    try:
        if getMsg == 0:
            print("Sensor Off!!")
            GPIO.output(13, True)
                         
        elif getMsg == 1:
            print("Sensor On!!")
            GPIO.output(13, False)
            time.sleep(20)
            
        elif getMsg == -1:
            print("Error!!")
        
    except KeyboardInterrupt:
        getMsg = -1