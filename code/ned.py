import RPi.GPIO as GPIO
import time, subprocess
from datetime import datetime
GPIO.setmode(GPIO.BCM)
# Start writing your program below

GPIO.setup(21, GPIO.OUT)

for i in range(5):
    GPIO.output(21, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(21, GPIO.LOW)
    time.sleep(1)
                    
command = "vlc -I dummy 'http://translate.google.com/translate_tts?"\
    + "ie=UTF-8&client=tw-ob&tl=ja&"\
    + "q=水をのめ' --play-and-exit"

for i in range(5):
    subprocess.run(command, shell=True)
    time.sleep(2)

# Write your program above this line
GPIO.cleanup()
