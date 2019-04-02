from dateutil.relativedelta import relativedelta

from DAO.DAO import DAO


class MessageDAO(DAO):

    def get_all_messages(self):
        """
        Gets all messages from DB.
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'WITH like_count AS (SELECT mid, COUNT(*) AS likes FROM likes WHERE upvote = TRUE GROUP BY mid), ' \
                'dislike_count AS (SELECT mid, COUNT(*) as dislikes FROM likes WHERE upvote = FALSE GROUP BY mid) ' \
                'SELECT mid, message, image, COALESCE(likes, 0) as likes, COALESCE(dislikes, 0) as dislikes, username, ' \
                'messages.created_on FROM messages LEFT OUTER JOIN like_count ON messages.mid = like_count.mid ' \
                'LEFT OUTER JOIN dislike_count ON messages.mid = dislike_count.mid ' \
                'LEFT OUTER JOIN photo ON messages.mid = photo.mid INNER JOIN users on messages.uid = users.uid ' \
                'ORDER BY messages.created_on DESC'
        cursor.execute(query)
        messages = cursor.fetchall()
        return messages

    def get_message(self, mid):
        """
        Gets message from DB with specified id
        :param mid: int
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'WITH like_count AS (SELECT mid, COUNT(*) AS likes FROM likes WHERE upvote = TRUE GROUP BY mid), ' \
                'dislike_count AS (SELECT mid, COUNT(*) as dislikes FROM likes WHERE upvote = FALSE GROUP BY mid) ' \
                'SELECT mid, message, image, COALESCE(likes, 0) as likes, COALESCE(dislikes, 0) as dislikes, username, ' \
                'messages.created_on FROM messages LEFT OUTER JOIN like_count ON messages.mid = like_count.mid ' \
                'LEFT OUTER JOIN dislike_count ON messages.mid = dislike_count.mid ' \
                'LEFT OUTER JOIN photo ON messages.mid = photo.mid INNER JOIN users on messages.uid = users.uid ' \
                'WHERE messages.mid = %s ORDER BY messages.created_on DESC'
        cursor.execute(query, (mid,))
        messages = cursor.fetchall()
        return messages

    def get_message_replies(self, mid):
        pass

    def get_likes_message(self, mid):
        cursor = self.get_cursor()
        query = "select count(*) from Likes where mid = %s and upvote = true"
        cursor.execute(query, (mid,))
        return cursor.fetchall()

    def get_list_of_likers_message(self, mid):
        """
        Gets list of users who have liked a message with the given id.
        :param mid: int
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT users.uid, users.first_name, users.last_name, likes.liked_on ' \
                'FROM users INNER JOIN likes ON users.uid = likes.uid AND likes.upvote = TRUE ' \
                'INNER JOIN messages ON messages.mid = likes.mid AND messages.mid = %s'
        cursor.execute(query, (mid,))
        return cursor.fetchall()

    def get_list_of_dislikers_message(self, mid):
        """
        Gets list of users who have disliked a message with the given id.
        :param mid: int
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT users.uid, users.first_name, usera.last_name, likes.liked_on ' \
                'FROM users INNER JOIN likes ON users.uid = likes.uid AND likes.upvote = FALSE ' \
                'INNER JOIN messages ON messages.mid = likes.mid AND messages.mid = %s'
        cursor.execute(query, (mid,))
        return cursor.fetchall()

    def like_message(self, mid):
        pass

    def dislike_message(self, mid):
        pass

    def get_num_messages_daily(self, date):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select count(*) as num from messages where created_on > %s and created_on < %s"
        cursor.execute(query, (date, end_date))
        count = cursor.fetchall()
        return count[0]['num']

    def get_num_likes_daily(self, date, like):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select count(*) as num from likes where liked_on > %s and liked_on < %s and upvote = %s"
        cursor.execute(query, (date, end_date, like))
        count = cursor.fetchall()
        return count[0]['num']

    def get_num_replies_daily(self, date):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select count(*) as num from replies inner join messages on messages.mid = replies.reply" \
                " where created_on > %s and created_on < %s"
        cursor.execute(query, (date, end_date))
        count = cursor.fetchall()
        return count[0]['num']

    def get_num_replies_photos_daily(self, pid, date):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select count(*) as num from replies where replies.reply = %s and created _on > %s and created_on < %s"
        cursor.execute(query, (pid, date, end_date, ))
        count = cursor.fetchall()
        return count[0]['num']

    def get_num_like_photos_daily(self, pid, date, like):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select count(*) as num likes from likes where likes.mid = %s " \
                "and likes.upvote = %s and created_on > %s and created_on < %s"
        cursor.execute(query, (pid, like, date, end_date, ))
        count = cursor.fetchall()
        return count[0]['num']

    def get_trending_hashtags_day(self, date):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "with trending as (select count(*) as num, hid from hashtags_messages natural inner join messages " \
                "natural inner join hashtags where messages.created_on > %s and messages.created_on < %s " \
                "group by hid order by num desc limit 10)" \
                "select hashtag from hashtags natural inner join trending"
        cursor.execute(query, (date, end_date))
        return cursor.fetchall()
