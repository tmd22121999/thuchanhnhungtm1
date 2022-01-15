# import modules
import RPi.GPIO as GPIO
import time

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
# loop 5 times
for i in range(5):
    
    # flash output pin 3
    GPIO.output(12, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12, GPIO.LOW)
    time.sleep(1)
    
    # read input pin 5
    if GPIO.input(11) == GPIO.HIGH:
        GPIO.output(16, GPIO.HIGH)
        print("Pin 11 is on")
    else:
        GPIO.output(16, GPIO.LOW)
        print("Pin 11 is off")    
