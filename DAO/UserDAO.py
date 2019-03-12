import os
from urllib.parse import urlparse

import psycopg2

from config.config import BaseConfig


class UserDAO:

    def __init__(self):
        config = BaseConfig()

        self.conn = psycopg2.connect(dbname=config.DBNAME, user=config.USER, password=config.PASSWORD, host=config.HOST,
                                     port=config.PORT)

