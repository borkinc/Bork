import base64

import psycopg2
import psycopg2.extras
from flask import current_app as app


def encode_message_images(messages):
    """
    Base64 encodes image bytes
    :param messages: list of queried messages
    :return: list
    """
    for message in messages:
        if message['image']:
            image_data = message['image'].tobytes()
            message['image'] = base64.encodebytes(image_data).decode('utf-8')
    return messages


class DAO:

    def __init__(self):
        config = app.config['DATABASE']
        self.conn = psycopg2.connect(dbname=config['DBNAME'], user=config['USER'], password=config['PASSWORD'],
                                     host=config['HOST'], port=config['PORT'])

    def get_cursor(self):
        return self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
