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
        today = datetime.date.today()
        trending_hashtags = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            hashtags = self.dao.get_trending_hashtags_day(day_to_get)
            hashtag_day = []
            for j, hashtag in enumerate(hashtags):
                hashtag_day.append({'hashtag': hashtag['hashtag'], 'position': j+1})
            trending_hashtags.append({'day': day_to_get, 'hashtags': hashtag_day})
        return jsonify(trending_hashtags)
