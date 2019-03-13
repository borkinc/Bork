

import psycopg2

from config.config import BaseConfig


class UserDAO:

    def __init__(self):
        config = BaseConfig()

        self.conn = psycopg2.connect(dbname=config.DBNAME, user=config.USER, password=config.PASSWORD, host=config.HOST,
                                     port=config.PORT)

    def insert_user(self, username, password, first_name, last_name, email, phone_number):
        cursor = self.conn.cursor()
        query = "insert into users (username, password, first_name, last_name, email, phone_number) " \
                "values ('%s','%s','%s','%s','%s','%s') returning uid" % (username, password, first_name, last_name, email, phone_number)
        cursor.execute(query)
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid
