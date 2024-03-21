import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('MyDatabase.db', check_same_thread=False)

    def create_event(self, date, name, begin, end, descryption=None):

        cursor = self.connection.cursor()
        cursor.execute(f'''INSERT OR IGNORE INTO Event (date, name, begin, end, descryption)
                                   VALUES ("{date}", "{name}", "{begin}", "{end}", "{descryption}")''')
        res = cursor.lastrowid
        self.connection.commit()
        cursor.close()
        return res

    def read_events(self):
        cursor = self.connection.cursor()
        cursor.execute(f'''SELECT * FROM Event
        ''')
        result = cursor.fetchall()
        cursor.close()
        return result

    def update_event(self, id, date, name, begin, end, descryption=None):
        cursor = self.connection.cursor()
        cursor.execute(f'''UPDATE Event SET date = "{date}", name = "{name}", begin = "{begin}", end = "{end}", descryption = "{descryption}"
                                   WHERE id = {id}''')
        self.connection.commit()
        cursor.close()

    def delete_event(self, id):
        cursor = self.connection.cursor()
        cursor.execute(
            f'''DELETE FROM Event
            WHERE id ={id}''')
        self.connection.commit()
        cursor.close()
