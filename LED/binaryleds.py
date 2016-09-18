# Imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# int fungerar foer heltal mellan 0 och 15
def divide_by_2(int):
    print("funktion")
    x = int
    stack = []
    while x != 0: 
        stack.append(x % 2)
        x = x - (x % 2)
        x = x / 2
    while len(stack) < 4:
        stack.append(0)        
    return stack

tal = raw_input("Heltal mellan 0 och 15: ")
binary_number = divide_by_2(int(tal))
print "talet aer: ", binary_number

# Minst signifikanta bit till mest 
GPIO.output(7, binary_number[0])
GPIO.output(11, binary_number[1])
GPIO.output(12, binary_number[2])
GPIO.output(13, binary_number[3])
time.sleep(5)

GPIO.output(7, False)
GPIO.output(11, False)
GPIO.output(12, False)
GPIO.output(13, False)
GPIO.cleanup()