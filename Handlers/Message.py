from DAO.MessageDAO import MessageDAO


class MessageHandler:

    def __init__(self):
        self.dao = MessageDAO()

    def get_all_messages(self):
        return self.dao.get_all_messages()

    def get_message(self, mid):
        return self.dao.get_message(mid)

    def get_replies(self, mid):
        return self.dao.get_message_replies(mid)

    def get_likers(self, mid):
        return self.dao.get_list_of_likers_message(mid)

    def get_dislikers(self, mid):
        return self.dao.get_list_of_dislikers_message(mid)

    def like_message(self, mid):
        return self.dao.like_message(mid)

    def dislike_message(self, mid):
        return self.dao.dislike_message(mid)
