import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

for i in range (0,500):
    GPIO.output(11, True)
    time.sleep(0.0008)
    GPIO.output(11, False)
    time.sleep(0.008)
    print(i)  

GPIO.cleanup()