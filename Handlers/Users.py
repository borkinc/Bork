import datetime

import bcrypt
from dateutil.relativedelta import relativedelta
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, create_access_token, create_refresh_token

from DAO.UserDAO import UserDAO


class UserHandler:

    def __init__(self):
        self.password = 'password'
        self.first_name = 'first_name'
        self.last_name = 'last_name'
        self.email = 'email'
        self.phone = '7875555555'
        self.dao = UserDAO()

    def get_users(self):
        return self.dao.get_all_users()

    def get_user_by_username(self, username):
        return self.dao.get_user_by_username(username)

    def get_user_by_id(self, uid):
        return self.dao.get_user(uid)

    def get_contacts(self, user_id):
        return self.dao.get_contacts(user_id)

    def insert_contact(self, data):
        owner_username = get_jwt_identity()
        owner_user = self.dao.get_user_by_username(owner_username)['uid']
        try:
            first_name = data['first_name']
            last_name = data['last_name']
        except KeyError:
            return jsonify(msg='Missing parameters')
        try:
            if 'phone' in data:
                contact_to_add = self.dao.get_user_by_phone_number(data['phone_number'])['uid']
            elif 'email' in data:
                contact_to_add = self.dao.get_user_by_email(data['email'])['uid']
            else:
                return jsonify(msg='Missing parameters')
        except IndexError:
            return jsonify(msg='User does not exist')
        self.dao.insert_contact(owner_user, contact_to_add, first_name, last_name)
        return jsonify(msg="Success")

    def update_contact(self, contact_id):
        contact = {
            'contact_id': 3,
            'uid': 4
        }
        return contact

    def insert_user(self, data):

        username = data['username']
        email = data['email']
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']
        phone_number = data['phone_number']

        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username, expires_delta=datetime.timedelta(days=365))
        uid = self.dao.insert_user(username, password, first_name, last_name, email, phone_number)
        user = {
            'uid': uid,
            'username': username,
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return jsonify(user=user)

    def verify_password(self, username, password):
        user = self.userDAO.get_user_by_username(username)
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

