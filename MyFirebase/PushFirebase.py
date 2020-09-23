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
posts_ref = ref.child('users')

new_post_ref = posts_ref.push()
new_post_ref.set({
    'author': 'gracehop',
    'title': 'Announcing COBOL, a New Programming Language'
})

# We can also chain the two calls together
posts_ref.push().set({
    'author': 'alanisawesome',
    'title': 'The Turing Machine'
})

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())
print(type(ref.get()))