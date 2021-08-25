from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

with open('config.json','r') as jsonFile:
    JsonData = json.load(jsonFile)['params']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = JsonData['local_uri']

db = SQLAlchemy(app)

from blog.views.routes import routes_blueprint
app.register_blueprint(routes_blueprint)