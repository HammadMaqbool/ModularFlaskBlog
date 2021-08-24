from datetime import datetime
from enum import unique
from blog import db
from datetime import datetime 

#name, email, phone, msg, myDate
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=False, nullable=True)
    email = db.Column(db.String(50), unique=False ,nullable=True)
    phone = db.Column(db.String(50), unique=True, nullable=True)
    msg = db.Column(db.String(200), unique=True, nullable=True)
    myDate = db.Column(db.String(60), unique=False, nullable=True)
    

