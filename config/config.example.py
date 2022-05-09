import os
import pymysql
SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SESSION_TYPE = 'redis'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://doadmin:AVNS_IulpPOvonyP84Sy@test-python-api-db:25060/defaultdb'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost:3306/dbname'
SQLALCHEMY_TRACK_MODIFICATIONS = False