import psycopg2

from config.dbconfig import pg_config


class Model:

    def __init__(self, **kwargs):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

        if kwargs:
            self.result_id = self.insert(kwargs)

    def insert(self, fields):
        cursor = self.conn.cursor()
        insert_str = 'insert into ' + self.__class__.__name__.lower() + ' ('

        for column, value in fields.items():
            insert_str += column + ", "
        insert_str = insert_str[:-2]
        insert_str += ') values ('
        for column, value in fields.items():
            if self.fields[column] == str:
                insert_str += "'" + value + "'" + ", "
            else:
                insert_str += "'" + value + "'" + ", "
        insert_str = insert_str[:-2]
        insert_str += ") returning " + self.id + ';'
        cursor.execute(insert_str)
        result_id = cursor.fetchone()[0]
        self.conn.commit()
        return result_id


class Users(Model):
    id = 'uid'
    fields = {
        'username': str,
        'hashed_password': str
    }



