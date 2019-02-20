import bcrypt


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
        # token = self.encode_auth_token(10)
        return 10

    def get_user_by_username(self, username):
        password = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return {'username': username, 'uid': 1, 'password': password}
