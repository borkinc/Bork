import datetime

import jwt


class UserHandler:

    def get_user(self, uid):
        return {'username': 'skiri', 'uid': uid}

    def get_contacts(self):
        pass

    def get_user_contacts(self, uid):
        pass

    def insert_user(self, username, email, password):
        """
        Should add user to database
        :param username: unique username
        :param email: email of user
        :param password: hashed password
        :return: user id from database
        """
        token = self.encode_auth_token(10)
        return 10, token

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        from app import app
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e
