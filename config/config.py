import os


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'bork_bork')
    DEBUG = True
    ENV = 'development'


class ProductionConfig(BaseConfig):
    SECRET_KEY = 'bork_bork'
    DEBUG = False
