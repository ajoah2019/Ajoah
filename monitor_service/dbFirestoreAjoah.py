import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime

# Use a service account
cred = credentials.Certificate('ajoah_key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()



def getSysDt():
    return datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y-%m-%d %H:%M:%S')

def getTimeLaps(pre, now):    
    return str(datetime.strptime(now, '%Y-%m-%d %H:%M:%S') - datetime.strptime(pre, '%Y-%m-%d %H:%M:%S'))

def useSpace(toiletID, toiletName):
    # 공통 변수 
    sysDt = getSysDt()
    toiletGrp = '.'.join(toiletID.split('.')[:2])
    
    # 사용하는 데이터 전송
    doc_col = db.collection('current')
    doc_ref_current=doc_col.document(toiletID)

    dataTmp={
        'group' : toiletGrp,
        'id' : toiletID,
        'name' : toiletName,
        'using' : True,
        'using_from': sysDt,
        'free_from':  None,
        'last_update' : sysDt
    }
    doc_ref_current.set(dataTmp,merge=True)
    print(dataTmp)

    
def notUseSpace(toiletID, toiletName):
    # 공통 변수 
    sysDt = getSysDt()
    toiletGrp = '.'.join(toiletID.split('.')[:2])
    
    # 사용하는 데이터 전송
    doc_col = db.collection('current')
    doc_ref_current=doc_col.document(toiletID)
    
    doc_ref_current_R = doc_ref_current.get().to_dict()
    dataTmp={
        'group' : toiletGrp,
        'id' : toiletID,
        'name' : toiletName,
        'using' : False,
        'free_from': sysDt,
        'last_update' : sysDt
    }
    doc_ref_current.set(dataTmp,merge=True)
    print(dataTmp)
    
    # 사용중이면 히스토리 저장 
    state = doc_ref_current_R['using']
    if state == True:
        usingFrom = doc_ref_current_R['using_from']
        
        doc_ref_history = db.collection('history').document(getSysDt()+'-'+toiletID)
        dataTmp = {
            'id' : toiletID,
            'name' : toiletName,
            'using_from': usingFrom,
            'using_to': sysDt, 
            'using_elapsed' : getTimeLaps(usingFrom, sysDt)
        }
        doc_ref_history.set(dataTmp)
        print(dataTmp)


    
