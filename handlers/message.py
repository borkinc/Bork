import datetime

from dateutil.relativedelta import relativedelta
from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from dao.message_dao import MessageDAO
from dao.user_dao import UserDAO


class MessageHandler:

    def __init__(self):
        self.dao = MessageDAO()

    def get_all_messages(self):
        """
        Gets all messages
        :return: RealDictCursor
        """
        return self.dao.get_all_messages()

    def get_message(self, mid):
        """
        Gets message with specified id
        :param mid: int
        :return: RealDictCursor
        """
        return self.dao.get_message(mid)

    def get_replies(self, mid):
        """
        Gets messages that have replied to given message id
        :param mid: int
        :return: RealDictCursor
        """
        return self.dao.get_message_replies(mid)

    def get_likers(self, mid):
        """
        Gets users who have liked a message with specified id
        :param mid: int
        :return: RealDictCursor
        """
        return self.dao.get_list_of_likers_message(mid)

    def get_dislikers(self, mid):
        """
        Gets users who have disliked a message with specified id
        :param mid: int
        :return: RealDictCursor
        """
        return self.dao.get_list_of_dislikers_message(mid)

    def like_message(self, mid):
        """
        Likes a message
        :param mid: int
        :return: RealDictCursor
        """
        return self._vote_message(mid, True)

    def dislike_message(self, mid):
        """
        Dislikes a message
        :param mid: int
        :return: RealDictCursor
        """
        return self._vote_message(mid, False)

    def get_num_messages_daily(self):
        """
        Gets amount of messages posted per day
        :return: JSOM
        """
        today = datetime.date.today()
        num_posts = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_messages_daily(day_to_get)
            num_posts.append({'day': day_to_get, 'total': num})
        return jsonify(num_posts)

    def get_num_likes_daily(self):
        """
        Gets daily amount of likes
        :return: JSON
        """
        today = datetime.date.today()
        num_likes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_likes_daily(day_to_get, True)
            num_likes.append({'day': day_to_get, 'total': num})
        return jsonify(num_likes)

    def get_num_dislikes_daily(self):
        """
        Gets daily number of dislikes
        :return: JSON
        """
        today = datetime.date.today()
        num_dislikes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_likes_daily(day_to_get, False)
            num_dislikes.append({'day': day_to_get, 'total': num})
        return jsonify(num_dislikes)

    def get_num_replies_daily(self):
        """
        Gets daily number of replies
        :return: JSON
        """
        today = datetime.date.today()
        num_replies = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_replies_daily(day_to_get)
            num_replies.append({'day': day_to_get, 'total': num})
        return jsonify(num_replies)

    def get_num_replies_photo(self, pid):
        """
        Gets daily number of replies that contain images
        :param pid: int
        :return: JSON
        """
        today = datetime.date.today()
        num_replies = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_replies_photos_daily(pid, day_to_get)
            num_replies.append({'day': day_to_get, 'total': num})
        return jsonify(num_replies)

    def get_num_likes_photo(self, pid):
        """
        Gets daily number of likes for images
        :param pid: int
        :return: JSON
        """
        today = datetime.date.today()
        num_likes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_like_photos_daily(pid, day_to_get, True)
            num_likes.append({'day': day_to_get, 'total': num})
        return jsonify(num_likes)

    def get_num_dislikes_photo(self, pid):
        """
        Gets number of dislikes for photo
        :param pid: int
        :return: JSON
        """
        today = datetime.date.today()
        num_likes = []
        for i in range(7):
            day_to_get = today - relativedelta(days=i)
            num = self.dao.get_num_like_photos_daily(pid, day_to_get, False)
            num_likes.append({'day': day_to_get, 'total': num})
        return jsonify(num_likes)

    def get_trending_hashtags(self):
        """
        Gets trending hashtags
        :return: JSON
        """
        trending_hashtags = []
        hashtags = self.dao.get_trending_hashtags()
        for i, hashtag in enumerate(hashtags):
            trending_hashtags.append({'hashtag': hashtag['hashtag'], 'position': i + 1})
        return jsonify(trending_hashtags)

    def _vote_message(self, mid, upvote):
        """
        Likes/Dislikes a message
        :param mid: int
        :param upvote: bool
        :return: str
        """
        user = get_jwt_identity()
        uid = UserDAO().get_user_by_username(user)['uid']
        try:
            self.dao.vote_message(mid, uid, upvote)
            msg = 'Successfully added vote'
        except:
            self.dao.conn.rollback()
            deleted = self.dao.remove_vote(mid, uid, upvote)
            if deleted:
                msg = 'Successfully changed vote'
            else:
                msg = 'Successfully removed vote'
        return msg
