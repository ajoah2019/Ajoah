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


def useSpace(toiletID, toiletName):
    # 사용하는 데이터 전송
    doc_col = db.collection('current')
    #doc_ref_current=doc_col.document(toiletID)
    
    doc_col.add({
        'id' : toiletID,
        'name' : toiletName,
        'using' : True,
        'using_from':getSysDt(),
        'last_update' : getSysDt()
    })

    '''
    # 전송 후 결과값 저장
    docs = doc_col.stream()
    for doc in docs:
        print('{} => {}'.format(doc.id, doc.to_dict()))

    
    # 결과값 히스토리 저장
    
    doc_col = db.collection('history')
    doc_ref_history=doc_col.document(getSysDt()+'-'+toiletID)
    
    doc_ref_history.set({
        'id' : toiletID,
        'name' : toiletName,
        'using_from':getSysDt(),
        'last_update' : getSysDt()
    })
    '''
    
def notUseSpace(toiletID, toiletName):
    # 사용하는 데이터 전송
    doc_col = db.collection('current')
    #doc_ref_current=doc_col.document(toiletID)
    
    doc_col.add({
        'id' : toiletID,
        'name' : toiletName,
        'using' : False,
        'free_from':getSysDt(),
        'last_update' : getSysDt()
    })
    '''
    # 전송 후 결과값 저장
    docs = doc_col.stream()

    # 결과값 히스토리 저장 
    ref = db.reference('history/'+toiletID)
    ref.update({
            getSysDt()+'-'+toiletID :toilet_status
    })
    '''
