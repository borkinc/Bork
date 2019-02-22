from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources import UserRegistration, TokenRefresh, UserLogin, Chats, Index, ChatMessages, Contacts, Users, Chat, \
    LikeChatMessage, DislikeChatMessage, ReplyChatMessage

app = Flask(__name__)
app.config.from_object('config.config.BaseConfig')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app, prefix='/api')
jwt = JWTManager(app)


# ------------------------statistics-------------------------------

@app.route('/stats/trending')
def trending_topics():
    pass


@app.route('/stats/posts')
def num_of_posts():
    pass


@app.route('/stats/likes')
def num_of_likes():
    pass


@app.route('/stats/replies')
def num_of_replies():
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


api.add_resource(Index, '/')
api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(Users, '/users')
api.add_resource(Chats, '/chats')
api.add_resource(Chat, '/chat/<int:cid>')
api.add_resource(Contacts, '/contacts')
api.add_resource(ChatMessages, '/chat/<int:chat_id>/messages')
api.add_resource(LikeChatMessage, '/chat/<int:chat_id>/message/<int:message_id>/like')
api.add_resource(DislikeChatMessage, '/chat/<int:chat_id>/message/<int:message_id>/dislike')
api.add_resource(ReplyChatMessage, '/chat/<int:chat_id>/message/<int:message_id>/reply')
api.add_resource(TokenRefresh, '/token/refresh')

if __name__ == '__main__':
    app.run()
