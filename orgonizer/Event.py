
class Event:
    def __init__(self, id, name, date, start_time, stop_time, description):
        self.id = id
        self.name = name
        self.date = date
        self.start_time = start_time
        self.stop_time = stop_time
        self.description = description

    def __str__(self):
        return f'Event({self.id}, "{self.name}", {self.date}, {self.start_time}, {self.stop_time}, "{self.description}")'
