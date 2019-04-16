import datetime

from dateutil.relativedelta import relativedelta
from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from DAO.MessageDAO import MessageDAO
from DAO.UserDAO import UserDAO


class MessageHandler:

    def __init__(self):
        self.dao = MessageDAO()

    def get_all_messages(self):
        return self.dao.get_all_messages()

    def get_message(self, mid):
        return self.dao.get_message(mid)

    def get_replies(self, mid):
        return self.dao.get_message_replies(mid)

    def get_likers(self, mid):
        return self.dao.get_list_of_likers_message(mid)

    def get_dislikers(self, mid):
        return self.dao.get_list_of_dislikers_message(mid)

    def like_message(self, mid):
        user = get_jwt_identity()
        uid = UserDAO().get_user_by_username(user)['uid']
        return self.dao.vote_message(mid, uid, True)

    def dislike_message(self, mid):
        user = get_jwt_identity()
        uid = UserDAO().get_user_by_username(user)['uid']
        return self.dao.vote_message(mid, uid, False)

    def get_num_messages_daily(self):
        today = datetime.date.today()
        num_posts = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_messages_daily(day_to_get)
            num_posts.append({'day': day_to_get, 'total': num})
        return jsonify(num_posts)

    def get_num_likes_daily(self):
        today = datetime.date.today()
        num_likes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_likes_daily(day_to_get, True)
            num_likes.append({'day': day_to_get, 'total': num})
        return jsonify(result=num_likes)

    def get_num_dislikes_daily(self):
        today = datetime.date.today()
        num_dislikes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_likes_daily(day_to_get, False)
            num_dislikes.append({'day': day_to_get, 'total': num})
        return jsonify(result=num_dislikes)

    def get_num_replies_daily(self):
        today = datetime.date.today()
        num_replies = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_replies_daily(day_to_get)
            num_replies.append({'day': day_to_get, 'total': num})
        return jsonify(result=num_replies)

    def get_num_replies_photo(self, pid):
        today = datetime.date.today()
        num_replies = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_replies_photos_daily(pid, day_to_get)
            num_replies.append({'day': day_to_get, 'total': num})
        return jsonify(result=num_replies)

    def get_num_likes_photo(self, pid):
        today = datetime.date.today()
        num_likes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_like_photos_daily(pid, day_to_get, True)
            num_likes.append({'day': day_to_get, 'total': num})
        return jsonify(result=num_likes)

    def get_num_dislikes_photo(self, pid):
        today = datetime.date.today()
        num_likes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_like_photos_daily(pid, day_to_get, False)
            num_likes.append({'day': day_to_get, 'total': num})
        return jsonify(result=num_likes)

    def get_trending_hashtags(self):
        trending_hashtags = []
        hashtags = self.dao.get_trending_hashtags()
        for i, hashtag in enumerate(hashtags):
            trending_hashtags.append({'hashtag': hashtag['hashtag'], 'position': i + 1})
        return jsonify(trending_hashtags)

