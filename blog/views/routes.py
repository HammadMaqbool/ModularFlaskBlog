from datetime import datetime
import re
from sys import path_hooks
from flask import Blueprint, request
from flask.templating import render_template
from blog.models.model_contact import Contact
from blog import db

routes_blueprint = Blueprint('routes_blueprint',__name__)

@routes_blueprint.route('/index')
@routes_blueprint.route('/')
def home():
    return render_template('index.html')

@routes_blueprint.route('/post')
def post():
    return render_template('post.html')

@routes_blueprint.route('/contact',  methods=['POST','GET'])
def contact():
    if(request.method == 'POST'):
        name = request.form['name']
        email = request.form['email']
        phoneNumber = request.form['phone']
        message = request.form['msg']
        DateOfMessage = datetime.now()
        forTheDb = Contact(name=name, email=email, phone=phoneNumber, msg=message, myDate=DateOfMessage)
        db.session.add(forTheDb)
        db.session.commit()
        return render_template('contact.html')
    else:
        return render_template('contact.html')

@routes_blueprint.route('/about')
def about():
    return render_template('about.html')
