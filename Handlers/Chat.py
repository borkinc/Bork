import datetime

from flask import jsonify


class ChatHandler:

    def __init__(self):
        self.participants = [
            {
                'contact_id': 1
            }
        ]

    def get_chats(self):
        chats = [
            {
                'cid': 1,
                'name': 'skiribops',
                'participants': self.participants
            },
            {
                'cid': 2,
                'name': 'Subscribe to PewDiePie',
                'participants': self.participants
            },
            {
                'cid': 3,
                'name': 'DB',
                'participants': self.participants
            }
        ]
        return chats

    def get_chat(self, cid):
        chat = {
            'cid': 1,
            'name': 'Subscribe to pewdiepie',
            'participants': self.participants
        }
        return chat

    def get_chat_messages(self, cid):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')
        messages = [
            {
                'message_id': '1',
                'user_id': '1',
                'message': 'This is a test message!',
                'created_on': current_time,
                'img': None
            },
            {
                'message_id': '2',
                'user_id': '2',
                'message': 'Hello test message, this is chat',
                'created_on': current_time,
                'img': None
            },
            {
                'message_id': '3',
                'user_id': '3',
                'message': 'Hello chat, this is person',
                'created_on': current_time,
                'img': None
            },
            {
                'message_id': '4',
                'user_id': '4',
                'message': 'Hello person, this is other person',
                'created_on': current_time,
                'img': None
            },
            {
                'message_id': '5',
                'user_id': '5',
                'message': 'Hello other person, this is patrick',
                'created_on': current_time,
                'img': None
            }
        ]
        return messages

    def insert_chat(self, chat_name):
        chat = {
            'cid': 1,
            'name': 'skiribops',
            'participants': self.participants
        }
        return chat

    def insert_chat_message(self, message, img=None):
        _img = {'src': img, 'likes': 0, 'dislikes': 0}
        message = {
            'message_id': 5,
            'message': 'message',
            'cid': 1,
            'contact_id': 1,
            'img': _img
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
        _img = {'src': '/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png', 'likes': 1, 'dislikes': 0}
        message = {
            'message_id': 5,
            'message': 'message',
            'cid': 1,
            'contact_id': 1,
            'img': _img
        }
        return message

    def dislike_chat_message(self, chat_id, message_id):
        _img = {'src': '/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png', 'likes': 0, 'dislikes': 1}
        message = {
            'message_id': 5,
            'message': 'message',
            'cid': 1,
            'contact_id': 1,
            'img': _img
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
