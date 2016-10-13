# coding: utf-8
import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "adqacfsae4adasae23"
    DATABASE_URL = os.path.join(os.path.dirname(__file__),'app.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DATABASE_URL)
    CSRF_ENABLED = True
    BOWER_COMPONENTS_ROOT = '../bower_components'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # email server
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False 
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'shuric80@gmail.com'
    MAIL_PASSWORD = 'mvgdwssbsgugejoa'
    # administrator list
    ADMINS = ['shuric80@gmail.com']

    
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(BaseConfig):
    TESTING = True


class DebugConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

