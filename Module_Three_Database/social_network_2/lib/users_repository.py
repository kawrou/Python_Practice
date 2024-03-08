from lib.user import *

class Users_repository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["email_address"], row["username"])
            users.append(item)
        return users

    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["email_address"], row["username"])

    def create(self, email_address, username):
        rows = self._connection.execute(
            'INSERT INTO users (email_address, username) VALUES (%s, %s)', [email_address, username]
        )
    def delete(self, user_id):
        rows = self._connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id]
        )
        