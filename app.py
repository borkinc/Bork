import bcrypt as bcrypt
from flask import Flask, request, jsonify

from Handlers.Chat import ChatHandler
from Handlers.Users import UserHandler

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register', methods=['POST'])
def create_user():
    """
    Should create user
    :return: json containing username and success
    """
    if request.method == 'POST':
        return UserHandler().insert_user(request), 201
    return jsonify(msg='Error'), 500


@app.route('/login', methods=['POST'])
def login():
    """

    :return:
    """
    if request.method == 'POST':
        return UserHandler().get_user(request), 200


@app.route('/chats', methods=['GET', 'POST'])
def chats():
    """
    if method == GET
    :return: All chats

    if method == POST
    send user id and chat name
    :return:
    """
    if request.method == 'GET':
        return ChatHandler().get_chats(request), 200

    elif request.method == 'POST':
        return ChatHandler().insert_chat(request), 201


@app.route('/chats/<int:cid>', methods=['GET'])
def chatByID(cid):
    if request.method == 'GET':
        return ChatHandler().get_chat(request), 200


@app.route('/contacts/<int:uid>', methods=['GET', 'POST'])
def contacts(uid):
    """
    if GET
    :param uid: user id de quien quieres la lista
    :return:

    if POST
    add a user to the contact del uid en el url
    """
    if request.method == 'GET':
        return UserHandler().get_contacts(request), 200
    else:
        uid_to_add = request.form['uid']
        return UserHandler().insert_contact(request), 201

@app.route('/chats/<int:cid>/messages')
def messages():
    if request.method == 'GET':
        return ChatHandler().get_chat_messages(request), 200
    else:
        #add message to chat
        return ChatHandler().insert_chat_message(request), 201

if __name__ == '__main__':
    app.run()
