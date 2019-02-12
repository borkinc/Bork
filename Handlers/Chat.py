from flask import jsonify


class ChatHandler:

    def get_chats(self, request):
        chats = []
        chats.append({'cid': 1, 'name': 'Skiribops'})
        chats.append({'cid': 2, 'name': 'Bork'})
        return jsonify(chats=chats)

    def get_chat(self, request):
        return jsonify(chats={'cid': request.form['cid'], 'name': 'Skiribops'})

    def get_chat_messages(self, request):
        cid = request.form['cid']
        messages = [
            {
                'mid': 1,
                'content': 'Hello',
                'user_id': 4
            },
            {
                'mid': 6,
                'content': 'BAI',
                'user_id': 5
            },
            {
                'mid': 7,
                'content': 'Chill',
                'user_id': 4
            }
        ]
        return jsonify(messages=messages, cid=cid)

    def insert_chat(self, request):
        name = request.form['name']
        return jsonify(msg='Success', chat={'cid': 3, 'name': name})

    def insert_chat_message(self, request):
        content = request.form['content']
        cid = request.form['cid']
        return jsonify(msg='Success', message={'mid': 5, 'content': content, 'cid': cid})