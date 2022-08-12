import pyrebase

config = {
  "apiKey": "AIzaSyCxmXRl93wpAo2SNh7bQixxSksq7py-69E",
  "authDomain": "smartcookie-test.firebaseapp.com",
  "databaseURL": "https://smartcookie-test-default-rtdb.firebaseio.com/",
  "storageBucket": "smartcookie-test.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

username = "user1"
user = db.child("users").child(username).get().val()
print(user["email"])

# call Drip API
