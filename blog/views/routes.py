from datetime import datetime
import re
from sys import path_hooks
from flask import Blueprint, request
from flask.templating import render_template
from blog.models.model_contact import Contact
from blog.models.model_posts import Posts
from blog import db
import json
from blog.controllers.getContact import GetContactData

with open('blog/config.json','r') as JsonOnView:
    LoadedJson = json.load(JsonOnView)['params']

routes_blueprint = Blueprint('routes_blueprint',__name__)

@routes_blueprint.route('/index')
@routes_blueprint.route('/')
def home():
    return render_template('index.html', JinjaParam= LoadedJson)


@routes_blueprint.route('/post/<slug_of_post>')
def post(slug_of_post):
    myPostData = Posts.query.filter_by(slug=slug_of_post).first()
    return render_template('post.html', postData = myPostData, JinjaParam= LoadedJson)


@routes_blueprint.route('/contact',  methods=['POST','GET'])
def contact(): 
    if(request.method == 'POST'):
        #Coded a class in Controler folder and all the code to save the data into the database is there. . .
        var = GetContactData()
        var.GetFormDatatoSave()
        return render_template('contact.html', JinjaParam= LoadedJson)
    else:
        return render_template('contact.html', JinjaParam= LoadedJson)

@routes_blueprint.route('/about')
def about():
    return render_template('about.html')



#Methods to Work with the database. . . .

