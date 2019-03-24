from flask import jsonify

from DAO.ChatDAO import ChatDAO


class ChatHandler:

    def __init__(self):
        self.chatDAO = ChatDAO()

    def get_chats(self):
        chats = self.chatDAO.get_all_chats()
        return chats

    def get_chat(self, cid):
        chat = self.chatDAO.get_chat(cid)
        return chat

    def get_chat_messages(self, cid):
        return self.chatDAO.get_chat_messages(cid)

    def insert_chat(self, chat_name, owner_id):
        cid = self.chatDAO.insert_chat(chat_name, owner_id)
        return cid

    def insert_chat_message(self, message, img=None):
        _img = {'src': img, 'likes': 0, 'dislikes': 0}
        message = {
            'message_id': 5,
            'message': 'message',
            'cid': 1,
            'contact_id': 1,
            'likes': [],
            'dislikes': [],
            'img': img
        }
        return message

    def add_contact_to_chat_group(self, contact_id):
        participants = [
            {
                'contact_id': 1
            },
            {
                'contact_id': 2
            }
        ]
        chat = {
            'cid': 1,
            'name': 'skiribops',
            'participants': participants
        }
        return chat

    def remove_contact_from_chat_group(self, contact_id):
        chat = {
            'cid': 1,
            'name': 'skiribops',
            'participants': self.participants
        }
        return chat

    def remove_chat(self, cid):
        chat = {
            'cid': 1,
            'name': 'skiribops',
            'participants': self.participants
        }
        return chat

    def like_chat_message(self, chat_id, message_id):
        message = {
            'message_id': 5,
            'message': 'message',
            'cid': 1,
            'contact_id': 1,
            'likes': [],
            'dislikes': [],
            'img': '/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png'
        }
        return message

    def dislike_chat_message(self, chat_id, message_id):
        message = {
            'message_id': 5,
            'message': 'message',
            'cid': 1,
            'contact_id': 1,
            'likes': [],
            'dislikes': [],
            'img': '/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png'
        }
        return message

    def reply_chat_message(self, chat_id, message_id, message):
        replies = [
            {
                'mid': 10
            }
        ]
        message = {
            'message_id': 5,
            'message': 'message',
            'cid': 1,
            'contact_id': 1,
            'likes': [],
            'dislikes': [],
            'img': None,
            'replies': replies
        }
        return message

    def get_trending_hashtags(self, request):
        hashtags = [{'hid': 3, 'tag': '#bork'}, {'hid': 4, 'tag': '#borked'}]
        return jsonify(result=hashtags)

    def get_num_posts_daily(self, request):
        return jsonify(result=4)

    def get_num_likes_daily(self, request):
        return jsonify(result=3)

    def get_num_replies_daily(self, request):
        return jsonify(result=1)

    def get_num_dislikes_daily(self, request):
        return jsonify(result=0)

    def get_num_replies_photo(self, request):
        return jsonify(result=1)

    def get_num_likes_photo(self, request):
        return jsonify(result=1)

    def get_num_dislikes_photo(self, request):
        return jsonify(result=100)
