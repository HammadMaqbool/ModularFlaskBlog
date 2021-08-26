from flask import request
from blog import db
from blog.models.model_contact import Contact
from datetime import datetime

class GetContactData:
    def GetFormDatatoSave(self):
        name = request.form['name']
        email = request.form['email']
        phoneNumber = request.form['phone']
        message = request.form['msg']
        DateOfMessage = datetime.now()
        forTheDb = Contact(name=name, email=email, phone=phoneNumber, msg=message, myDate=DateOfMessage)
        db.session.add(forTheDb)
        db.session.commit()
