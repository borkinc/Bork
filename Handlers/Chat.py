import uuid

from flask import jsonify, json
from flask_jwt_extended import get_jwt_identity
from werkzeug.utils import secure_filename

from DAO.ChatDAO import ChatDAO
from DAO.MessageDAO import MessageDAO
from DAO.UserDAO import UserDAO


class ChatHandler:

    def __init__(self):
        self.chatDAO = ChatDAO()
        self.messageDAO = MessageDAO()
        self.userDAO = UserDAO()

    def get_chats(self):
        """
        Gets all chats for current user
        :return: tuple
        """
        username = get_jwt_identity()
        user = self.userDAO.get_user_by_username(username)
        chats = self.chatDAO.get_user_chats(user['uid'])
        response_data = json.dumps({'chats': chats})
        response_status = 200
        return response_data, response_status

    def get_chat(self, cid):
        chat = self.chatDAO.get_chat(cid)
        return chat

    def get_chat_messages(self, cid):
        return self.chatDAO.get_chat_messages(cid)

    def get_chat_members(self, cid):
        return self.chatDAO.get_members_from_chat(cid)

    def get_chat_owner(self, cid):
        return self.chatDAO.get_owner_of_chat(cid)

    def insert_chat(self, data):
        """
        Gathers necessary data to be sent to dao for inserting a new chat
        :param data: dict
        :return: tuple
        """
        if 'chat_name' in data and data['chat_name']:
            chat_name = data['chat_name']
            username = get_jwt_identity()
            user = self.userDAO.get_user_by_username(username)
            if data['members'] is not None:
                members = data['members'].split(',')
            else:
                members = []
            cid = self.chatDAO.insert_chat_group(chat_name, user['uid'], members=members)
            response_data = json.dumps({
                'chat': cid,
                'msg': 'Success'
            })
            response_status = 201
        else:
            response_data = json.dumps({'message': 'Chat name cannot be blank'})
            response_status = 400
        return response_data, response_status

    def insert_chat_message(self, cid, username, message, img=None):
        if img:
            img.filename = f'{uuid.uuid4()}{img.filename}'
            filename = secure_filename(img.filename)
            from app import ROOT_DIR
            img.save(f'{ROOT_DIR}\\static\\img\\{filename}')
            img = f'static/img/{filename}'
        uid = UserDAO().get_user_by_username(username)['uid']
        return self.messageDAO.insert_message(cid, uid, message, img=img)

    def add_contact_to_chat_group(self, cid, data):
        current_user_username = get_jwt_identity()
        current_user_uid = self.userDAO.get_user_by_username(current_user_username)['uid']
        user_to_add = data['contact_id']
        chat_owner_uid = self.chatDAO.get_owner_of_chat(cid)[0]['uid']

        if chat_owner_uid != current_user_uid:
            response_data = json.dumps({'msg': 'Not owner of chat'})
            response_status = 403
        else:
            self.chatDAO.insert_member(cid, user_to_add)
            response_data = json.dumps({'msg': 'Success'})
            response_status = 201
        return response_data, response_status

    def remove_contact_from_chat_group(self, cid, data):
        current_user_username = get_jwt_identity()
        current_user_uid = self.userDAO.get_user_by_username(current_user_username)['uid']
        user_to_remove = data['contact_id']
        chat_owner_uid = self.chatDAO.get_owner_of_chat(cid)[0]['uid']

        if chat_owner_uid != current_user_uid:
            response_data = json.dumps({'msg': 'Not owner of chat'})
            response_status = 403
        else:
            self.chatDAO.remove_member(cid, user_to_remove)
            response_data = json.dumps({'msg': 'Success'})
            response_status = 201
        return response_data, response_status

    def remove_chat(self, cid):
        chat = {
            'cid': 1,
            'name': 'skiribops',
            'participants': []
        }
        return chat

    def reply_chat_message(self, data, mid):
        try:
            message = data['message']
            cid = data['cid']
        except KeyError:
            return jsonify(msg='Missing parameter')
        if 'img' in data:
            img = data['img']
        else:
            img = None
        username = get_jwt_identity()
        uid = self.userDAO.get_user_by_username(username)

        rid = self.messageDAO.insert_reply(message, uid, mid, cid, img=img)
        return rid

    def delete_chat(self, cid):
        username = get_jwt_identity()
        uid = self.userDAO.get_user_by_username(username)['uid']
        chat_owner = self.chatDAO.get_owner_of_chat(cid)[0]['uid']
        if uid == chat_owner:
            self.chatDAO.delete_chat(cid)
            return jsonify(msg="Deleted")
        else:
            return jsonify(msg="Not ur chat >:(")
