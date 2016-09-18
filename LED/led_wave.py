# Imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.output(7, True)
GPIO.output(11, True)
GPIO.output(12, True)
GPIO.output(13, True)
pins = [7, 11, 12, 13]


for i in range(0,15):
    for pin in pins:
        time.sleep(0.1)
        if GPIO.input(pin):
            GPIO.output(pin, 0)
        else:
            GPIO.output(pin, 1)    


GPIO.output(7, False)
GPIO.output(11, False)
GPIO.output(12, False)
GPIO.output(13, False)
GPIO.cleanup()