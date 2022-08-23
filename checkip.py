import threading

from requests import get
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time


cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

callback_done = threading.Event()

def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        if doc.id == "home_information":
            print("Request Recieve")
            doc_dict = doc.to_dict()
            ip = get('https://api.ipify.org').text
            if doc_dict['flag'] == True:
                doc_ref.set({
                    u'ip': ip,
                    u'flag': False,
                })
                print("Set new IP:" + str(ip) + " to home_information document")
            print("IP Changed by another Admin")


    callback_done.set()

doc_ref = db.collection(u'home').document(u'home_information')

# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)

while True:
    pass