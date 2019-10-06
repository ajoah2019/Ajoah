from dbAjoah import *
import time

# 1. 화장실 ID / Name 가져오기 
toiletID=''
toiletName=''
testIDX=0  #Test var
with open("toiletInfo.txt", "r") as f:
    data = f.read().split('\n')
    print
    for idx in range(len(data)):
        if idx==0:
            print('id: '+data[idx].split('\"')[1])
            toiletID=data[idx].split('\"')[1]
        elif idx==1:
            print('name: '+data[idx].split('\"')[1])
            toiletName=data[idx].split('\"')[1]

# MockUp.py
idxCnt=0
while True:
    #1. init
    if idxCnt % 2 == 0 :
        print('UseSpace')
        useSpace(toiletID, toiletName)
        time.sleep(5)
    else :
        print('notUseSpace')
        notUseSpace(toiletID, toiletName)
    idxCnt+=1
    time.sleep(5)
    
