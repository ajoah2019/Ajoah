import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

try:
    while True:
        input_value = GPIO.input(18)

        if input_value ==False:
            print('1')
        else :
            print('2')

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
