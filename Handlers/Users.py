import datetime

import bcrypt
from dateutil.relativedelta import relativedelta
from flask import jsonify

from DAO.UserDAO import UserDAO


class UserHandler:

    def __init__(self):
        self.password = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.first_name = 'first_name'
        self.last_name = 'last_name'
        self.email = 'email'
        self.phone = '7875555555'
        self.dao = UserDAO()

    def get_users(self):
        users = [
            {
                'uid': 1,
                'username': 'ninja',
                'password': self.password,
                'email': self.email,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'phone': self.phone
            },
            {
                'uid': 2,
                'username': 'pewdiepie',
                'password': self.password,
                'email': self.email,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'phone': self.phone
            },
            {
                'uid': 3,
                'username': 'markiplier',
                'password': self.password,
                'email': self.email,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'phone': self.phone
            }
        ]
        return users

    def get_user_by_username(self, username):
        user = {
            'uid': 1,
            'username': 'ninja',
            'password': self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone
        }
        return user

    def get_user_by_id(self, uid):
        return self.dao.get_user(uid)

    def get_contacts(self, user_id):
        return self.dao.get_contacts(user_id)

    def insert_contact(self, first_name, last_name, email=None, phone=None):
        contact = {
            'contact_id': 3,
            'uid': 4
        }
        return contact

    def update_contact(self, contact_id):
        contact = {
            'contact_id': 3,
            'uid': 4
        }
        return contact

    def insert_user(self, username, email, password):
        """
        Should add user to database
        :param username: unique username
        :param email: email of user
        :param password: hashed password
        :return: user id from database
        """
        # token = self.encode_auth_token(10)
        return 10

    def get_user_by_username(self, username):
        # TODO: Method should be something along the lines of verify_user_password
        password = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return {'username': username, 'uid': 1, 'password': password}

    def verify_password(self, username, password):
        user = self.get_user(username)
        is_authenticated = bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8'))
        return user, is_authenticated

    def update_user_username(self, username, new_username):
        user = self.get_user(username)
        user['username'] = new_username
        return user

    def remove_contact(self, contact_id):
        contact = {
            'contact_id': 3,
            'uid': 4
        }
        return contact

    def get_daily_active_users(self):
        today = datetime.datetime.today()
        users = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_daily_active_users(day_to_get)
            users.append({'%s' % day_to_get: num})
        return jsonify(result=users)

    def get_num_messages_user(self, uid):
        today = datetime.datetime.today()
        num_messages = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_daily_messages_user(uid, day_to_get)
            num_messages.append({'%s' % day_to_get: num})
        return jsonify(result=num_messages)

