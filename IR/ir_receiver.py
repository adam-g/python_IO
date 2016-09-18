import RPi.GPIO as GPIO
import time
import threading
from Queue import Queue
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(7, GPIO.OUT)

def thread_receive():
    f = open('log','a')    
    for x in range(300000):
        f.write(str(read_receiver()))
        if x % 100 == 0:
            f.write('\n')
            
def thread_send():
    for x in range(100000):
        ir_send()

def read_receiver():
    time.sleep(0.0000069)
    return GPIO.input(11)

def ir_send():
    GPIO.output(7, True)
    time.sleep(0.000021)
    GPIO.output(7, False)

t_receive = threading.Thread(target = thread_receive)
t_receive.daemon = True 
t_receive.start()
t_send = threading.Thread(target = thread_send)
t_send.daemon = True
t_send.start()
time.sleep(10)

GPIO.cleanup()


