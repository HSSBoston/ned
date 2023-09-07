import RPi.GPIO as GPIO
import time, kintone, subprocess
from datetime import datetime
GPIO.setmode(GPIO.BCM)
# Start writing your program below

GPIO.setup(21, GPIO.OUT)

sdomain = ""
appId = ""
token = ""

while True:
    try:
        record = kintone.getRecord(subDomain=sdomain,
                                   apiToken=token,
                                   appId=appId,
                                   recordId="1")
        alarmTimeHr = int(record["alarmTimeHr"]["value"])
        alarmTimeMin = int(record["alarmTimeMin"]["value"])
        startTimeHr = int(record["startTimeHr"]["value"])
        startTimeMin = int(record["startTimeMin"]["value"])
        endTimeHr = int(record["endTimeHr"]["value"])
        endTimeMin = int(record["endTimeMin"]["value"])
        print("Alarm time: " + str(alarmTimeHr) + ":" + str(alarmTimeMin))
        print("Start time: " + str(startTimeHr) + ":" + str(startTimeMin))
        print("End time: " + str(endTimeHr) + ":" + str(endTimeMin))
        
        dt = datetime.now()
        currentTimeHr = dt.hour
        currentTimeMin = dt.minute

        if(alarmTimeHr == currentTimeHr and
           alarmTimeMin == currentTimeMin):
            for i in range(5):
                GPIO.output(21, GPIO.HIGH)
                time.sleep(2)
                GPIO.output(21, GPIO.LOW)
                time.sleep(1)
            
            commandMusic = "vlc -I dummy chrissy_wake_up.mp3 --play-and-exit"
                
            commandVoice = "vlc -I dummy 'http://translate.google.com/translate_tts?"\
                        + "ie=UTF-8&client=tw-ob&tl=ja&"\
                        + "q=水を飲みましょう' --play-and-exit"
            
            subprocess.run(commandMusic, shell=True)
            
            for i in range(3):
                subprocess.run(commandVoice, shell=True)
                time.sleep(2)

        if(startTimeHr <= currentTimeHr and
           currentTimeHr <= endTimeHr):
           if(startTimeMin == currentTimeMin):
                if startTimeHr % 2 == 0:
                    if currentTimeHr % 2 ==0:
                        for i in range(5):
                            GPIO.output(21, GPIO.HIGH)
                            time.sleep(1)
                            GPIO.output(21, GPIO.LOW)
                            time.sleep(1)
                if startTimeHr % 2 == 1:
                    if currentTimeHr % 2 ==1:
                        for i in range(5):
                            GPIO.output(21, GPIO.HIGH)
                            time.sleep(1)
                            GPIO.output(21, GPIO.LOW)
                            time.sleep(1) 
        
        time.sleep(60)        
    except KeyboardInterrupt:
        break

# Write your program above this line
GPIO.cleanup()