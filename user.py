
from mongoengine import connect, Document, StringField, DateTimeField, ListField        

class Users(Document):
    login = StringField(require=True, unique=True)
    senha = StringField(require=True)
        
    