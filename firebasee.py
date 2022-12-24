import time
import pyrebase

config = {
    "apiKey": "AIzaSyB1O_UBL7Au05qSQNUZP90OJYSgFrO0S7g",
    "authDomain": "projectesd-65cc2.firebaseapp.com",
    "databaseURL": "https://projectesd-65cc2-default-rtdb.firebaseio.com/",
    "storageBucket": "projectesd-65cc2.appspot.com"
}
# https://practice-48e2c-default-rtdb.asia-southeast1.firebasedatabase.app/
# https://console.firebase.google.com/project/projectesd-65cc2/database/projectesd-65cc2-default-rtdb/data

firebase = pyrebase.initialize_app(config)
db = firebase.database()

print("Send Data to Firebase Using Raspberry Pi")
print("—————————————-")
print()

while True:

    

    value_1 = db.child("phval").get().val()
    value_2 = db.child("tds").get().val()
    
    print(f"TDS: {value_2}")
    print(f"Ph Variable: {value_1}")

    time.sleep(2)