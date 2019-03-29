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
