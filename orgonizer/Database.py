import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('MyDatabase.db', check_same_thread=False)

    def create_event(self, date, name, begin, end, descryption=None):

        cursor = self.connection.cursor()
        cursor.execute(f'''INSERT OR IGNORE INTO Event (date, name, begin, end, descryption)
                                   VALUES ("{date}", "{name}", "{begin}", "{end}", "{descryption}")''')
        self.connection.commit()
        cursor.close()

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

"""
Controller = Event()

#Controller.create_event("02.02", "чачлыки", "19:00", "23:00")

print(Controller.read_events())
Controller.delete_event(3)

#Controller.update_event(1, "02.02", 'баран', '19:00', '23:00', 'None')
"""
Controller = Database()
print(Controller.read_events())