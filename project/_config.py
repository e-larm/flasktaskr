# project/_config.py
import os

# grab the folder where the script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
#USERNAME = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

# define the full path for the database 
DATABASE_PATH = os.path.join(basedir, DATABASE)

# Define the database uri to tell SQLAlchemy where to access the database.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH 