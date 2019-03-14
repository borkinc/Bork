import os
from urllib.parse import urlparse


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'bork_bork')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'bork_bops')
    DATABASE_URL = os.getenv('DATABASE_URL')
    DEBUG = True
    ENV = 'development'

    url = urlparse(os.environ['DATABASE_URL'])
    DBNAME = url.path[1:]
    USER = url.username
    PASSWORD = url.password
    HOST = url.hostname
    PORT = url.port


class ProductionConfig(BaseConfig):
    SECRET_KEY = 'bork_bork'
    JWT_SECRET_KEY = 'bork_bops'
    DEBUG = False
    ENV = 'production'
