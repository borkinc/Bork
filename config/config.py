import os


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'bork_bork')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'bork_bops')
    DEBUG = True
    ENV = 'development'


class ProductionConfig(BaseConfig):
    SECRET_KEY = 'bork_bork'
    JWT_SECRET_KEY = 'bork_bops'
    DEBUG = False
    ENV = 'production'
