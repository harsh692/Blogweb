## Under blog_main/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

import sqlalchemy

app=Flask(__name__)


############################
####### DATABASE SETUP #####
############################

basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = sqlalchemy(app)
Migrate(app,db)

############################

############################
##### LOGIN CONFIGURATIONS ##
##########################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


##########################

from blog_main.core.views import core
app.register_blueprint(core)

from blog_main.error_pages.handlers import error_pages
app.register_blueprint(error_pages)

from blog_main.users.views import users
app.register_blueprint(users)