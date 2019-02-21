import bcrypt as bcrypt
from flask import Flask, request, jsonify

from Handlers.Chat import ChatHandler
from Handlers.Users import UserHandler
from flask_cors import CORS

app = Flask(__name__)
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


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/register', methods=['POST'])
def create_user():
    """
    Creates user with given username, email and password to be stored in database
    :return: json containing username and success
    """
    if request.method == 'POST':
        return UserHandler().insert_user(request), 201
    return jsonify(msg='Error'), 500


@app.route('/api/login', methods=['POST'])
def login():
    """

    :return:
    """
    if request.method == 'POST':
        return UserHandler().get_user(request), 200


@app.route('/api/chats', methods=['GET', 'POST'])
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


@app.route('/api/chats/<int:cid>', methods=['GET'])
def chatByID(cid):
    if request.method == 'GET':
        return ChatHandler().get_chat(request), 200


@app.route('/api/contacts/<int:uid>', methods=['GET', 'POST'])
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
        # add message to chat
        return ChatHandler().insert_chat_message(request), 201


# ------------------------statistics-------------------------------

@app.route('/stats/trending')
def trending_topics():
    pass


@app.route('stats/posts')
def num_of_posts():
    pass


@app.route('/stats/likes')
def num_of_likes():
    pass


@app.route('/stats/replies')
def num_of_likes():
    pass


@app.route('/stats/dislikes')
def num_of_dislikes():
    pass


@app.route('/stats/active')
def active_users():
    pass


@app.route('/stats/users/<int:uid>/messages')
def num_of_mess_per_day(uid):
    pass


@app.route('/stats/photos/<int:pid>/replies')
def num_of_replies_photo(pid):
    pass


@app.route('/stats/photos/<int:pid>/likes')
def num_of_likes_photos(pid):
    pass


@app.route('/stats/photos/<int:pid>/dislikes')
def num_of_dislikes_photos(pid):
    pass


if __name__ == '__main__':
    app.run()
