import base64
from io import BytesIO

from DAO.DAO import DAO


class ChatDAO(DAO):

    def get_chat_messages(self, cid):
        buffered = BytesIO()
        cursor = self.get_cursor()
        query = "with like_count as (select count(*) as likes, mid from likes where upvote = true group by mid), " \
                "dislike_count as (select count(*) as dislikes, mid from likes where upvote = false group by mid) " \
                "select messages.mid, message, image, likes, dislikes, username, messages.created_on, messages.uid " \
                "from messages left outer join " \
                "like_count on messages.mid = like_count.mid left outer join photo on " \
                "messages.mid = photo.mid left outer join dislike_count on messages.mid = dislike_count.mid " \
                "left outer join users on messages.uid = users.uid where messages.cid = %s"
        cursor.execute(query, (cid,))
        messages = cursor.fetchall()
        for message in messages:
            if message['image']:
                image_data = message['image'].tobytes()
                message['image'] = base64.encodebytes(image_data).decode('utf-8')
            if message['dislikes'] is None:
                message['dislikes'] = 0
        return messages
        # messages = [row for row in cursor]
        # return messages

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
