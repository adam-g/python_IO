# Imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

def blink(num_times, speed):
    for i in range(0, num_times):
        print("iteration " + str(i+1))
        GPIO.output(7, True)
        time.sleep(speed)
        GPIO.output(7, False)
        time.sleep(speed)
    print("done")
    GPIO.cleanup()

iterations = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter length of each blink (seconds): ")
blink(int(iterations), float(speed))