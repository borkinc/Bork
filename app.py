from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources import UserRegistration, TokenRefresh, UserLogin, Chats

app = Flask(__name__)
app.config.from_object('config.config.BaseConfig')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app, prefix='/api')
jwt = JWTManager(app)


@app.route('/', methods=['GET'])
def index():
    return jsonify(welcome='Hello World')


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

# api.add_resource(Chat, '/chat/<int:chat_id>')
api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(Chats, '/chats')
api.add_resource(TokenRefresh, '/token/refresh')

if __name__ == '__main__':
    app.run(debug=True)
