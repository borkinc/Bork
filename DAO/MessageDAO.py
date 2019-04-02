import base64

from dateutil.relativedelta import relativedelta

from DAO.DAO import DAO


class MessageDAO(DAO):

    def get_all_messages(self):
        cursor = self.get_cursor()
        query = "with like_count as (select count(*) as likes, mid from likes where upvote = true group by mid), " \
                "dislike_count as (select count(*) as dislikes, mid from likes where upvote = false group by mid) " \
                "select message, image, likes, dislikes, username, messages.created_on from messages left outer join " \
                "like_count on messages.mid = like_count.mid left outer join photo on " \
                "messages.mid = photo.mid left outer join dislike_count on messages.mid = dislike_count.mid " \
                "left outer join users on messages.uid = users.uid"
        cursor.execute(query)
        messages = cursor.fetchall()
        for message in messages:
            if message['dislikes'] is None:
                message['dislikes'] = 0
            if message['likes'] is None:
                message['dislikes'] = 0
        return messages

    def get_message(self, mid):
        cursor = self.get_cursor()
        query = "with like_count as (select count(*) as likes, mid from likes where upvote = true group by mid), " \
                "dislike_count as (select count(*) as dislikes, mid from likes where upvote = false group by mid) " \
                "select message, image, likes, dislikes, username, messages.created_on from messages left outer join " \
                "like_count on messages.mid = like_count.mid left outer join photo on " \
                "messages.mid = photo.mid left outer join dislike_count on messages.mid = dislike_count.mid " \
                "left outer join users on messages.uid = users.uid where messages.mid = %s"
        messages = cursor.fetchall()
        for message in messages:
            if message['image']:
                image_data = message['image'].tobytes()
                message['image'] = base64.encodebytes(image_data).decode('utf-8')
            if message['dislikes'] is None:
                message['dislikes'] = 0
            if message['likes'] is None:
                message['likes'] = 0
        return messages

    def get_message_replies(self, mid):
        pass

    def get_likes_message(self, mid):
        cursor = self.get_cursor()
        query = "select count(*) from Likes where mid = %s and upvote = true"
        cursor.execute(query, (mid,))
        return cursor.fetchall()

    def get_list_of_likers_message(self, mid):
        cursor = self.get_cursor()
        query = "SELECT users.uid, users.username " \
                "FROM users INNER JOIN messages ON messages.mid = %s AND messages.uid = users.uid " \
                "INNER JOIN likes ON messages.mid = likes.mid AND likes.upvote = TRUE "
        cursor.execute(query, (mid,))
        return cursor.fetchall()

    def get_list_of_dislikers_message(self, mid):
        cursor = self.get_cursor()
        query = "SELECT users.uid, users.username " \
                "FROM users INNER JOIN messages ON messages.mid = %s AND messages.uid = users.uid " \
                "INNER JOIN likes ON messages.mid = likes.mid AND likes.upvote = FALSE "
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
                "select hashtag from hashtags inner join trending on trending.hid = hashtags.hid"
        cursor.execute(query, (date, end_date))
        return cursor.fetchall()


