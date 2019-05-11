from dateutil.relativedelta import relativedelta

from dao.dao import DAO


class UserDAO(DAO):

    def insert_user(self, username, password, first_name, last_name, email, phone_number):
        """
        Inserts new user to database
        :param username: str
        :param password: str
        :param first_name: str
        :param last_name: str
        :param email: str
        :param phone_number: str
        :return: int
        """
        cursor = self.get_cursor()
        query = 'INSERT INTO users (username, password, first_name, ' \
                'last_name, email, phone_number) ' \
                'VALUES (%s,%s,%s,%s,%s,%s) returning uid'
        cursor.execute(query, (username, password, first_name, last_name, email, phone_number,))
        uid = cursor.fetchone()['uid']
        self.commit()
        return uid

    def get_all_users(self):
        """
        Gets all users from database
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT uid, username, first_name, last_name, email, phone_number ' \
                'FROM users'
        cursor.execute(query)
        return cursor.fetchall()

    def get_user(self, uid):
        """
        Gets user from database
        :param uid: int
        :return: RealDIctCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT username, first_name, last_name, email, phone_number ' \
                'FROM users WHERE uid = %s'
        cursor.execute(query, (uid,))
        return cursor.fetchall()

    def get_contacts(self, uid):
        """
        Gets list of users who are contacts of given user id
        :param uid: int
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT uid, contacts.first_name, contacts.last_name ' \
                'FROM users INNER JOIN contacts ON contacts.owner_id = %s ' \
                'AND users.uid = contacts.contact_id'
        cursor.execute(query, (uid,))
        return cursor.fetchall()

    def get_user_by_username(self, username):
        """
        Queries DB for information on given username
        :param username: str
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT uid, username, first_name, last_name, email, phone_number ' \
                'FROM users ' \
                'WHERE username = %s'
        cursor.execute(query, (username,))
        return cursor.fetchall()[0] if cursor.rowcount > 0 else None

    def get_user_by_phone_number(self, phone_number):
        """
        Gets user from database with matching phone number
        :param phone_number: str
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT uid, username, first_name, last_name, email, phone_number ' \
                'FROM users ' \
                'WHERE phone_number = %s'
        cursor.execute(query, (phone_number,))
        return cursor.fetchall()[0]

    def get_user_by_email(self, email):
        """
        Gets user from database with matching email
        :param email: str
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        query = 'SELECT uid, username, first_name, last_name, email, phone_number ' \
                'FROM users ' \
                'WHERE email = %s'
        cursor.execute(query, (email,))
        return cursor.fetchall()[0]

    def get_daily_messages_user(self, date, uid):
        """
        Gets number of messages posted on given date
        :param date: datetime
        :param uid: int
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = 'SELECT count(*) AS num, username ' \
                'FROM messages INNER JOIN users ON users.uid = messages.uid ' \
                'WHERE messages.uid = %s AND messages.created_on > %s ' \
                'AND messages.created_on < %s GROUP BY username'
        cursor.execute(query, (uid, date, end_date,))
        count = cursor.fetchone()
        if count:
            return count
        else:
            user = self.get_user(uid)[0]
            return {'num': 0, 'username': user['username']}

    def get_daily_active_users(self, date):
        """
        Gets daily active users from database
        :param date: datetime
        :return: RealDictCursor
        """
        cursor = self.get_cursor()
        end_date = date + relativedelta(days=1)
        query = 'WITH top_users AS (SELECT COUNT(*) AS amount, username ' \
                'FROM messages INNER JOIN users ON messages.uid = users.uid ' \
                'WHERE messages.created_on > %s AND messages.created_on < %s ' \
                'GROUP BY username ORDER BY amount DESC)' \
                'SELECT username FROM top_users LIMIT 10 '
        cursor.execute(query, (date, end_date))
        users = cursor.fetchall()
        return users

    def insert_contact(self, owner_contact, contact_uid_to_add, first_name, last_name):
        """
        Inserts a new contact to database
        :param owner_contact: int
        :param contact_uid_to_add: int
        :param first_name: str
        :param last_name: str
        """
        cursor = self.get_cursor()
        query = 'INSERT INTO contacts (owner_id, contact_id, first_name, last_name) ' \
                'VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (owner_contact, contact_uid_to_add, first_name, last_name,))
        self.commit()

    def delete_contact(self, owner_id, contact_id):
        """
        Deletes contact from database
        :param owner_id: int
        :param contact_id: int
        """
        cursor = self.get_cursor()
        query = 'DELETE FROM contacts WHERE owner_id = %s AND contact_id = %s'
        cursor.execute(query, (owner_id, contact_id,))
        self.commit()

    def get_user_password(self, username):
        """
        Get's password for specified user from DB
        :param username:
        :return:
        """
        cursor = self.get_cursor()
        query = 'SELECT password ' \
                'FROM users ' \
                'WHERE username = %s'
        cursor.execute(query, (username,))
        return cursor.fetchone()['password'] if cursor.rowcount > 0 else None
