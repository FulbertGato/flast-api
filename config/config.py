import os
import pymysql
SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SESSION_TYPE = 'redis'
SQLALCHEMY_TRACK_MODIFICATIONS = False