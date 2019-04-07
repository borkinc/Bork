import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from Handlers.Message import MessageHandler
from Handlers.Users import UserHandler
from resources import UserRegistration, TokenRefresh, UserLogin, Chats, Index, ChatMessages, Contacts, Users, Chat, \
    LikeChatMessage, DislikeChatMessage, ReplyChatMessage, User, Contact, Messages, Message, ChatMembers

app = Flask(__name__)
config = f'config.config.{os.getenv("FLASK_SETTINGS")}'
app.config.from_object(config)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app, prefix='/api')
jwt = JWTManager(app)


# ------------------------statistics-------------------------------

@app.route('/stats/trending')
def trending_topics():
    return MessageHandler().get_trending_hashtags(), 200


@app.route('/stats/messages')
def num_of_posts():
    return MessageHandler().get_num_messages_daily(), 200


@app.route('/stats/likes')
def num_of_likes():
    return MessageHandler().get_num_likes_daily(), 200


@app.route('/stats/replies')
def num_of_replies():
    return MessageHandler().get_num_replies_daily(), 200


@app.route('/stats/dislikes')
def num_of_dislikes():
    return MessageHandler().get_num_dislikes_daily(), 200


@app.route('/stats/active')
def active_users():
    return UserHandler().get_daily_active_users(), 200


@app.route('/stats/users/<int:uid>/messages')
def num_of_mess_per_day(uid):
    return UserHandler().get_num_messages_user(uid)


@app.route('/stats/photos/<int:pid>/replies')
def num_of_replies_photo(pid):
    return MessageHandler().get_num_replies_photo(pid)


@app.route('/stats/photos/<int:pid>/likes')
def num_of_likes_photos(pid):
    return MessageHandler().get_num_likes_photo(pid)


@app.route('/stats/photos/<int:pid>/dislikes')
def num_of_dislikes_photos(pid):
    return MessageHandler().get_num_dislikes_photo(pid)


api.add_resource(Index, '/')
api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<string:user>')
api.add_resource(Chats, '/chats')
api.add_resource(Chat, '/chats/<int:cid>')
api.add_resource(ChatMembers, '/chats/<int:cid>/members')
api.add_resource(ChatOwner, '/chats/<int:cid>/owner')
api.add_resource(Contacts, '/contacts')
api.add_resource(Contact, '/contacts/<int:uid>')
api.add_resource(ChatMessages, '/chats/<int:chat_id>/messages')
api.add_resource(Messages, '/messages')
api.add_resource(Message, '/messages/<int:mid>')
api.add_resource(LikeChatMessage, '/messages/<int:mid>/like')
api.add_resource(DislikeChatMessage, '/messages/<int:mid>/dislike')
api.add_resource(ReplyChatMessage, '/messages/<int:mid>/replies')
api.add_resource(TokenRefresh, '/token/refresh')

if __name__ == '__main__':
    app.run()
