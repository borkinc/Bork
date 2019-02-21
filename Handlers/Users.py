import bcrypt
from flask import jsonify


class UserHandler:

    def get_user(self, request):
        return jsonify(user={'username': request.form['username']})

    def get_contacts(self, request):
        contacts = [
            {'cid': 3, 'uid': 4}
        ]
        return contacts

    def insert_contact(self, request):
        pass

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
