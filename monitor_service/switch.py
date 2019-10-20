import RPi.GPIO as GPIO 
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
#LED_list=[18, 23, 24, 25]
 
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(LED_list, GPIO.OUT)
#GPIO.output(LED_list, False)
 
def LED369(channel):
    print("LED369 activated")
 
GPIO.add_event_detect(21, GPIO.BOTH, callback=LED369, bouncetime=300)
print("Wait for the switch event.")
 
while True:
    try:
        sleep(5)
    except KeyboardInterrupt:
        print("Au revoir!".center(20))
        GPIO.cleanup()
        break


