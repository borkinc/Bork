import uuid

from werkzeug.utils import secure_filename

from DAO.ChatDAO import ChatDAO
from DAO.MessageDAO import MessageDAO


class ChatHandler:

    def __init__(self):
        self.chatDAO = ChatDAO()
        self.messageDAO = MessageDAO()

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

    def insert_chat_message(self, cid, uid, message, img=None):
        if img:
            img.filename = f'{uuid.uuid4()}{img.filename}'
            filename = secure_filename(img.filename)
            from app import ROOT_DIR
            img.save(f'{ROOT_DIR}\\static\\img\\{filename}')
            img = f'static/img/{filename}'
        return self.messageDAO.insert_message(cid, uid, message, img)

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

    def get_chat_members(self, cid):
        return self.chatDAO.get_members_from_chat(cid)
