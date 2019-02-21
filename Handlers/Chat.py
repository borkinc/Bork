import datetime

from flask import jsonify


class ChatHandler:

    def get_chats(self):
        chats = [
            {"id": 1, "chat_name": "skiribops"},
            {"id": 2, "chat_name": "Subscribe to PewDiePie"},
            {"id": 3, "chat_name": "DB"}
        ]
        return jsonify(chats=chats)

    def get_chat(self, chat_id):
        results = {
            'chat': {
                'id': 1,
                'chat_name': 'Subscribe to pewdiepie'}
        }
        return jsonify(results=results)

    def get_chat_messages(self, chat_id):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        messages = [
            {
                'message_id': '1',
                'user_id': '1',
                'message': 'This is a test message!',
                'created_on': current_time
            },
            {
                'message_id': '2',
                'user_id': '2',
                'message': "Hello test message, this is chat",
                'created_on': current_time
            },
            {
                'message_id': '3',
                'user_id': '3',
                'message': "Hello chat, this is person",
                'created_on': current_time
            },
            {
                'message_id': '4',
                'user_id': '4',
                'message': "Hello person, this is other person",
                'created_on': current_time
            },
            {
                'message_id': '5',
                'user_id': '5',
                'message': "Hello other person, this is patrick",
                'created_on': current_time
            }
        ]
        return messages

    def insert_chat(self, request):
        name = request.form['name']
        return jsonify(msg='Success', chat={'cid': 3, 'name': name})

    def insert_chat_message(self, request):
        content = request.form['content']
        cid = request.form['cid']
        return jsonify(msg='Success', message={'message_id': 5, 'content': content, 'cid': cid})
