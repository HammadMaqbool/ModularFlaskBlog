from enum import unique
from blog import db
from datetime import datetime

#Columns coming From the database are. . . as follow
#sno, title, slug, content and date
class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False, unique=False)
    slug = db.Column(db.String(50), nullable=False, unique=True)
    content = db.Column(db.String(), nullable=False, unique=True)
    date = db.Column(db.String(50), nullable=False, unique=True)