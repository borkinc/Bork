import bcrypt as bcrypt
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource

from Handlers.Chat import ChatHandler
from Handlers.Users import UserHandler

app = Flask(__name__)
app.config.from_object('config.config.BaseConfig')
print(app.config['SECRET_KEY'])
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

DUMMY_DATA = {
    'register': {
        'username': 'test',
        'msg': 'success'
    },
    'login': {
        'is_authenticated': True
    }
}


@app.route('/', methods=['GET'])
def index():
    return jsonify(welcome='Hello World')


@app.route('/api/register', methods=['POST'])
def create_user():
    """
    Creates user with given username, email and password to be stored in database
    :return: json
    """
    if request.method == 'POST':
        username = 'new_user'
        email = 'new_user@bork.com'
        password = 'password'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user_id, token = UserHandler().insert_user(username=username, email=email, password=hashed_password)
        user = {'uid': user_id, 'username': username, 'auth': token.decode('utf-8'), 'msg': 'Success'}
        return jsonify(user=user), 201
    return jsonify(msg='Error'), 500


@app.route('/api/login', methods=['POST'])
def login():
    """

    :return:
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # get the user with this username
        return jsonify(user={'username': 'test'}, is_authenticated=True), 200


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


# @app.route('/api/chats', methods=['GET', 'POST'])
# def chats():
#     """
#     if method == GET
#     :return: All chats
#
#     if method == POST
#     send user id and chat name
#     :return:
#     """
#     if request.method == 'GET':
#         chats = [
#             {"id": 1, "chat_name": "skiribops"},
#             {"id": 2, "chat_name": "Subscribe to PewDiePie"},
#             {"id": 3, "chat_name": "DB"}
#         ]
#         return jsonify(results=chats), 200
#
#     elif request.method == 'POST':
#         chat_name = request.form['chat_name']
#         owner_id = request.form['uid']
#         return jsonify(chat={'id': 2, 'chat_name': chat_name}, msg='Success'), 201


# @app.route('/api/chats/<int:cid>', methods=['GET'])
# def chatByID(cid):
#     if request.method == 'GET':
#         return jsonify(chat={'id': cid, 'chat_name': 'skiribops'}), 200
#
#
# @app.route('/api/contacts/<int:uid>', methods=['GET', 'POST'])
# def contacts(uid):
#     """
#     if GET
#     :param uid: user id de quien quieres la lista
#     :return:
#
#     if POST
#     add a user to the contact del uid en el url
#     """
#     if request.method == 'GET':
#         return jsonify(contacts=[{'uid': 3}, {'uid': 4}]), 200
#     else:
#         uid_to_add = request.form['uid']
#         return jsonify(msg='added'), 201
#
#
# @app.route('/chats/<int:cid>/messages')
# def messages():
#     if request.method == 'GET':
#         return jsonify()
#     else:
#         # add message to chat
#         pass

# api.add_resource(User, '/user')
# api.add_resource(Chats, '/chats')
# api.add_resource(Chat, '/chat/<int:chat_id>')

if __name__ == '__main__':
    app.run(debug=True)
