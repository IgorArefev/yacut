import os

SHORT_LINK_LENGTH = 6
SHORT_LINK_PATTERN = r'^[a-zA-Z0-9]*$'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
