from dateutil.relativedelta import relativedelta

from DAO.DAO import DAO


class MessageDAO(DAO):

    def get_all_messages(self):
        cursor = self.get_cursor()
        query = "with like_count as (select count(*) as likes, mid from likes where upvote = true group by mid), " \
                "dislike_count as (select count(*) as dislikes, mid from likes where upvote = false group by mid) " \
                "select message, image, likes, dislikes, username, messages.created_on from messages left outer join " \
                "like_count on messages.mid = like_count.mid left outer join multimedia on " \
                "messages.mid = multimedia.mid left outer join dislike_count on messages.mid = dislike_count.mid " \
                "left outer join users on messages.uid = users.uid"
        cursor.execute(query)
        messages = [row for row in cursor]
        return messages

    def get_message(self, mid):
        cursor = self.get_cursor()
        query = "with like_count as (select count(*) as likes, mid from likes where upvote = true group by mid), " \
                "dislike_count as (select count(*) as dislikes, mid from likes where upvote = false group by mid) " \
                "select message, image, likes, dislikes, username, messages.created_on from messages left outer join " \
                "like_count on messages.mid = like_count.mid left outer join multimedia on " \
                "messages.mid = multimedia.mid left outer join dislike_count on messages.mid = dislike_count.mid " \
                "left outer join users on messages.uid = users.uid where messages.mid = %s"
        cursor.execute(query, (mid,))
        message = [row for row in cursor]
        return message[0]

    def get_message_replies(self, mid):
        pass

    def get_likes_message(self, mid):
        cursor = self.get_cursor()
        query = "select count(*) from Likes where mid = %s and upvote = true"
        cursor.execute(query, (mid,))
        return cursor[0]

    def get_list_of_likers_message(self, mid):
        cursor = self.get_cursor()
        query = "select username from Likes left outer join users on likes.uid = users.uid where likes.mid = %s and " \
                "upvote = true "
        cursor.execute(query, (mid,))
        usernames = [row for row in cursor]
        return usernames

    def get_list_of_dislikers_message(self, mid):
        cursor = self.get_cursor()
        query = "select username from Likes left outer join users on likes.uid = users.uid where likes.mid = %s and " \
                "upvote = false "
        cursor.execute(query, (mid,))
        usernames = [row for row in cursor]
        return usernames

    def like_message(self, mid):
        pass

    def dislike_message(self, mid):
        pass

    def get_num_messages_daily(self, date):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select count(*) as num from messages where created_on > %s and created_on < %s"
        cursor.execute(query, (date, end_date))
        count = [row for row in cursor]
        return count[0]['num']

    def get_num_likes_daily(self, date, like):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select count(*) as num from likes where liked_on > %s and liked_on < %s and upvote = %s"
        cursor.execute(query, (date, end_date, like))
        count = [row for row in cursor]
        return count[0]['num']

    def get_num_replies_daily(self, date):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select count(*) as num from replies inner join messages on messages.mid = replies.reply" \
                " where created_on > %s and created_on < %s"
        cursor.execute(query, (date, end_date))
        count = [row for row in cursor]
        return count[0]['num']

    def get_num_replies_photos_daily(self, pid, date):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select count(*) as num from replies where replies.reply = %s and created _on > %s and created_on < %s"
        cursor.execute(query, (pid, date, end_date, ))
        count = [row for row in cursor]
        return count[0]['num']

    def get_num_like_photos_daily(self, pid, date, like):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select count(*) as num likes from likes where likes.mid = %s " \
                "and likes.upvote = %s and created_on > %s and created_on < %s"
        cursor.execute(query, (pid, like, date, end_date, ))
        count = [row for row in cursor]
        return count[0]['num']



