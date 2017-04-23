import RPi.GPIO as GPIO  
import time  
# blinking function
pin = 11


def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(50)  
        return  
# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)  
# set up GPIO output channel  
GPIO.setup(pin, GPIO.OUT)  
# blink GPI7 50 times  
for i in range(0,2):  
        blink(pin)  
GPIO.cleanup()
