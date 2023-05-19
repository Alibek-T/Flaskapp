import sqlite3


class User:

    def __init__(self):  # , username, email, password, register_date):
        # self.username = username
        # self.email = email
        # self.password = password
        # self.register_date = register_date
        self.db = 'db.sqlite3'
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()

    def get_all_users(self):
        result = []
        query = self.cursor.execute("SELECT * FROM users")
        for data in query.fetchall():
            result.append({
                'id': data[0],
                'username': data[1],
                'email': data[2],
                'password': data[3],
                'register_date': data[4]
            })
        return result
