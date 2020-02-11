from __future__ import print_function
from dbFirestoreAjoah import *
import RPi.GPIO as GPIO
import argparse
from time import sleep

# interpret Args
parser = argparse.ArgumentParser()
parser.add_argument('SENSOR_NUMBER', type=int,
                help="What is the Sensor number?[1 or 2]")

args = parser.parse_args()

SENSOR_NUMBER = args.SENSOR_NUMBER
print('SensorNumber['+str(SENSOR_NUMBER)+']')


# data Init 
isTest=True

pirPin=0

if SENSOR_NUMBER == 1 :
    pirPin =7
elif SENSOR_NUMBER == 2 :
    pirPin = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)

timelaps=1
timeidx=0
timeInterval=20 #base second is 4 sec. 
threshold=4  #total count 4s/timelaps
detectCnt=0


# 함수 정의
def logprint(outStr):
    with open("ajoah_toilet_monitor.log","a") as f:
        strTMP = '['+getSysDt()+']['+str(SENSOR_NUMBER)+']'+outStr+'\n'
        f.write(strTMP)
        if isTest:
            print(strTMP,end='')

# Main

# 1. 화장실 ID / Name 가져오기 
toiletID=''
toiletName=''
testIDX=0  #Test var
with open("toiletInfo"+str(SENSOR_NUMBER), "r") as f:
    data = f.read().split('\n')
    print
    for idx in range(len(data)):
        if idx==0:
            logprint('id'+data[idx].split('\"')[1])
            toiletID=data[idx].split('\"')[1]
        elif idx==1:
            logprint('name'+data[idx].split('\"')[1])
            toiletName=data[idx].split('\"')[1]

# 2. 실행
while True:
    #1. init
    detectCnt=0
    for i in range(int(timeInterval/timelaps)):
        if isTest:
            print('['+str(timeidx*timelaps), end=']')
            logprint('['+str(timeidx*timelaps)+']')
        if GPIO.input(pirPin) == True:
            logprint("Motion detected!")
            detectCnt+=1
        #else:
            #logprint(" ")
        sleep(timelaps)
        timeidx+=1
        
    #logprint('detectCnt ['+str(detectCnt)+']')
    #logprint('threshold ['+str(threshold)+']')


    if detectCnt > threshold :
        logprint('this is Human')
        logprint('UseSpace')
        useSpace(toiletID)
    else :
        logprint('notUseSpace')
        notUseSpace(toiletID)


