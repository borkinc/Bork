from DAO.DAO import DAO


class ChatDAO(DAO):

    def get_chat_messages(self, cid):
        cursor = self.get_cursor()
        query = "with like_count as (select count(*) as likes, mid from likes where upvote = true group by mid), " \
                "dislike_count as (select count(*) as dislikes, mid from likes where upvote = false group by mid) " \
                "select message, image, likes, dislikes, username, messages.created_on from messages left outer join " \
                "like_count on messages.mid = like_count.mid left outer join multimedia on " \
                "messages.mid = multimedia.mid left outer join dislike_count on messages.mid = dislike_count.mid " \
                "left outer join users on messages.uid = users.uid where messages.cid = %s"
        cursor.execute(query, (cid,))
        messages = [row for row in cursor]
        return messages

    def get_all_chats(self):
        cursor = self.get_cursor()
        query = "select * from chat_group"
        cursor.execute(query)
        chat_groups = [row for row in cursor]
        return chat_groups

    def get_chat(self, cid):
        cursor = self.get_cursor()
        query = "select * from chat_group where cid = %s"
        cursor.execute(query, (cid,))
        chat = [row for row in cursor]
        return chat[0]

    def get_members_from_chat(self, cid):
        cursor = self.get_cursor()
        query = "select * from chat_members natural inner join users where cid = %s"
        cursor.execute(query, (cid,))
        members = [row for row in cursor]
        return members

    def get_owner_of_chat(self, cid):
        cursor = self.get_cursor()
        query = "select * from chat_group natural inner join users where cid = %s"
        cursor.execute(query, (cid,))
        chat = [row for row in cursor]
        return chat[0]['username']

    def insert_chat_group(self, chat_name, owner_id):
        cursor = self.get_cursor()
        query = "insert into chat_group (name, owner_id) values (%s, %s) returning cid"
        cursor.execute(query, (chat_name, owner_id))
        cid = cursor.fetchone()[0]
        self.conn.commit()
        return cid
