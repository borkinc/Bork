from flask import jsonify, request, current_app as app
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse

from Handlers.Chat import ChatHandler
from Handlers.Message import MessageHandler
from Handlers.Users import UserHandler

HELP_TEXT = 'This field cannot be blank'


class Index(Resource):

    def get(self):
        return jsonify(msg='Hello World')


class UserRegistration(Resource):

    def __init__(self):
        self.handler = UserHandler()

    def post(self):
        """
        Registers user to application.
        :return: JSON
        """

        # Arguments to be extracted from request
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP_TEXT, required=True)
        parser.add_argument('email', help=HELP_TEXT, required=True)
        parser.add_argument('password', help=HELP_TEXT, required=True)
        parser.add_argument('first_name', help=HELP_TEXT, required=True)
        parser.add_argument('last_name', help=HELP_TEXT, required=True)
        parser.add_argument('phone_number', help=HELP_TEXT, required=True)

        # Verifies required arguments are in request and extracts data into a dictionary
        data = parser.parse_args()
        response, status = self.handler.insert_user(data)
        return app.response_class(response=response, status=status, mimetype='application/json')


class UserLogin(Resource):

    def post(self):
        """
        Logs in existing user
        :return: JSON
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP_TEXT, required=True)
        parser.add_argument('password', help=HELP_TEXT, required=True)

        # Extracts data from request and verifies required data is available
        data = parser.parse_args()

        response, status = UserHandler().verify_password(data)
        return app.response_class(response=response, status=status, mimetype='application/json')


class Users(Resource):

    def __init__(self):
        self.handler = UserHandler()

    # @jwt_required
    def get(self):
        users = self.handler.get_users()
        return jsonify(users=users)

    # @jwt_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('new_username')
        data = parser.parse_args()
        if 'new_username' in data and data['new_username']:
            user = self.handler.update_user_username(username='ninja', new_username='Cherdleys')
            return jsonify(user=user)
        else:
            return jsonify(msg='Bad request')


class User(Resource):
    def __init__(self):
        self.handler = UserHandler()

    def get(self, user):
        if user.isdigit():
            _user = self.handler.get_user_by_id(user)
        else:
            _user = self.handler.get_user_by_username(user)
        return jsonify(user=user)


class Chats(Resource):

    def __init__(self):
        self.handler = ChatHandler()

    @jwt_required
    def get(self):
        response, status = self.handler.get_chats()
        return app.response_class(response=response, status=status, mimetype='application/json')

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('chat_name', help=HELP_TEXT, required=True)
        parser.add_argument('members')
        data = parser.parse_args()
        response, status = self.handler.insert_chat(data)
        return app.response_class(response=response, status=status, mimetype='application/json')

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
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', help=HELP_TEXT, required=True)
        parser.add_argument('last_name', help=HELP_TEXT, required=True)
        parser.add_argument('email', help=HELP_TEXT)
        parser.add_argument('phone_number', help=HELP_TEXT)
        data = parser.parse_args()
        return self.handler.insert_contact(data)

    # @jwt_required
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
        return self.handler.remove_contact(data)


class Contact(Resource):

    def __init__(self):
        self.handler = UserHandler()

    def get(self, uid):
        contacts = self.handler.get_contacts(uid)
        return jsonify(contacts=contacts)


class Chat(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('contact_id', help=HELP_TEXT, required=True)

    def get(self, cid):
        chat = ChatHandler().get_chat(cid)
        return jsonify(chat=chat)

    @jwt_required
    def post(self, cid):
        data = self.parser.parse_args()
        chat = ChatHandler().add_contact_to_chat_group(cid, data)
        return jsonify(chat=chat)

    @jwt_required
    def delete(self, cid):
        return ChatHandler().delete_chat(cid)


class ChatMembers(Resource):

    @jwt_required
    def get(self, cid):
        chat_members = ChatHandler().get_chat_members(cid)
        return jsonify(chat_members=chat_members)

    @jwt_required
    def post(self, cid):
        parser = reqparse.RequestParser()
        parser.add_argument('contact_id', help=HELP_TEXT, required=True)

        data = parser.parse_args()

        response, status = ChatHandler().add_contact_to_chat_group(cid, data)
        return app.response_class(response=response, status=status, mimetype='application/json')

    @jwt_required
    def delete(self, cid):
        parser = reqparse.RequestParser()
        parser.add_argument('contact_id', help=HELP_TEXT, required=True)

        data = parser.parse_args()

        response, status = ChatHandler().remove_contact_from_chat_group(cid, data)
        return app.response_class(response=response, status=status, mimetype='application/json')


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
        parser.add_argument('uid', help=HELP_TEXT, required=True)
        parser.add_argument('message', help=HELP_TEXT, required=True)
        data = parser.parse_args()
        if 'img' in request.files and request.files['img']:
            message = ChatHandler().insert_chat_message(cid=chat_id, username=get_jwt_identity(),
                                                        message=data['message'],
                                                        img=request.files['img'])
        else:
            message = ChatHandler().insert_chat_message(cid=chat_id, username=get_jwt_identity(),
                                                        message=data['message'])
        return jsonify(message=message)


class Messages(Resource):

    def __init__(self):
        self.handler = MessageHandler()

    def get(self):
        messages = self.handler.get_all_messages()
        return jsonify(messages=messages)


class Message(Resource):

    def __init__(self):
        self.handler = MessageHandler()

    def get(self, mid):
        message = self.handler.get_message(mid)
        return jsonify(message=message)


class LikeChatMessage(Resource):

    def __init__(self):
        self.handler = MessageHandler()

    def get(self, mid):
        likers = self.handler.get_likers(mid)
        return jsonify(likers=likers, likes=len(likers))

    @jwt_required
    def post(self, mid):
        message = self.handler.like_message(mid)
        return jsonify(message=message)


class DislikeChatMessage(Resource):

    def __init__(self):
        self.handler = MessageHandler()

    def get(self, mid):
        dislikers = MessageHandler().get_dislikers(mid)
        return jsonify(dislikers=dislikers, dislikes=len(dislikers))

    @jwt_required
    def post(self, mid):
        message = self.handler.dislike_message(mid)
        return jsonify(message=message)


class ReplyChatMessage(Resource):

    def __init__(self):
        self.handler = MessageHandler()

    def get(self, mid):
        replies = self.handler.get_replies(mid)
        return jsonify(replies=replies)

    @jwt_required
    def post(self, mid):
        parser = reqparse.RequestParser()
        parser.add_argument('message', help=HELP_TEXT, required=True)
        parser.add_argument('cid', help=HELP_TEXT, required=True)
        data = parser.parse_args()
        data['img'] = request.files['img'] or None
        response, status = ChatHandler().reply_chat_message(data, mid)
        return app.response_class(response=response, status=status, mimetype='application/json')


class TokenRefresh(Resource):

    # @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return jsonify(access_token=access_token)
