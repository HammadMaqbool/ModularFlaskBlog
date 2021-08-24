from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/thecleandb'

db = SQLAlchemy(app)

from blog.views.routes import routes_blueprint
app.register_blueprint(routes_blueprint)