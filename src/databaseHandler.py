import sqlite3

class Database(object):
    def __init__(self):
        self.db_name = 'lists.db'

    def connect_db(self):
        self.cnx = sqlite3.connect(self.db_name)
        self.cursor = self.cnx.cursor()

    def query_db(self, query):
        self.connect_db()
        self.cursor.execute(query)

        if query[0:6].lower() == 'select':
            result = self.cursor.fetchall()
            self.cnx.close()
            return [result, self.cursor.description]
        else:
            self.cnx.commit()
            self.cnx.close()