import RPi.GPIO as GPIO
import time

# GPIO.setup(7,GPIO.OUT)

# Determines for how long a note will play
# If scale is set to 1, the duration will be 0.5 seconds
# If scale is set to 0.01, it allows for playing notes through keyboard input
# in the console
scale = 0.01

# Plays the note a, if pin is connected to a buzzer
# pin is an int identifying the GPIO pin that will send the signal,
# the pin numbering follows the GPIO.BOARD mode (RPi.GPIO library)
# sleep time is calculated 1/f where f is the frequency of the note
def a_note(pin):
    #GPIO.setup(pin, GPIO.OUT)
    for i in range(0,int(250*scale)):
        GPIO.output(pin, True)
        time.sleep(0.0023)
        GPIO.output(pin, False)

def b_note(pin):
    #GPIO.setup(pin, GPIO.OUT)
    for i in range(0,int(255*scale)):
        GPIO.output(pin, True)
        time.sleep(0.0020)
        GPIO.output(pin, False)

def c_note(pin):
    #GPIO.setup(pin, GPIO.OUT)
    for i in range(0,int(260*scale)):
        GPIO.output(pin, True)
        time.sleep(0.0019)
        GPIO.output(pin, False)

def d_note(pin):
    #GPIO.setup(pin, GPIO.OUT)
    for i in range(0,int(290*scale)):
        GPIO.output(pin, True)
        time.sleep(0.0017)
        GPIO.output(pin, False)

def e_note(pin):
    #GPIO.setup(pin, GPIO.OUT)
    for i in range(0,int(330*scale)):
        GPIO.output(pin, True)
        time.sleep(0.0015)
        GPIO.output(pin, False)

def f_note(pin):
    #GPIO.setup(pin, GPIO.OUT)
    for i in range(0,int(350*scale)):
        GPIO.output(pin, True)
        time.sleep(0.0014)
        GPIO.output(pin, False)

def g_note(pin):
    #GPIO.setup(pin, GPIO.OUT)
    for i in range(0,int(392*scale)):
        GPIO.output(pin, True)
        time.sleep(0.0013)
        GPIO.output(pin, False)

# Makes the buzzer play the tune "Spanien"
# pin is an int representing the IO pin sending the signal to the buzzer
# pin numbering is according to the GPIO.BOARD mode (RPi.GPIO library)
def spanien_tune(pin):
    # Sets the duration of a note to 
    # 0.5 seconds per function call
    global scale
    prev_scale = scale
    scale = 1
    
    for i in range(0,2):
        c_note(pin)
        time.sleep(0.03)
        d_note(pin)
        time.sleep(0.03)
        e_note(pin)
        e_note(pin)
        time.sleep(0.03)
    
    for i in range(0,4):
        d_note(pin)
        time.sleep(0.03)

    for i in range(0,2):
        c_note(pin)
        c_note(pin)
        time.sleep(0.03)

    scale = prev_scale

