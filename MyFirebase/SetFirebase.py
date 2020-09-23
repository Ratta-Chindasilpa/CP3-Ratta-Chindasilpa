import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('helloworldfirebase-2794d-firebase-adminsdk-uzee1-c9b122e44c.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://helloworldfirebase-2794d.firebaseio.com/'
})

# Get a database reference to our posts
ref = db.reference('') ##ต้องใส่ path ให้ถูก
users_ref = ref.child('users')
users_ref.set({
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
    'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
})

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())
print(type(ref.get()))