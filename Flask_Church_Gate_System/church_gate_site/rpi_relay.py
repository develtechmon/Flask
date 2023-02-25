import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Close the gate
GPIO.setup(14,GPIO.OUT)

# Pause and Close the gate
GPIO.setup(15,GPIO.OUT)

def rpi_relay(state):
    try:
        if state == "open":
            GPIO.output(14, GPIO.HIGH)
            print('Relay 1 ON')
            time.sleep(1)
        
        elif state == "pause":
            GPIO.output(15, GPIO.HIGH)
            print('Relay 2 ON')
            time.sleep(1)
        
        elif state == "close":
            GPIO.output(15, GPIO.HIGH)
            print('Relay 2 ON')
            time.sleep(1)
    finally:
        GPIO.cleanup()
         