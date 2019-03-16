from DAO.DAO import DAO


class ChatDAO(DAO):

    def get_all_messages(self):
        '''
        yeah this needs some work
        '''
        cursor = self.get_cursor()
        query = "select * from messages"
        cursor.execute(query)
        messages = []
        for row in cursor:
            mid = row['mid']
            query = "select count(*) filter (where upvote = true) as liked, count(*) filter (where upvote = false) as disliked from likes natural inner join users where mid = %s"
            new_cursor = self.get_cursor()
            new_cursor.execute(query, (mid, ))
            row = dict(row)
            row.update({'likes': new_cursor.fetchone()[0], 'dislikes': new_cursor.fetchone()[1]})
            messages.append(row)
        return messages

    def get_all_chats(self):
        cursor = self.get_cursor()
        query = "select * from chat_group"
        cursor.execute(query)
        chat_groups = [row for row in cursor]
        return chat_groups

    def get_members_from_chat(self, cid):
        cursor = self.get_cursor()
        query = "select * from chat_members natural inner join users where cid = %s"
        cursor.execute(query, (cid, ))
        members = [row for row in cursor]
        return members

    def get_owner_of_chat(self, cid):
        cursor = self.get_cursor()
        query = "select * from chat_group natural inner join users where cid = %s"
        cursor.execute(query, (cid, ))
        chat = [row for row in cursor]
        return chat[0]['username']

    def get_likes_message(self, mid):
        cursor = self.get_cursor()
        query = "select count(*) from Likes where mid = %s and upvote = true"
        cursor.execute(query, (mid, ))
        return cursor[0]

