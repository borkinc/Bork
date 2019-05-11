import uuid

from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from flask import current_app as app
from flask import jsonify, json
from flask_jwt_extended import get_jwt_identity
from werkzeug.utils import secure_filename

from dao.chat_dao import ChatDAO
from dao.message_dao import MessageDAO
from dao.user_dao import UserDAO


def store_image(img):
    """
    Stores image in cloudinary when running on production mode, otherwise,
    image is stored in the static img diractory
    :param img: File
    :return: str
    """
    if app.config['ENV'] == 'development':
        img.filename = f'{uuid.uuid4()}{img.filename}'
        filename = secure_filename(img.filename)
        from app import ROOT_DIR
        img.save(f'{ROOT_DIR}\\static\\img\\{filename}')
        image_url = f'static/img/{filename}'
    else:
        upload_result = upload(img)
        image_url = cloudinary_url(upload_result['public_id'], format='jpg')[0]
    return image_url


class ChatHandler:

    def __init__(self):
        self.chat_dao = ChatDAO()
        self.message_dao = MessageDAO()
        self.user_dao = UserDAO()

    def get_chats(self):
        """
        Gets all chats for current user
        :return: tuple
        """
        username = get_jwt_identity()
        user = self.user_dao.get_user_by_username(username)
        chats = self.chat_dao.get_user_chats(user['uid'])
        response_data = json.dumps({'chats': chats})
        response_status = 200
        return response_data, response_status

    def get_chat(self, cid):
        """
        Gets chat from database with given chat id
        :param cid: int
        :return: RealDictCursor
        """
        chat = self.chat_dao.get_chat(cid)
        return chat

    def get_chat_messages(self, cid):
        """
        Gets messages pertaining to chat with given id
        :param cid: int
        :return: RealDictCursor
        """
        return self.chat_dao.get_chat_messages(cid)

    def get_chat_members(self, cid):
        """
        Gets chat members of given chat id
        :param cid: int
        :return: RealDictCursor
        """
        return self.chat_dao.get_members_from_chat(cid)

    def get_chat_owner(self, cid):
        """
        Gets owner of chat with given id
        :param cid: int
        :return: RealDictCursor
        """
        return self.chat_dao.get_owner_of_chat(cid)

    def insert_chat(self, data):
        """
        Gathers necessary data to be sent to dao for inserting a new chat
        :param data: dict
        :return: tuple
        """
        if 'chat_name' in data and data['chat_name']:
            chat_name = data['chat_name']
            username = get_jwt_identity()
            user = self.user_dao.get_user_by_username(username)
            if data['members'] is not None:
                members = data['members'].split(',')
            else:
                members = []
            cid, created_on = self.chat_dao.insert_chat_group(chat_name, user['uid'],
                                                              members=members)
            response_data = json.dumps({
                'chat': {
                    'cid': cid,
                    'name': chat_name,
                    'created_on': created_on,
                    'msg': 'Success'
                }
            })
            response_status = 201
        else:
            response_data = json.dumps({'message': 'Chat name cannot be blank'})
            response_status = 400
        return response_data, response_status

    def insert_chat_message(self, cid, username, message, img=None):
        """
        Adds a new message to database
        :param cid: int
        :param username: str
        :param message: str
        :param img: File
        :return: RealDictCursor
        """
        if img:
            img = store_image(img)
        uid = UserDAO().get_user_by_username(username)['uid']
        return self.message_dao.insert_message(cid, uid, message, img=img)

    def add_contact_to_chat_group(self, cid, data):
        """
        Adds a contact from current user's contacts list to a chat group
        :param cid: int
        :param data: dict
        :return: tuple
        """
        current_user_username = get_jwt_identity()
        current_user_uid = self.user_dao.get_user_by_username(current_user_username)['uid']
        user_to_add = data['contact_id']
        chat_owner_uid = self.chat_dao.get_owner_of_chat(cid)[0]['uid']

        if chat_owner_uid != current_user_uid:
            response_data = json.dumps({'msg': 'Not owner of chat'})
            response_status = 403
        else:
            self.chat_dao.insert_member(cid, user_to_add)
            response_data = json.dumps({'msg': 'Success'})
            response_status = 201
        return response_data, response_status

    def remove_contact_from_chat_group(self, cid, data):
        """
        Removes a contact from current user's contacts list from chat group
        :param cid: int
        :param data: dict
        :return: tuple
        """
        current_user_username = get_jwt_identity()
        current_user_uid = self.user_dao.get_user_by_username(current_user_username)['uid']
        user_to_remove = data['contact_id']
        chat_owner_uid = self.chat_dao.get_owner_of_chat(cid)[0]['uid']

        if chat_owner_uid != current_user_uid:
            response_data = json.dumps({'msg': 'Not owner of chat'})
            response_status = 403
        else:
            self.chat_dao.remove_member(cid, user_to_remove)
            response_data = json.dumps({'msg': 'Success'})
            response_status = 201
        return response_data, response_status

    def reply_chat_message(self, data, mid):
        """
        Adds a reply to an existing message
        :param data: dict
        :param mid: int
        :return: tuple
        """
        message = data['message']
        cid = data['cid']
        img = store_image(data['img']) if data['img'] else None
        username = get_jwt_identity()
        uid = self.user_dao.get_user_by_username(username)['uid']
        rid = self.message_dao.insert_reply(message, uid, mid, cid, img=img)
        response_data = json.dumps({'rid': rid})
        response_status = 201
        return response_data, response_status

    def delete_chat(self, cid):
        """
        Deletes an existing chat
        :param cid: int
        :return: JSON
        """
        username = get_jwt_identity()
        uid = self.user_dao.get_user_by_username(username)['uid']
        chat_owner = self.chat_dao.get_owner_of_chat(cid)[0]['uid']
        if uid == chat_owner:
            self.chat_dao.delete_chat(cid)
            msg = 'Deleted'
        else:
            msg = 'Not ur chat >:('
        return jsonify(msg=msg)
