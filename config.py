import os
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config :
    SECRET_KEY = "your-secre-key"
    SQLALCHEMY_DATABASE_URL = "sqlite:///" + os.path.join(BASE_DIR , "database.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False