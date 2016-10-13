# -*- coding:utf-8 -*-

import os
import sys
from flask import Flask, render_template

from flask_bower import Bower
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager
from flask_script.commands import ShowUrls, Clean
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flaskext.markdown import Markdown
from flask_debugtoolbar import DebugToolbarExtension
import flask_login as login
from extlog import logger


app = Flask(__name__, template_folder='../src/templates')

app.config.from_object('config.DebugConfig')

Markdown(app)

db = SQLAlchemy(app)

mail = Mail(app)

Bower(app)

bcrypt = Bcrypt(app)


#debug_toolbar = DebugToolbarExtension(app) if app.config['DEBUG'] else None


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(SuperUser).get(user_id)

init_login()

from app.gallery.admin import CustomAdminIndexView

admin = Admin( app, name='event', \
               base_template = 'master.html', \
               index_view=CustomAdminIndexView())

from app.gallery.admin import AdminView, UserView, \
    ContentView, MailView

from app.gallery.models import SuperUser, User, \
    Content, Mail

admin.add_view(AdminView(SuperUser, db.session))
admin.add_view(UserView(User, db.session))
admin.add_view(ContentView(Content, db.session))   
admin.add_view(MailView(Mail, db.session))


"""
    GENERATE SECRET KEY
   """

def install_secret_key(app, filename="secret_key"):
    filename = os.path.join(app.instance_path, filename)
    print filename
    try:
        app.config['SECRET_KEY'] = open(filename, 'r').read()
    except IOError:
        logger.error('Error: No secret key.Create it with:')
        full_path = os.path.dirname(filename)
        if not os.path.dirname(full_path):
            print ('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
            sys.exit(1)

            
if not app.config['DEBUG']:
    install_secret_key(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    logger.info('index')
    return render_template('index.html')


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('shell', Shell(make_context=lambda: {'app': app}))
manager.add_command('db', MigrateCommand)
manager.add_command('show-urls', ShowUrls)
manager.add_command('clean', Clean)

#from app.gallery.views import *

from app.gallery.views import mod as event
app.register_blueprint(event)

from app.gallery.models import SuperUser
