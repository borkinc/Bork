import os
from urllib.parse import urlparse


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'bork_bork')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'bork_bops')


class DevelopmentConfig(BaseConfig):
    DATABASE = {
        'DBNAME': 'Bork',
        'USER': 'borkuser',
        'PASSWORD': 'borkuser!@',
        'HOST': 'localhost',
        'PORT': '5432'
    }
    DEBUG = True
    ENV = 'development'


class ProductionConfig(BaseConfig):
    DATABASE_URL = os.getenv('DATABASE_URL')
    url = urlparse(DATABASE_URL)
    DATABASE = {
        'DBNAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port
    }
    CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')
    API_KEY = os.getenv('CLOUDINARY_API_KEY')
    API_SECRET = os.getenv('CLOUDINARY_API_SECRET')
    DEBUG = False
    ENV = 'production'
