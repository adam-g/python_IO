import RPi.GPIO as GPIO
import time
import threading
from Queue import Queue
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(7, GPIO.OUT)


def read_receiver():
    return not GPIO.input(11)

def thread_receive():
    f = open('log','a')    
    for i in range(3000):
        time.sleep(0.0005)
        p = read_receiver()
        if p:
            for x in range(8):
                time.sleep(0.001)
                f.write(str(int(read_receiver())))
            f.write('\n')
            time.sleep(0.001)
    f.close()

    #for x in range(300000):
    #    f.write(str(read_receiver()))
    #    if x % 100 == 0:
    #        f.write('\n')
            
def ir_send():
    GPIO.output(7, True)
    time.sleep(0.001)
    GPIO.output(7, False)
    time.sleep(0.001)
    GPIO.output(7, False)
    time.sleep(0.001)
    GPIO.output(7, False)
    time.sleep(0.001)
    GPIO.output(7, True)
    time.sleep(0.001)
    GPIO.output(7, False)
    time.sleep(0.001)
    GPIO.output(7, True)
    time.sleep(0.001)
    GPIO.output(7, False)
    time.sleep(0.001)
    GPIO.output(7, True)
    time.sleep(0.001)
    GPIO.output(7, False)

def thread_send():
    for x in range(100):
        time.sleep(0.01)
        ir_send()


t_receive = threading.Thread(target = thread_receive)
t_receive.daemon = True 
t_receive.start()
t_send = threading.Thread(target = thread_send)
t_send.daemon = True
t_send.start()
time.sleep(5)

GPIO.cleanup()

f = open('log', 'r')
count = 0
for line in f:  
    if line == '11101010\n':
        count += 1
print count

