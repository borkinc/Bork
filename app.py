import bcrypt as bcrypt
from flask import Flask, request, jsonify
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
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return jsonify(username='test', msg='Success'), 201
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
        return jsonify(chats={'id': 1, 'chat_name': 'skiribops'}), 200

    elif request.method == 'POST':
        chat_name = request.form['chat_name']
        owner_id = request.form['uid']
        return jsonify(chat={'id':2, 'chat_name':chat_name}, msg='Success'), 201


@app.route('/api/chats/<int:cid>', methods=['GET'])
def chatByID(cid):
    if request.method == 'GET':
        return jsonify(chat={'id': cid, 'chat_name': 'skiribops'}), 200


@app.route('/api/contacts/<int:uid>', methods=['GET', 'POST'])
def contacts(uid):
    """
    if GET
    :param uid: user id de quien quieres la lista
    :return:
    """
    if request.method == 'GET':
        return jsonify(contacts=[{'uid': 3}, {'uid': 4}]), 200
    else:
        uid_to_add = request.form['uid']
        return jsonify(msg='added'), 201


if __name__ == '__main__':
    app.run()
