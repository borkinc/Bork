from DAO.DAO import DAO


class UserDAO(DAO):

    def insert_user(self, username, password, first_name, last_name, email, phone_number):
        cursor = self.get_cursor()
        query = 'insert into users (username, password, first_name, last_name, email, phone_number) ' \
                'values (%s,%s,%s,%s,%s,%s) returning uid'
        cursor.execute(query, (username, password, first_name, last_name, email, phone_number,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def get_all_users(self):
        cursor = self.get_cursor()
        query = 'select username, first_name, last_name, email, phone_number from users;'
        cursor.execute(query)
        return cursor.fetchall()

    def get_user(self, uid):
        cursor = self.get_cursor()
        query = 'select username, first_name, last_name, email, phone_number from users where uid = %s'
        cursor.execute(query, (uid,))
        return cursor.fetchall()

    def get_contacts(self, uid):
        cursor = self.get_cursor()
        query = 'select username, first_name, last_name from contacts, users inner join on contact_id = uid ' \
                'where owner_id = %s'
        cursor.execute(query, (uid,))
        return cursor.fetchall()

    def get_user_by_username(self, username):
        cursor = self.get_cursor()
        query = 'select uid, username, password from users where username = %s'
        cursor.execute(query, (username,))
        return cursor.fetchall()
