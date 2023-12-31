import os

SHORT_LINK_LENGTH = 6
SHORT_LINK_PATTERN = r'^[a-zA-Z0-9]*$'
SHORT_LINK_MAX_LENGTH = 16


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
