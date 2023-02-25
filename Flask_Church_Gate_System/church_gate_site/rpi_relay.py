import RPi.GPIO as GPIO
import time

def rpi_relay(state):
    GPIO.setmode(GPIO.BCM)
    
    # Close the gate
    GPIO.setup(14,GPIO.OUT)

    # Pause and Close the gate
    GPIO.setup(15,GPIO.OUT)
    print(state)
    try:
        if state == "open":
            GPIO.output(14, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
            print('Relay 1 ON')
            time.sleep(1)
        
        elif state == "pause":
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(14, GPIO.LOW)
            print('Relay 2 ON')
            time.sleep(1)
            
        
        elif state == "close":
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(14, GPIO.LOW)
            print('Relay 2 ON')
            time.sleep(1)
    except:
        pass
    
    finally:
        GPIO.cleanup()
         