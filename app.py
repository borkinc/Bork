from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from Handlers.Chat import ChatHandler
from Handlers.Users import UserHandler
from resources import UserRegistration, TokenRefresh, UserLogin, Chats, Index, ChatMessages, Contacts, Users, Chat, \
    LikeChatMessage, DislikeChatMessage, ReplyChatMessage, User, Contact, Messages, Message

app = Flask(__name__)
app.config.from_object('config.config.BaseConfig')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app, prefix='/api')
jwt = JWTManager(app)


# ------------------------statistics-------------------------------

@app.route('/stats/trending')
def trending_topics():
    return ChatHandler().get_trending_hashtags(request), 200


@app.route('/stats/posts')
def num_of_posts():
    return ChatHandler().get_num_posts_daily(request), 200


@app.route('/stats/likes')
def num_of_likes():
    return ChatHandler().get_num_likes_daily(request), 200


@app.route('/stats/replies')
def num_of_replies():
    return ChatHandler().get_num_replies_daily(request), 200


@app.route('/stats/dislikes')
def num_of_dislikes():
    return ChatHandler().get_num_dislikes_daily(request), 200


@app.route('/stats/active')
def active_users():
    return UserHandler().get_daily_active_users(request), 200


@app.route('/stats/users/<int:uid>/messages')
def num_of_mess_per_day(uid):
    return UserHandler().get_num_posts_user(request)


@app.route('/stats/photos/<int:pid>/replies')
def num_of_replies_photo(pid):
    return ChatHandler().get_num_replies_photo(request)


@app.route('/stats/photos/<int:pid>/likes')
def num_of_likes_photos(pid):
    return ChatHandler().get_num_likes_photo(request)


@app.route('/stats/photos/<int:pid>/dislikes')
def num_of_dislikes_photos(pid):
    return ChatHandler().get_num_dislikes_photo(request)


api.add_resource(Index, '/')
api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(Users, '/users')
api.add_resource(User, '/user')
api.add_resource(Chats, '/chats')
api.add_resource(Chat, '/chat/<int:cid>')
api.add_resource(Contacts, '/contacts')
api.add_resource(Contact, '/contacts/<int:uid>')
api.add_resource(ChatMessages, '/chat/<int:chat_id>/messages')
api.add_resource(Messages, '/messages')
api.add_resource(Message, '/messages/<int:mid>')
api.add_resource(LikeChatMessage, '/messages/<int:mid>/like')
api.add_resource(DislikeChatMessage, '/messages/<int:mid>/dislike')
api.add_resource(ReplyChatMessage, '/messages/<int:mid>/replies')
api.add_resource(TokenRefresh, '/token/refresh')

if __name__ == '__main__':
    app.run()
