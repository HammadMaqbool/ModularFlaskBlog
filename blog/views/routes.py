from datetime import datetime
from operator import pos
import re
from sys import path_hooks
from flask import Blueprint, request, session
from flask.templating import render_template
from sqlalchemy.orm import joinedload
from werkzeug.utils import redirect, secure_filename
from blog.models.model_contact import Contact
from blog.models.model_posts import Posts
from blog import db
import json
from blog.controllers.getContact import GetContactData
import os


with open('blog/config.json','r') as JsonOnView:
    LoadedJson = json.load(JsonOnView)['params']

routes_blueprint = Blueprint('routes_blueprint',__name__)

FILE_PATH = "C:\\Users\\Hammad Maqbool\\Desktop\\MyCloud\\ModularFlaskBlog\\blog\\static"


@routes_blueprint.route('/index')
@routes_blueprint.route('/index/page/<int:page>')
@routes_blueprint.route('/')
def home(page=1):
    post = Posts.query.paginate(page, per_page=2)
    return render_template('index.html', JinjaParam= LoadedJson, posts = post)



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
    return render_template('about.html', JinjaParam = LoadedJson)



@routes_blueprint.route('/admin_board', methods=['GET','POST'])
def admin_dashboard():
    if 'user' in session and session['user']=='TRUE':
        return render_template('Admin/myPosts.html', JinjaParam=LoadedJson, posts=OnHomeShowPosts())

    if(request.method == 'POST'):
        email = request.form.get('email')
        password = request.form.get('password')
        if(email=='admin@admin' and password=='admin'):
            session['user']='TRUE'        
            return render_template('Admin/myPosts.html', JinjaParam=LoadedJson, posts=OnHomeShowPosts())
        else:
            return render_template('Admin/login.html')
    else:
        return render_template('Admin/login.html')



@routes_blueprint.route('/edit_post/<sno_of_post>', methods=['GET', 'POST'])
def EditPost(sno_of_post):
        if 'user' in session and session['user']=='TRUE':
            post = Posts.query.filter_by(sno=sno_of_post).first()
            if(request.method=="POST"):
                UpdateRecord = Posts.query.get_or_404(sno_of_post)
                UpdateRecord.title = request.form.get('title')
                UpdateRecord.slug = request.form.get('slug')
                UpdateRecord.content = request.form.get('content')
                UpdateRecord.date = request.form.get('date')
                db.session.commit()
                return redirect('/admin_board')
            else:
                return render_template('Admin/edit_post.html', posts = post)
        else:
            return render_template('Admin/login.html')



@routes_blueprint.route('/delete_post/<string:sno_to_delete>', methods=['GET','POST'])
def DeletePost(sno_to_delete):
    post = Posts.query.filter_by(sno=sno_to_delete).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/admin_board')



@routes_blueprint.route('/add_post', methods=['GET','POST'])
def Insert_post():
    if 'user' in session and session['user']=='TRUE':
        if(request.method == 'POST'):
            title = request.form.get('title')
            post_slug = request.form.get('slug')
            post_content = request.form.get('content')
            post_date = datetime.now()
            myFile = request.files['fileOne']
            myFile.save(os.path.join(FILE_PATH, secure_filename(myFile.filename)))
            Save_to_DB = Posts(title=title, slug=post_slug, content=post_content, date=post_date)
            db.session.add(Save_to_DB)
            db.session.commit()
            return redirect('/admin_board')
        else:
            return render_template('/Admin/add_post.html')
    else:
        return render_template('Admin/login.html')



#Methods to Work with the database. . . .
def OnHomeShowPosts():
    post = Posts.query.filter_by().all()[0:15]
    return post

