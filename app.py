import os

import cloudinary
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from handlers.message import MessageHandler
from handlers.users import UserHandler
from resources import UserRegistration, TokenRefresh, UserLogin, Chats, \
    Index, ChatMessages, Contacts, Users, Chat, \
    LikeChatMessage, DislikeChatMessage, ReplyChatMessage, \
    User, Contact, Messages, Message, ChatMembers

APP = Flask(__name__)
CONFIG = f'config.config.{os.getenv("FLASK_SETTINGS")}'
APP.config.from_object(CONFIG)
CORS = CORS(APP, resources={r"*": {"origins": "*"}})
API = Api(APP, prefix='/api')
jwt = JWTManager(APP)

if APP.config['ENV'] == 'production':
    cloudinary.config(cloud_name=APP.config['CLOUD_NAME'], api_key=APP.config['API_KEY'],
                      api_secret=APP.config['API_SECRET'])
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# ------------------------statistics-------------------------------

@APP.route('/stats/trending')
def trending_topics():
    """
    Gets trending hashtags from database
    :return: JSON
    """
    return MessageHandler().get_trending_hashtags(), 200


@APP.route('/stats/messages')
def num_of_posts():
    """
    Gets number of messages posted per day from database
    :return: JSON
    """
    return MessageHandler().get_num_messages_daily(), 200


@APP.route('/stats/likes')
def num_of_likes():
    """
    Gets number of likes per day from database
    :return: JSON
    """
    return MessageHandler().get_num_likes_daily(), 200


@APP.route('/stats/replies')
def num_of_replies():
    """
    Gets number of replies per day from database
    :return: JSON
    """
    return MessageHandler().get_num_replies_daily(), 200


@APP.route('/stats/dislikes')
def num_of_dislikes():
    """
    Gets number of dislikes per day from database
    :return: JSON
    """
    return MessageHandler().get_num_dislikes_daily(), 200


@APP.route('/stats/active')
def active_users():
    """
    Gets daily active users from database
    :return: JSON
    """
    return UserHandler().get_daily_active_users(), 200


@APP.route('/stats/users/<int:uid>/messages')
def num_of_mess_per_day(uid):
    """
    Gets numbers of posted messages by user per day
    :param uid: int
    :return: JSON
    """
    return UserHandler().get_num_messages_user(uid)


@APP.route('/stats/photos/<int:pid>/replies')
def num_of_replies_photo(pid):
    """
    Gets number of photo replies per day for the given photo id
    :param pid: int
    :return: JSON
    """
    return MessageHandler().get_num_replies_photo(pid)


@APP.route('/stats/photos/<int:pid>/likes')
def num_of_likes_photos(pid):
    """
    Gets number of likes for the given photo id
    :param pid: int
    :return: JSON
    """
    return MessageHandler().get_num_likes_photo(pid)


@APP.route('/stats/photos/<int:pid>/dislikes')
def num_of_dislikes_photos(pid):
    """
    Gets number of dislikes for the given photo id
    :param pid: int
    :return: JSON
    """
    return MessageHandler().get_num_dislikes_photo(pid)


API.add_resource(Index, '/')
API.add_resource(UserRegistration, '/register')
API.add_resource(UserLogin, '/login')
API.add_resource(Users, '/users')
API.add_resource(User, '/users/<string:user>')
API.add_resource(Chats, '/chats')
API.add_resource(Chat, '/chats/<int:cid>')
API.add_resource(ChatMembers, '/chats/<int:cid>/members')
API.add_resource(Contacts, '/contacts')
API.add_resource(Contact, '/contacts/<int:uid>')
API.add_resource(ChatMessages, '/chats/<int:chat_id>/messages')
API.add_resource(Messages, '/messages')
API.add_resource(Message, '/messages/<int:mid>')
API.add_resource(LikeChatMessage, '/messages/<int:mid>/like')
API.add_resource(DislikeChatMessage, '/messages/<int:mid>/dislike')
API.add_resource(ReplyChatMessage, '/messages/<int:mid>/replies')
API.add_resource(TokenRefresh, '/token/refresh')

if __name__ == '__main__':
    APP.run()
