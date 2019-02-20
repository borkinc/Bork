import os


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'bork_bork')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'bork_bops')
    DEBUG = True
    ENV = 'development'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


class ProductionConfig(BaseConfig):
    SECRET_KEY = 'bork_bork'
    JWT_SECRET_KEY = 'bork_bops'
    DEBUG = False
    ENV = 'production'
