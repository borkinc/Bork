

import psycopg2
import psycopg2.extras

from DAO.DAO import DAO


class UserDAO(DAO):

    def insert_user(self, username, password, first_name, last_name, email, phone_number):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "insert into users (username, password, first_name, last_name, email, phone_number) " \
                "values (%s,%s,%s,%s,%s,%s) returning uid"
        cursor.execute(query, (username, password, first_name, last_name, email, phone_number, ))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def get_all_users(self):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "select username, first_name, last_name, email, phone_number from users;"
        cursor.execute(query)
        users = [row for row in cursor]
        return users

