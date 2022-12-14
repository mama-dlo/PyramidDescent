from os import environ, path

basedir = path.abspath(path.dirname(__file__))

SECRET_KEY = environ.get('SECRET_KEY')
DATABASE_URI = ''
UPLOAD_FOLDER = './static/io/'
class ProdConfig:
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''

class DevConfig:
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''