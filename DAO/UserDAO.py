from DAO.DAO import DAO


class UserDAO(DAO):

    def insert_user(self, username, password, first_name, last_name, email, phone_number):
        cursor = self.get_cursor()
        query = "insert into users (username, password, first_name, last_name, email, phone_number) " \
                "values (%s,%s,%s,%s,%s,%s) returning uid"
        cursor.execute(query, (username, password, first_name, last_name, email, phone_number,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def get_all_users(self):
        cursor = self.get_cursor()
        query = "select username, first_name, last_name, email, phone_number from users;"
        cursor.execute(query)
        users = [row for row in cursor]
        return users

    def get_user(self, uid):
        cursor = self.get_cursor()
        query = "select username, first_name, last_name, email, phone_number from users where uid = %s"
        cursor.execute(query, (uid,))
        user = [row for row in cursor]
        return user[0]

    def get_contacts(self, uid):
        cursor = self.get_cursor()
        query = "select username, first_name, last_name from contacts, users inner join on contact_id = uid where owner_id = %s"
        cursor.execute(query, (uid,))
        users = [row for row in cursor]
        return users
