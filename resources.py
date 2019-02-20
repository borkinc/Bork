import bcrypt
from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity
from flask_restful import Resource, reqparse

from Handlers.Chat import ChatHandler
from Handlers.Users import UserHandler


class Index(Resource):

    def get(self):
        return jsonify(msg='Hello World')


class UserRegistration(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='Username field cannot be blank', required=True)
        parser.add_argument('email', help='Email field cannot be blank', required=True)
        parser.add_argument('password', help='Password field cannot be blank', required=True)

        # Contains actual data
        data = parser.parse_args()

        # Dummy data for phase I of project
        username = 'new_user'
        email = 'new_user@bork.com'
        password = 'password'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user_id = UserHandler().insert_user(username=username, email=email, password=hashed_password)
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        user = {
            'uid': user_id,
            'username': username,
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return jsonify(user=user)


class UserLogin(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='Username field cannot be blank', required=True)
        parser.add_argument('password', help='Password field cannot be blank', required=True)
        data = parser.parse_args()
        username = 'skiri'
        password = 'password'
        user = UserHandler().get_user_by_username(username)
        is_authenticated = bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8'))
        if is_authenticated:
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            user = {
                'uid': user['uid'],
                'username': username,
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            user = {
                'msg': 'Invalid credentials'
            }
        return jsonify(user=user)


class Chats(Resource):

    def get(self):
        return ChatHandler().get_chats()

    def post(self):
        chat = {'id': 2, 'chat_name': 'Videout'}
        return jsonify(chat=chat, msg='Success')


class Chat(Resource):

    def get(self, chat_id):
        """
        Gets all messages from given chat id.
        :param chat_id: id of the chat messages are to be extracted from
        :return: JSON representation of messages table
        """
        return ChatHandler().get_chat(chat_id)


class ChatMessages(Resource):

    def get(self):
        pass


class TokenRefresh(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return jsonify(access_token=access_token)
