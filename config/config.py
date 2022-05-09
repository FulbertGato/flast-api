import os
import pymysql
SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SESSION_TYPE = 'redis'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://doadmin:AVNS_3we2TEfqWuCAQSQ@flask-api-db-do-user-11003527-0-ddc9.b.db.ondigitalocean.com:25060/defaultdb'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/python_flask_online_food_ordering'
SQLALCHEMY_TRACK_MODIFICATIONS = False