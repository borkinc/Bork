from dateutil.relativedelta import relativedelta

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
        query = 'SELECT uid, username, first_name, last_name, email, phone_number ' \
                'FROM users'
        cursor.execute(query)
        return cursor.fetchall()

    def get_user(self, uid):
        cursor = self.get_cursor()
        query = 'select username, first_name, last_name, email, phone_number from users where uid = %s'
        cursor.execute(query, (uid,))
        return cursor.fetchall()

    def get_contacts(self, uid):
        """
        Gets list of users who are contacts of given user id
        :param uid: int
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT username, first_name, last_name ' \
                'FROM users INNER JOIN contacts ON contacts.owner_id = %s AND users.uid = contacts.contact_id'
        cursor.execute(query, (uid,))
        return cursor.fetchall()

    def get_user_by_username(self, username):
        cursor = self.get_cursor()
        query = 'SELECT username, first_name, last_name, email, phone_number ' \
                'FROM users ' \
                'WHERE username = %s'
        cursor.execute(query, (username,))
        return cursor.fetchall()

    def get_daily_messages_user(self, date, uid):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select count(*) as num from messages where messages.uid = %s and created_on > %s and created_on < %s"
        cursor.execute(query, (uid, date, end_date,))
        count = cursor.fetchall()
        return count[0]['num']

    def get_daily_active_users(self, date):
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = "select username from messages natural inner join users where created_on > %s and created_on < %s"
        cursor.execute(query, (date, end_date))
        users = cursor.fetchall()
        return users
