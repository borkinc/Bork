from dateutil.relativedelta import relativedelta

from DAO.DAO import DAO


class MessageDAO(DAO):

    def get_all_messages(self):
        """
        Gets all messages from DB.
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'WITH replies_query as (SELECT replied_to, array_agg(mid) AS replies_list ' \
                'FROM replies INNER JOIN messages on replies.reply =  messages.mid GROUP BY replied_to), ' \
                'like_count AS (SELECT mid, COUNT(*) AS likes FROM vote WHERE upvote = TRUE GROUP BY mid), ' \
                'dislike_count AS (SELECT mid, COUNT(*) as dislikes FROM vote WHERE upvote = FALSE GROUP BY mid) ' \
                'SELECT messages.mid, users.uid, cid, message, image, COALESCE(likes, 0) as likes, ' \
                "COALESCE(dislikes, 0) as dislikes, username, COALESCE(replies_list, '{}') as replies, " \
                'messages.created_on FROM messages LEFT OUTER JOIN like_count ON messages.mid = like_count.mid ' \
                'LEFT OUTER JOIN dislike_count ON messages.mid = dislike_count.mid ' \
                'LEFT OUTER JOIN photo ON messages.mid = photo.mid INNER JOIN users on messages.uid = users.uid ' \
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
        query = 'WITH like_count AS (SELECT mid, COUNT(*) AS likes FROM vote WHERE upvote = TRUE GROUP BY mid), ' \
                'dislike_count AS (SELECT mid, COUNT(*) as dislikes FROM vote WHERE upvote = FALSE GROUP BY mid),' \
                'replies_query as (SELECT replied_to, array_agg(mid) AS replies_list ' \
                'FROM replies INNER JOIN messages on replies.reply =  messages.mid GROUP BY replied_to) ' \
                'SELECT messages.mid, cid, message, image, COALESCE(likes, 0) as likes, COALESCE(dislikes, 0) ' \
                "as dislikes, username, COALESCE(replies_list, '{}') as replies " \
                'messages.created_on FROM messages LEFT OUTER JOIN like_count ON messages.mid = like_count.mid ' \
                'LEFT OUTER JOIN dislike_count ON messages.mid = dislike_count.mid ' \
                'LEFT OUTER JOIN photo ON messages.mid = photo.mid INNER JOIN users on messages.uid = users.uid ' \
                'LEFT OUTER JOIN replies_query ON messages.mid = replies_query.replied_to ' \
                'WHERE messages.mid = %s ORDER BY messages.created_on DESC'
        cursor.execute(query, (mid,))
        messages = cursor.fetchall()
        return messages

    def get_message_replies(self, mid):
        pass

    def get_likes_message(self, mid):
        cursor = self.get_cursor()
        query = "select count(*) from vote where mid = %s and upvote = true"
        cursor.execute(query, (mid,))
        return cursor.fetchall()

    def get_list_of_likers_message(self, mid):
        """
        Gets list of users who have liked a message with the given id.
        :param mid: int
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT users.uid, users.first_name, users.last_name, users.username, vote.voted_on ' \
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
        query = 'SELECT users.uid,users.first_name, users.last_name, users.username, vote.voted_on ' \
                'FROM users INNER JOIN vote ON users.uid = vote.uid AND vote.upvote = FALSE ' \
                'INNER JOIN messages ON messages.mid = vote.mid AND messages.mid = %s'
        cursor.execute(query, (mid,))
        return cursor.fetchall()

    def vote_message(self, mid, uid, upvote):
        cursor = self.get_cursor()
        query = 'insert into vote (mid, uid, upvote) values (%s, %s, %s)'
        cursor.execute(query, (mid, uid, upvote, ))
        self.conn.commit()

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
        query = "select count(*) as num from vote where voted_on > %s and voted_on < %s and upvote = %s"
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
        query = "select count(*) as num, vote from vote where vote.mid = %s " \
                "and vote.upvote = %s and created_on > %s and created_on < %s"
        cursor.execute(query, (pid, like, date, end_date, ))
        count = cursor.fetchall()
        return count[0]['num']

    def get_trending_hashtags(self):
        cursor = self.get_cursor()
        query = "select count(*) as num, hashtag from hashtags_messages natural inner join messages " \
                "group by hashtag order by num desc limit 10"
        cursor.execute(query)
        return cursor.fetchall()

    def insert_message(self, cid, uid, message, img=None):
        cursor = self.get_cursor()
        query = 'INSERT INTO messages (cid, uid, message) VALUES(%s, %s, %s) RETURNING mid'
        cursor.execute(query, (cid, uid, message))
        message_id = cursor.fetchone()['mid']
        if img:
            query = 'INSERT INTO photo (image, mid) VALUES (%s, %s)'
            cursor.execute(query, (img, message_id))
        hastags = [mess for mess in message.split() if mess.startswith("#")]
        cursor.connection.commit()
        for hashtag in hastags:
            self.insert_hashtag(hashtag, message_id)
        return message_id

    def insert_reply(self, message, uid, mid, cid, img=None):
        cursor = self.get_cursor()
        rid = self.insert_message(cid, uid, message, img=img)
        query = 'INSERT INTO replies (replied_to, reply) values (%s, %s)'
        cursor.execute(query, (mid, rid))
        reply_id = cursor.fetchone()['mid']
        self.conn.commit()
        return reply_id

    def insert_hashtag(self, hashtag, mid):
        cursor = self.get_cursor()
        query = 'INSERT INTO hashtags_messages (hashtag, mid) values (%s, %s)'
        cursor.execute(query, (hashtag, mid))
        self.conn.commit()

    def remove_vote(self, mid, uid, upvote):
        cursor = self.get_cursor()
        query = "SELECT * FROM vote WHERE mid = %s and uid = %s"
        cursor.execute(query, (mid, uid))
        vote = [vote for vote in cursor.fetchall()]
        delete = vote[0]['upvote'] == upvote

        if delete:
            query = "DELETE FROM vote WHERE mid = %s and uid = %s"
            cursor.execute(query, (mid, uid))

        else:
            query = "UPDATE vote SET upvote = %s WHERE mid = %s and uid = %s"
            cursor.execute(query, (upvote, mid, uid))
        self.conn.commit()
        return delete
