import datetime

from dateutil.relativedelta import relativedelta
from flask import jsonify

from DAO.MessageDAO import MessageDAO


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
        return self.dao.like_message(mid)

    def dislike_message(self, mid):
        return self.dao.dislike_message(mid)

    def get_num_messages_daily(self):
        today = datetime.datetime.today()
        num_posts = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_messages_daily(day_to_get)
            num_posts.append({'%s' % day_to_get: num})
        return jsonify(result=num_posts)

    def get_num_likes_daily(self):
        today = datetime.datetime.today()
        num_likes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_likes_daily(day_to_get, True)
            num_likes.append({'%s' % day_to_get: num})
        return jsonify(result=num_likes)

    def get_num_dislikes_daily(self):
        today = datetime.datetime.today()
        num_dislikes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_likes_daily(day_to_get, False)
            num_dislikes.append({'%s' % day_to_get: num})
        return jsonify(result=num_dislikes)

    def get_num_replies_daily(self):
        today = datetime.datetime.today()
        num_replies = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_replies_daily(day_to_get)
            num_replies.append({'%s' % day_to_get: num})
        return jsonify(result=num_replies)

    def get_num_replies_photo(self, pid):
        today = datetime.datetime.today()
        num_replies = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_replies_photos_daily(pid, day_to_get)
            num_replies.append({'%s' % day_to_get: num})
        return jsonify(result=num_replies)

    def get_num_likes_photo(self, pid):
        today = datetime.datetime.today()
        num_likes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_like_photos_daily(pid, day_to_get, True)
            num_likes.append({'%s' % day_to_get: num})
        return jsonify(result=num_likes)

    def get_num_dislikes_photo(self, pid):
        today = datetime.datetime.today()
        num_likes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_like_photos_daily(pid, day_to_get, False)
            num_likes.append({'%s' % day_to_get: num})
        return jsonify(result=num_likes)
