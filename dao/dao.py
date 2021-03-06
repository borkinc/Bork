import psycopg2
import psycopg2.extras
from flask import current_app as app


class DAO:

    def __init__(self):
        config = app.config['DATABASE']
        self.conn = psycopg2.connect(dbname=config['DBNAME'], user=config['USER'],
                                     password=config['PASSWORD'], host=config['HOST'],
                                     port=config['PORT'])

    def get_cursor(self):
        """
        Gets psycopg2 RealDictCursor
        :return: RealDictCursor
        """
        return self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def commit(self):
        """
        Commits changes to database
        """
        self.conn.commit()
