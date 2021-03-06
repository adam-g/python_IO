import RPi.GPIO as GPIO
import threading
from Queue import Queue
import time

# The pin sending the signal to the buzzer,
# the pin number is according to the GPIO.BOARD mode (RPi.GPIO library) 
pin1 = 7
pin2 = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
import unbuffered_input
import note_lib

def user_input():
    play = True
    while play:
        input = unbuffered_input.input_with()
        if(input == 'q'):
            play = False
        elif(input == 'nobodyexpects'):
            note_lib.spanien_tune()
        elif(input == '1'):
            note_lib.a_note(pin)
        elif(input == '2'):
            note_lib.b_note(pin)
        elif(input == '3'):
            note_lib.c_note(pin)
        elif(input == '4'):
            note_lib.d_note(pin)
        elif(input == '5'):
            note_lib.e_note(pin)
        elif(input == '6'):
            note_lib.f_note(pin)
        elif(input == '7'):
            note_lib.g_note(pin)

q = Queue()
            
def spanien_thread():
    while True:
        pin = q.get()
        note_lib.spanien_tune(pin)
        q.task_done()
       
#user_input()
#note_lib.spanien_tune(pin)

for x in range(2):
    t = threading.Thread(target = spanien_thread)
    t.daemon = True
    t.start()

for pin in [7, 11]:
    q.put(pin)
    time.sleep(4.24)

q.join()
#note_lib.spanien_tune(11)
note_lib.GPIO.cleanup()

