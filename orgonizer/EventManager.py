from PyQt5.QtCore import QDate, QTime

from Database import Database
from Event import Event


class EventManager:
    def __init__(self):
        self.event_list = []
        self.Controller = Database()
        for event in self.Controller.read_events():
            self.event_list.append(Event(id=event[0], name=event[1], date=QDate.fromString(event[5]),
                                         start_time=QTime.fromString(event[2]),
                                         stop_time=QTime.fromString(event[3]),
                                         description=event[4]))

    def add_event(self, name, date, start_time, stop_time, description):

        id = self.Controller.create_event(date.toString(), name, start_time.toString(), stop_time.toString(), description)
        new_event = Event(id, name, date, start_time, stop_time, description)
        self.event_list.append(new_event)
        return new_event

    def get_by_date(self, date):
        list_by_date = []
        for event in self.event_list:
            if event.date == date:
                list_by_date.append(event)

        return list_by_date

    def update_event(self, event_for_update, name, date, start_time, stop_time, description):
        for event in self.event_list:
            if event == event_for_update:
                event.name = name
                event.date = date
                event.start_time = start_time
                event.stop_time = stop_time
                event.description = description
                self.Controller.update_event(event.get_id(), date.toString(), name, start_time.toString(),
                                             stop_time.toString(), description)
                return event

    def delete_event(self, event_for_delete):
        self.Controller.delete_event(event_for_delete.get_id())
        for i in range(len(self.event_list)):
            if self.event_list[i] == event_for_delete:
                for_del = i
                break

        self.event_list.remove(self.event_list[for_del])
