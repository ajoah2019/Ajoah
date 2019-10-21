import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
import time

# Use a service account
cred = credentials.Certificate('ajoah_key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

initState=True
statSpace= False

print('statSpace 초기값 : ',statSpace)
print('initState 초기값 : ',initState)

def getTimeStamp():
    return int(str(time.time()).split('.')[0])

def getSysDt():
    return datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y-%m-%d %H:%M:%S')

def getTimeLaps(pre, now):    
    return str(datetime.strptime(now, '%Y-%m-%d %H:%M:%S') - datetime.strptime(pre, '%Y-%m-%d %H:%M:%S'))

def useSpace(toiletID, toiletName):
    global statSpace, initState
    if initState:
        statSpace= db.collection('current').document(toiletID).get().to_dict()['using']
        
    if statSpace:
        print('같은 상태값')
        return -1
    
    # 공통 변수
    sysDt = getSysDt()
    sysTstmp = getTimeStamp()
    toiletGrp = '.'.join(toiletID.split('.')[:2])
    
    # 사용하는 데이터 전송
    doc_col = db.collection('current')
    doc_ref_current=doc_col.document(toiletID)

    dataTmp={
        'timestamp' : sysTstmp,
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
    statSpace=True

    
def notUseSpace(toiletID, toiletName):
    global statSpace, initState
    if initState:
        statSpace= db.collection('current').document(toiletID).get().to_dict()['using']
        
    if not(statSpace):
        print('같은 상태값')
        return -1
    
    # 공통 변수
    sysDt = getSysDt()
    sysTstmp = getTimeStamp()
    toiletGrp = '.'.join(toiletID.split('.')[:2])
    
    # 사용하는 데이터 전송
    doc_col = db.collection('current')
    doc_ref_current=doc_col.document(toiletID)
    
    doc_ref_current_R = doc_ref_current.get().to_dict()
    dataTmp={
        'timestamp' : sysTstmp,
        'group' : toiletGrp,
        'id' : toiletID,
        'name' : toiletName,
        
        'using' : False,
        'free_from': sysDt,
        
        'last_update' : sysDt
    }
    doc_ref_current.set(dataTmp,merge=True)
    print(dataTmp)
    
    # 사용중이면 히스토리 저장 & 화장실 사용 횟수 추가
    state = doc_ref_current_R['using']
    if state == True:
        # 히스토리 저장 
        usingFrom = doc_ref_current_R['using_from']
        
        doc_ref_history = db.collection('history').document(getSysDt()+'-'+toiletID)
        dataTmp = {
            'timestamp' : sysTstmp,
            'id' : toiletID,
            'name' : toiletName,
            'using_from': usingFrom,
            'using_to': sysDt, 
            'using_elapsed' : getTimeLaps(usingFrom, sysDt)
        }
        doc_ref_history.set(dataTmp)
        print(dataTmp)
        
        # 화장실 사용 횟수 추가
        dateKey=sysDt[:10]
        db_ref= db.collection('statics').document(dateKey)
        db_data = db_ref.get().to_dict()

        print(db_data)
        if db_data == None:
            print('새로운 document key 생성') 
            dataTmp = {
                    toiletID : 1
            }
            print(dataTmp)
            db_ref.set(dataTmp,merge=True)
            return 

        try :
            cnt = db_data[toiletID]
        except Exception as ex:
            print('키 에러가 발생 했습니다', ex)
            dataTmp = {
                toiletID : 1
            }
            print(dataTmp)
            db_ref.set(dataTmp,merge=True)
            return 
        else:
            print('+1 수행') 
            dataTmp = {
                toiletID : cnt+1
            }
            print(dataTmp)
            db_ref.set(dataTmp,merge=True)
            return 
    
    statSpace=False


    
