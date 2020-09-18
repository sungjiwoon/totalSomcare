import time
import RPi.GPIO as GPIO
import spidev

pin2 = 19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin2, GPIO.OUT)
p = GPIO.PWM(pin2, 50)
p.start(0)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

window = -1

def read_spi_adc(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out

def inputValue() :
    setMsg = 0
    try:
        adc_out = read_spi_adc(0)
        print(adc_out)
        if adc_out < 1000 :
            setMsg = 1
           
        if adc_out == 0 :
            setMsg = -1
    except KeyboardInterrupt:
        setMsg = 0
    finally:
        return [4, setMsg, -1, -1]
        
def outputValue(getMsg) :
    try:
        global window
        if getMsg == 1 :
            print("It's rainy day")
            if window == -1 :
                for i in [1]:
                    p.ChangeDutyCycle(5.0) 
                    time.sleep(1)
                    window = 1
        elif getMsg == 0 :
            print("Sunny day")                  
        else :
            print("Error")
    except KeyboardInterrupt:
        p.stop()
    GPIO.cleanup()