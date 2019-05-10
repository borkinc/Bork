from dateutil.relativedelta import relativedelta

from DAO.dao import DAO


class MessageDAO(DAO):

    def get_all_messages(self):
        """
        Gets all messages from DB.
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'WITH replies_query AS (SELECT replied_to, array_agg(mid) AS replies_list ' \
                'FROM replies INNER JOIN messages ON replies.reply =  messages.mid ' \
                'GROUP BY replied_to), ' \
                'like_count AS (SELECT mid, COUNT(*) AS likes FROM vote ' \
                'WHERE upvote = TRUE GROUP BY mid), ' \
                'dislike_count AS (SELECT mid, COUNT(*) AS dislikes FROM vote ' \
                'WHERE upvote = FALSE GROUP BY mid) ' \
                'SELECT messages.mid, users.uid, cid, message, image, ' \
                'COALESCE(likes, 0) AS likes, COALESCE(dislikes, 0) AS dislikes, username, ' \
                "COALESCE(replies_list, '{}') AS replies, messages.created_on " \
                'FROM messages LEFT OUTER JOIN like_count ON messages.mid = like_count.mid ' \
                'LEFT OUTER JOIN dislike_count ON messages.mid = dislike_count.mid ' \
                'LEFT OUTER JOIN photo ON messages.mid = photo.mid ' \
                'INNER JOIN users ON messages.uid = users.uid ' \
                'LEFT OUTER JOIN replies_query ON messages.mid = replies_query.replied_to ' \
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
        query = 'WITH like_count AS (SELECT mid, COUNT(*) AS likes ' \
                'FROM vote WHERE upvote = TRUE GROUP BY mid), ' \
                'dislike_count AS (SELECT mid, COUNT(*) AS dislikes ' \
                'FROM vote WHERE upvote = FALSE GROUP BY mid),' \
                'replies_query AS (SELECT replied_to, array_agg(mid) AS replies_list ' \
                'FROM replies INNER JOIN messages ON replies.reply =  messages.mid ' \
                'GROUP BY replied_to) ' \
                'SELECT messages.mid, cid, message, image, COALESCE(likes, 0) AS likes, ' \
                'COALESCE(dislikes, 0) AS dislikes, username, ' \
                "COALESCE(replies_list, '{}') AS replies " \
                'messages.created_on FROM messages ' \
                'LEFT OUTER JOIN like_count ON messages.mid = like_count.mid ' \
                'LEFT OUTER JOIN dislike_count ON messages.mid = dislike_count.mid ' \
                'LEFT OUTER JOIN photo ON messages.mid = photo.mid ' \
                'INNER JOIN users ON messages.uid = users.uid ' \
                'LEFT OUTER JOIN replies_query ON messages.mid = replies_query.replied_to ' \
                'WHERE messages.mid = %s ORDER BY messages.created_on DESC'
        cursor.execute(query, (mid,))
        messages = cursor.fetchall()
        return messages

    def get_message_replies(self, mid):
        """
        Gets messages that are replies to specified message
        :param mid: int
        """
        pass

    def get_likes_message(self, mid):
        """
        Gets number of likes message has
        :param mid: int
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT count(*) FROM vote WHERE mid = %s AND upvote = TRUE'
        cursor.execute(query, (mid,))
        return cursor.fetchall()

    def get_list_of_likers_message(self, mid):
        """
        Gets list of users who have liked a message with the given id.
        :param mid: int
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT users.uid, users.first_name, users.last_name, users.username, ' \
                'vote.voted_on ' \
                'FROM users INNER JOIN vote ON users.uid = vote.uid AND vote.upvote = TRUE ' \
                'INNER JOIN messages ON messages.mid = vote.mid AND messages.mid = %s'
        cursor.execute(query, (mid,))
        return cursor.fetchall()

    def get_list_of_dislikers_message(self, mid):
        """
        Gets list of users who have disliked a message with the given id.
        :param mid: int
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT users.uid,users.first_name, users.last_name, users.username, ' \
                'vote.voted_on ' \
                'FROM users INNER JOIN vote ON users.uid = vote.uid AND vote.upvote = FALSE ' \
                'INNER JOIN messages ON messages.mid = vote.mid AND messages.mid = %s'
        cursor.execute(query, (mid,))
        return cursor.fetchall()

    def vote_message(self, mid, uid, upvote):
        """
        Likes/Dislikes a message
        :param mid: int
        :param uid: int
        :param upvote: bool
        """
        cursor = self.get_cursor()
        query = 'INSERT into vote (mid, uid, upvote) values (%s, %s, %s)'
        cursor.execute(query, (mid, uid, upvote,))
        self.commit()

    def get_num_messages_daily(self, date):
        """
        Gets daily number of messages
        :param date: datetime
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = 'SELECT count(*) AS num FROM messages WHERE created_on > %s AND created_on < %s'
        cursor.execute(query, (date, end_date))
        count = cursor.fetchall()
        return count[0]['num']

    def get_num_likes_daily(self, date, like):
        """
        Gets daily number of likes
        :param date: datetime
        :param like: bool
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = 'SELECT count(*) AS num ' \
                'FROM vote ' \
                'WHERE voted_on > %s AND voted_on < %s AND upvote = %s'
        cursor.execute(query, (date, end_date, like))
        count = cursor.fetchall()
        return count[0]['num']

    def get_num_replies_daily(self, date):
        """
        Gets daily number of replies
        :param date: datetime
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = 'SELECT count(*) AS num ' \
                'FROM replies INNER JOIN messages ON messages.mid = replies.replied_to' \
                ' WHERE created_on > %s AND created_on < %s'
        cursor.execute(query, (date, end_date))
        count = cursor.fetchall()
        return count[0]['num']

    def get_num_replies_photos_daily(self, pid, date):
        """
        Gets daily number of replies for replies containing images
        :param pid: int
        :param date: datetime
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = 'SELECT count(*) AS num ' \
                'FROM replies INNER JOIN messages ON messages.mid = replies.replied_to ' \
                'WHERE replies.replied_to = %s AND created_on > %s AND created_on < %s'
        cursor.execute(query, (pid, date, end_date,))
        count = cursor.fetchall()
        return count[0]['num']

    def get_num_like_photos_daily(self, pid, date, like):
        """
        Gets daily number of likes for images
        :param pid: int
        :param date: datetime
        :param like: bool
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = 'SELECT count(*) AS num FROM vote WHERE vote.mid = %s ' \
                'AND vote.upvote = %s AND voted_on > %s AND voted_on < %s'
        cursor.execute(query, (pid, like, date, end_date,))
        count = cursor.fetchall()
        return count[0]['num']

    def get_trending_hashtags(self):
        """
        Gets trending hashtags
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT count(*) AS num, hashtag ' \
                'FROM hashtags_messages NATURAL INNER JOIN messages ' \
                'group by hashtag order by num desc limit 10'
        cursor.execute(query)
        return cursor.fetchall()

    def insert_message(self, cid, uid, message, img=None):
        """
        Inserts new message to database
        :param cid: int
        :param uid: int
        :param message: str
        :param img: str
        :return: int
        """
        cursor = self.get_cursor()
        query = 'INSERT INTO messages (cid, uid, message) VALUES(%s, %s, %s) RETURNING mid'
        cursor.execute(query, (cid, uid, message))
        message_id = cursor.fetchone()['mid']
        if img:
            query = 'INSERT INTO photo (image, mid) VALUES (%s, %s)'
            cursor.execute(query, (img, message_id))
        hastags = [mess for mess in message.split() if mess.startswith('#')]
        for hashtag in hastags:
            self.insert_hashtag(hashtag, message_id)
        cursor.connection.commit()
        return message_id

    def insert_reply(self, message, uid, mid, cid, img=None):
        """
        Inserts a new message in the form of a reply
        :param message: str
        :param uid: int
        :param mid: int
        :param cid: int
        :param img: str
        :return: int
        """
        cursor = self.get_cursor()
        rid = self.insert_message(cid, uid, message, img=img)
        query = 'INSERT INTO replies (replied_to, reply) values (%s, %s) RETURNING reply'
        cursor.execute(query, (mid, rid))
        reply_id = cursor.fetchone()['reply']
        self.commit()
        return reply_id

    def insert_hashtag(self, hashtag, mid):
        """
        Inserts a new hashtag to the database
        :param hashtag: str
        :param mid: int
        """
        cursor = self.get_cursor()
        query = 'INSERT INTO hashtags_messages (hashtag, mid) values (%s, %s)'
        cursor.execute(query, (hashtag, mid))
        self.commit()

    def remove_vote(self, mid, uid, upvote):
        """
        Updates/Deletes upvote column to remove a like/dislike
        :param mid: int
        :param uid: int
        :param upvote: bool
        :return: bool
        """
        cursor = self.get_cursor()
        query = 'SELECT * FROM vote WHERE mid = %s AND uid = %s'
        cursor.execute(query, (mid, uid))
        vote = [vote for vote in cursor.fetchall()]
        delete = vote[0]['upvote'] == upvote

        if delete:
            query = 'DELETE FROM vote WHERE mid = %s AND uid = %s'
            cursor.execute(query, (mid, uid))

        else:
            query = 'UPDATE vote SET upvote = %s WHERE mid = %s AND uid = %s'
            cursor.execute(query, (upvote, mid, uid))
        self.commit()
        return delete
