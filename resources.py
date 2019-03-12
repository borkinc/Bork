import datetime

import bcrypt
from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity, \
    jwt_required
from flask_restful import Resource, reqparse

from Handlers.Chat import ChatHandler
from Handlers.Users import UserHandler

HELP_TEXT = 'This field cannot be blank'


class Index(Resource):

    def get(self):
        return jsonify(msg='Hello World')


class UserRegistration(Resource):

    def post(self):
        """
        Registers new user
        :return: JSON
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP_TEXT, required=True)
        parser.add_argument('email', help=HELP_TEXT, required=True)
        parser.add_argument('password', help=HELP_TEXT, required=True)

        # Verifies needed parameters to register users are present
        data = parser.parse_args()

        # Dummy data for phase I of project
        username = 'new_user'
        email = 'new_user@bork.com'
        password = 'password'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        uid = UserHandler().insert_user(username=username, email=email, password=hashed_password)
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        user = {
            'uid': uid,
            'username': username,
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return jsonify(user=user)


class UserLogin(Resource):

    def post(self):
        """
        Logs in existing user
        :return: JSON
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP_TEXT, required=True)
        parser.add_argument('password', help=HELP_TEXT, required=True)

        # Verifies needed parameters to register users are present
        data = parser.parse_args()

        # Dummy data for Phase I
        username = 'ninja'
        password = 'password'
        user, is_authenticated = UserHandler().verify_password(username, password)
        if is_authenticated:

            # TODO: Remove expires_delta after Phase I
            access_token = create_access_token(identity=username, expires_delta=datetime.timedelta(days=365))
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
        return jsonify(user=user, is_authenticated=is_authenticated)


class Users(Resource):

    def __init__(self):
        self.handler = UserHandler()

    @jwt_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        data = parser.parse_args()
        if 'username' in data and data['username']:
            users = self.handler.get_user(username='ninja')
        else:
            users = self.handler.get_users()
        return jsonify(users=users)

    @jwt_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('new_username')
        data = parser.parse_args()
        if 'new_username' in data and data['new_username']:
            user = self.handler.update_user_username(username='ninja', new_username='Cherdleys')
            return jsonify(user=user)
        else:
            return jsonify(msg='Bad request')


class Chats(Resource):

    @jwt_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('cid')
        data = parser.parse_args()
        if 'cid' in data and data['cid']:
            chats = ChatHandler().get_chat(data['cid'])
        else:
            chats = ChatHandler().get_chats()
        return jsonify(chats=chats)

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('chat_name', help=HELP_TEXT, required=True)
        data = parser.parse_args()
        if 'chat_name' in data and data['chat_name']:
            chat_name = 'Videout'
            chat = ChatHandler().insert_chat(chat_name)
            msg = 'Success'
        else:
            chat = 'N/A'
            msg = 'Bad request'
        return jsonify(chat=chat, msg=msg)

    @jwt_required
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('cid')
        data = parser.parse_args()
        chat = ChatHandler().remove_chat(cid=1)
        return jsonify(chat=chat, msg='Successfully removed chat')



class Contacts(Resource):

    def __init__(self):
        self.handler = UserHandler()

    @jwt_required
    def get(self):
        """
        Retrieves all contacts from database
        :return: JSON
        """
        parser = reqparse.RequestParser()
        parser.add_argument('uid', help=HELP_TEXT, required=True)
        data = parser.parse_args()
        contacts = self.handler.get_contacts(1)
        return jsonify(contacts=contacts)

    @jwt_required
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('first_name', help=HELP_TEXT, required=True)
        parser.add_argument('last_name', help=HELP_TEXT, required=True)
        parser.add_argument('email', help=HELP_TEXT)
        parser.add_argument('phone', help=HELP_TEXT)
        data = parser.parse_args()
        if 'email' in data and data['email']:
            contact = self.handler.insert_contact(first_name='first', last_name='last', email='email@email.com')
        elif 'phone' in data and data['phone']:
            contact = self.handler.insert_contact(first_name='first', last_name='last', phone='7875555555')
        else:
            return jsonify(msg='Bad request')
        return jsonify(contact=contact)

    @jwt_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('contact_id', help=HELP_TEXT, required=True)
        data = parser.parse_args()
        contact = self.handler.update_contact(1)
        return jsonify(contact=contact)

    @jwt_required
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('contact_id', help=HELP_TEXT, required=True)
        data = parser.parse_args()
        contact = self.handler.remove_contact(1)
        return jsonify(contact=contact)


class Chat(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('contact_id', help=HELP_TEXT, required=True)

    @jwt_required
    def post(self, cid):
        data = self.parser.parse_args()
        chat = ChatHandler().add_contact_to_chat_group(1)
        return jsonify(chat=chat)

    @jwt_required
    def delete(self, cid):
        data = self.parser.parse_args()
        chat = ChatHandler().remove_contact_from_chat_group(1)
        return jsonify(chat=chat)


class ChatMessages(Resource):

    @jwt_required
    def get(self, chat_id):
        """
        Gets all messages from given chat id.
        :param chat_id: id of the chat messages are to be extracted from
        :return: JSON representation of messages table
        """
        messages = ChatHandler().get_chat_messages(chat_id)
        return jsonify(messages=messages)

    @jwt_required
    def post(self, chat_id):
        parser = reqparse.RequestParser()
        parser.add_argument('message', help=HELP_TEXT, required=True)
        parser.add_argument('img')
        data = parser.parse_args()
        message = ChatHandler().insert_chat_message(message='message',
                                                    img='/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png')
        return jsonify(message=message)


class LikeChatMessage(Resource):

    @jwt_required
    def post(self, chat_id, message_id):
        message = ChatHandler().like_chat_message(chat_id=1, message_id=1)
        return jsonify(message=message)


class DislikeChatMessage(Resource):

    @jwt_required
    def post(self, chat_id, message_id):
        message = ChatHandler().dislike_chat_message(chat_id=1, message_id=1)
        return jsonify(message=message)


class ReplyChatMessage(Resource):

    @jwt_required
    def post(self, chat_id, message_id):
        parser = reqparse.RequestParser()
        parser.add_argument('message', help=HELP_TEXT, required=True)
        parser.add_argument('img')
        data = parser.parse_args()
        message = ChatHandler().reply_chat_message(chat_id=1, message_id=1, message='reply')
        return jsonify(message=message)


class TokenRefresh(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return jsonify(access_token=access_token)