from DAO.DAO import DAO


class ChatDAO(DAO):

    def get_chat_messages(self, cid):
        cursor = self.get_cursor()
        query = "with like_count as (select count(*) as likes, mid from likes where upvote = true group by mid), " \
                "dislike_count as (select count(*) as dislikes, mid from likes where upvote = false group by mid) " \
                "select messages.mid, message, image, COALESCE(likes, 0) as likes, " \
                "COALESCE(dislikes, 0) as dislikes, username, messages.created_on, messages.uid " \
                "from messages left outer join " \
                "like_count on messages.mid = like_count.mid left outer join photo on " \
                "messages.mid = photo.mid left outer join dislike_count on messages.mid = dislike_count.mid " \
                "left outer join users on messages.uid = users.uid where messages.cid = %s " \
                "ORDER BY messages.created_on DESC"
        cursor.execute(query, (cid,))
        messages = cursor.fetchall()
        return messages

    def get_all_chats(self):
        cursor = self.get_cursor()
        query = "select * from chat_group"
        cursor.execute(query)
        return cursor.fetchall()

    def get_chat(self, cid):
        cursor = self.get_cursor()
        query = "SELECT chat_group.cid, chat_group.name, chat_group.uid, messages.message, messages.created_on " \
                "FROM chat_group INNER JOIN messages ON chat_group.cid = %s AND messages.cid = chat_group.cid " \
                "ORDER BY messages.created_on DESC LIMIT 1"
        cursor.execute(query, (cid,))
        return cursor.fetchall()

    def get_members_from_chat(self, cid):
        cursor = self.get_cursor()
        query = "select * from chat_members natural inner join users where cid = %s"
        cursor.execute(query, (cid,))
        return cursor.fetchall()

    def get_owner_of_chat(self, cid):
        cursor = self.get_cursor()
        query = "select * from chat_group natural inner join users where cid = %s"
        cursor.execute(query, (cid,))
        return cursor.fetchall()

    def insert_chat_group(self, chat_name, owner_id):
        cursor = self.get_cursor()
        query = "insert into chat_group (name, owner_id) values (%s, %s) returning cid"
        cursor.execute(query, (chat_name, owner_id))
        cid = cursor.fetchone()[0]
        self.conn.commit()
        return cid
