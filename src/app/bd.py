import pyrebase

config = {
    "apiKey": "AIzaSyA3oN-5MADuWKzjX-BVCGbQAbLPBJbDWl4",
    "authDomain": "signature-web-social-media.firebaseapp.com",
    "databaseURL": "https://signature-web-social-media.firebaseio.com",
    "projectId": "signature-web-social-media",
    "storageBucket": "signature-web-social-media.appspot.com",
    "messagingSenderId": "910948963145",
    "appId": "1:910948963145:web:c2687b5d40a910a5440098",
    "measurementId": "G-WC97S4G8VE"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

db.child("names").push({"name":"sera"})

