import random

from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QVBoxLayout
from PyQt5.QtCore import QDate, QTime
from PyQt5 import uic

from EventWidget import EventWidget
from Event import Event
from AddEventDialog import AddEventDialog
from WeekWindow import WeekWindow
from EventManager import EventManager


class DayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('DayWindow.ui', self)
        self.ui.pbAddNew.clicked.connect(self.add_event_clicked_slot)
        self.ui.pbWeek.clicked.connect(self.open_week_window_slot)
        self.weekWindow = WeekWindow(self)
        self.currentDayNumber = QDate.currentDate().dayOfWeek()

        self.setStyleSheet('QFrame[frameShape="4"] { max-height: none; }')  # Это стиль для горизонтальных линий

        self.hourToLabel = {}
        self.dayNumberToButton = {}
        self.init_dicts()

        self.update_days_style()
        for button in self.dayNumberToButton.values():
            button.clicked.connect(self.day_changed_slot)

        self.eventWidgets = []
        self.eventManager = EventManager()

    def init_events(self):
        for event in self.eventManager.get_by_date(QDate.currentDate()):
            self.create_event(event, random.choice(list(EventWidget.colors.values())))

    def day_changed_slot(self):
        self.currentDayNumber = list(self.dayNumberToButton.keys())[list(self.dayNumberToButton.values()).index(self.sender())]
        print(f'Выбрали день недели: {self.currentDayNumber}')
        print('Надо бы угадать дату и обновить список событий')
        self.update_days_style()

    def update_days_style(self):
        for i in range(1, 8):
            button = self.dayNumberToButton[i]
            if i == self.currentDayNumber:
                button.setStyleSheet('color: #ff0000; min-width: 10px;')
            else:
                button.setStyleSheet('color: #0000ff; min-width: 10px;')

    def create_event(self, event, color):
        text = f'<b>{event.name}</b><br/>{event.description}'
        tmp = EventWidget(event, text, self, color=color)
        self.set_event_geometry(tmp)
        tmp.doubleClickedSignal.connect(self.event_double_clicked_slot)
        tmp.contextRequest.connect(self.context_request_slot)

        self.eventWidgets.append(tmp)
        tmp.show()

    def set_event_geometry(self, tmp):
        hour_height = (self.hourToLabel[tmp.event.start_time.hour() + 1].pos().y() -
                       self.hourToLabel[tmp.event.start_time.hour()].pos().y())

        x_pos = self.hourToLabel[tmp.event.start_time.hour()].pos().x() + 10
        y_pos = (self.hourToLabel[tmp.event.start_time.hour()].pos().y() +
                 self.hourToLabel[tmp.event.start_time.hour()].height() // 2 +
                 round(hour_height * tmp.event.start_time.minute() / 60))
        y_stop = (self.hourToLabel[tmp.event.stop_time.hour()].pos().y() +
                  self.hourToLabel[tmp.event.stop_time.hour()].height() // 2 +
                  round(hour_height * tmp.event.stop_time.minute() / 60))
        height = max(y_stop - y_pos, 20)
        width = self.hourToLabel[tmp.event.start_time.hour()].width() - 20
        tmp.setGeometry(x_pos, y_pos, width, height)

    def event_double_clicked_slot(self):
        print(f'double_clicked "{self.sender().event}"')

    def context_request_slot(self, pos):
        menu = QMenu(self)
        actionEdit = QAction('Изменить событие', self.sender())
        actionDelete = QAction('Удалить событие', self.sender())
        actionEdit.triggered.connect(self.edit_slot)
        actionDelete.triggered.connect(self.delete_slot)
        menu.addAction(actionEdit)
        menu.addAction(actionDelete)
        menu.popup(self.sender().mapToGlobal(pos))

    def edit_slot(self):
        eventWidget = self.sender().parent()
        print(f'Изменение "{eventWidget.event}"')
        print('Пока нет реализации')

    def delete_slot(self):
        eventWidget = self.sender().parent()
        print(f'Удаление "{eventWidget.event}"')
        print('runtime удаление из окна не реализовано. Перезапустите приложение')
        self.eventManager.delete_event(eventWidget.event)

    def open_week_window_slot(self):
        self.weekWindow.show()
        self.hide()

    def add_event_clicked_slot(self):
        dialog = AddEventDialog(self)
        if dialog.exec() == AddEventDialog.DialogCode.Accepted:
            event = self.eventManager.add_event(dialog.name(), dialog.date(), dialog.start_time(), dialog.stop_time(), dialog.description())
            self.create_event(event, random.choice(list(EventWidget.colors.values())))

    def resizeEvent(self, event):
        for tmp in self.eventWidgets:
            self.set_event_geometry(tmp)

    def init_dicts(self):
        self.hourToLabel = {
            0: self.ui.line_1,
            1: self.ui.line_2,
            2: self.ui.line_3,
            3: self.ui.line_4,
            4: self.ui.line_5,
            5: self.ui.line_6,
            6: self.ui.line_7,
            7: self.ui.line_8,
            8: self.ui.line_9,
            9: self.ui.line_10,
            10: self.ui.line_11,
            11: self.ui.line_12,
            12: self.ui.line_13,
            13: self.ui.line_14,
            14: self.ui.line_15,
            15: self.ui.line_16,
            16: self.ui.line_17,
            17: self.ui.line_18,
            18: self.ui.line_19,
            19: self.ui.line_20,
            20: self.ui.line_21,
            21: self.ui.line_22,
            22: self.ui.line_23,
            23: self.ui.line_24,
            24: self.ui.line_25
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

