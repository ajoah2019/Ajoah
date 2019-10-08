import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('ajoah_key.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://ajoah-2121f.firebaseio.com/'
})

def getSysDt():
    return datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y-%m-%d %H:%M:%S')


def useSpace(toiletID, toiletName):
    # 사용하는 데이터 전송
    ref = db.reference('current/'+toiletID)
    ref.update({
        'name' : toiletName,
        'using' : True,
        'using_from':getSysDt(),
        'last_update' : getSysDt()
    })
    # 전송 후 결과값 저장 
    toilet_status=ref.get()

    # 결과값 히스토리 저장 
    ref = db.reference('history/'+toiletID)
    ref.update({
            getSysDt()+'-'+toiletID :toilet_status
    })
def notUseSpace(toiletID, toiletName):
    # 사용하는 데이터 전송
    ref = db.reference('current/'+toiletID)
    ref.update({
        'name' : toiletName,
        'using' : False,
        'free_from':getSysDt(),
        'last_update' : getSysDt()
    })
    # 전송 후 결과값 저장 
    toilet_status=ref.get()

    # 결과값 히스토리 저장 
    ref = db.reference('history/'+toiletID)
    ref.update({
            getSysDt()+'-'+toiletID :toilet_status
    })
