import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('helloworldfirebase-2794d-firebase-adminsdk-uzee1-c9b122e44c.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://helloworldfirebase-2794d.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('') #ต้องใส่ path ให้ถูก

hopper_ref = ref.child('Users/-MHv9zWM9jTaEgWqICeb')
hopper_ref.delete()
print(ref.get())
#print(type(ref.get()))

#set	Write or replace data to a defined path, like messages/users/<username>
#update	Update some of the keys for a defined path without replacing all of the data
#push	Add to a list of data in the database. Every time you push a new node onto a list, your database generates a unique key, like messages/users/<unique-user-id>/<username>
#transaction	Use transactions when working with complex data that could be corrupted by concurrent updates
