import psycopg2
import psycopg2.extras

from config.config import ProductionConfig


class DAO:

    def __init__(self):
        config = ProductionConfig()

        self.conn = psycopg2.connect(dbname=config.DATABASE['DBNAME'], user=config.DATABASE['USER'],
                                     password=config.DATABASE['PASSWORD'], host=config.DATABASE['HOST'],
                                     port=config.DATABASE['PORT'])

    def get_cursor(self):
        return self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
