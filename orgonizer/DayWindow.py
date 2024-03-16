from PyQt5.QtWidgets import QMainWindow, QMenu, QAction
from PyQt5.QtCore import QDate
from PyQt5 import uic

from EventWidget import EventWidget
from Event import Event
from AddEventDialog import AddEventDialog
from WeekWindow import WeekWindow


class DayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('DayWindow.ui', self)
        self.ui.pbAddNew.clicked.connect(self.add_event_clicked_slot)
        self.ui.pbWeek.clicked.connect(self.open_week_window_slot)
        self.weekWindow = WeekWindow(self)

        self.hourToLabel = {
            0: self.ui.label_1,
            1: self.ui.label_2,
            2: self.ui.label_3,
            3: self.ui.label_4,
            4: self.ui.label_5,
            5: self.ui.label_6,
            6: self.ui.label_7,
            7: self.ui.label_8,
            8: self.ui.label_9,
            9: self.ui.label_10,
            10: self.ui.label_11,
            11: self.ui.label_12,
            12: self.ui.label_13,
            13: self.ui.label_14,
            14: self.ui.label_15,
            15: self.ui.label_16,
            16: self.ui.label_17,
            17: self.ui.label_18,
            18: self.ui.label_19,
            19: self.ui.label_20,
            20: self.ui.label_21,
            21: self.ui.label_22,
            22: self.ui.label_23,
            23: self.ui.label_24
        }

        self.dayNumberToButton = {
            1: self.ui.pbDay1,
            2: self.ui.pbDay2,
            3: self.ui.pbDay3,
            4: self.ui.pbDay4,
            5: self.ui.pbDay5,
            6: self.ui.pbDay6,
            7: self.ui.pbDay7
        }

        for i in range(1, 8):
            button = self.dayNumberToButton[i]
            if i == QDate.currentDate().dayOfWeek():
                button.setStyleSheet('color: #ff0000; min-width: 10px;')
            else:
                button.setStyleSheet('color: #0000ff; min-width: 10px;')

            button.clicked.connect(self.day_changed_slot)

        self.events = []

    def day_changed_slot(self):
        for i in range(1, 8):
            button = self.dayNumberToButton[i]
            if button == self.sender():
                button.setStyleSheet('color: #ff0000; min-width: 10px;')
            else:
                button.setStyleSheet('color: #0000ff; min-width: 10px;')

    def test(self):
        self.create_event('Правоведение', (0, 0), (3, 0), 'University', EventWidget.colors['green'])
        self.create_event('Работа', (5, 0), (6, 0), 'Work', EventWidget.colors['pink'])
        self.create_event('Test', (8, 0), (13, 0), 'Тест', EventWidget.colors['red'])
        self.create_event('Тест 2', (18, 0), (21, 0), 'Test 2', EventWidget.colors['orange'])

    def create_event(self, name, start_time, stop_time, description, color):
        text = f'<b>{name}</b><br/>{description}'
        event = Event(10, name, 'today', start_time, stop_time, description)
        tmp = EventWidget(event, text, self, color=color)
        y_pos = self.hourToLabel[start_time[0]].pos().y() + 10
        y_stop = self.hourToLabel[stop_time[0]].pos().y() + 10
        height = max(y_stop - y_pos, 20)
        width = self.width() - self.hourToLabel[start_time[0]].width() - 40
        tmp.setGeometry(50, y_pos, width, height)
        tmp.clickedSignal.connect(self.event_clicked_slot)
        tmp.contextRequest.connect(self.context_request_slot)

        self.events.append(tmp)
        tmp.show()

    def event_clicked_slot(self):
        print(self.sender().event)

    def context_request_slot(self, pos):
        menu = QMenu(self)
        action = QAction('Удалить событие', self.sender())
        action.triggered.connect(self.delete_slot)
        menu.addAction(action)
        menu.popup(self.sender().mapToGlobal(pos))

    def delete_slot(self):
        eventWidget = self.sender().parent()
        print(eventWidget.event)

    def open_week_window_slot(self):
        self.weekWindow.show()
        self.hide()

    def add_event_clicked_slot(self):
        dialog = AddEventDialog(self)
        if dialog.exec() == AddEventDialog.DialogCode.Accepted:
            start_time = (dialog.start_time().hour(), dialog.start_time().minute())
            stop_time = (dialog.stop_time().hour(), dialog.stop_time().minute())

            if stop_time < start_time:
                start_time, stop_time = stop_time, start_time

            event = Event(None, dialog.name(), dialog.date(), start_time, stop_time, dialog.description())

            text = f'<b>{dialog.name()}</b><br/>{dialog.description()}'

            tmp = EventWidget(event, text, self, color=EventWidget.colors['green'])
            y_pos = self.hourToLabel[start_time[0]].pos().y() + 10
            y_stop = self.hourToLabel[stop_time[0]].pos().y() + 10
            height = max(y_stop - y_pos, 20)
            width = self.width() - self.hourToLabel[start_time[0]].width() - 40

            tmp.setGeometry(50, y_pos, width, height)
            tmp.clickedSignal.connect(self.event_clicked_slot)
            tmp.contextRequest.connect(self.context_request_slot)

            self.events.append(tmp)
            tmp.show()

    def resizeEvent(self, event):
        for tmp in self.events:
            y_pos = self.hourToLabel[tmp.event.start_time[0]].pos().y() + 10
            y_stop = self.hourToLabel[tmp.event.stop_time[0]].pos().y() + 10
            height = max(y_stop - y_pos, 20)
            width = self.width() - self.hourToLabel[tmp.event.start_time[0]].width() - 40
            tmp.setGeometry(50, y_pos, width, height)

