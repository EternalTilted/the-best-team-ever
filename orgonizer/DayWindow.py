from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5 import uic

from EventWidget import EventWidget


class DayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('DayWindow.ui', self)

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

        self.events = []
        self.started = False

    def test(self):
        self.started = True
        self.createEvent((0, 0), (3, 0), '<b>Правоведение</b><br/>University', EventWidget.colors['green'])
        self.createEvent((5, 0), (6, 0), '<b>Работа</b><br/>Work', EventWidget.colors['pink'])
        self.createEvent((8, 0), (13, 0), '<b>Test</b><br/>Тест', EventWidget.colors['red'])
        self.createEvent((18, 0), (21, 0), '<b>Тест 2</b><br/>Test 2', EventWidget.colors['orange'])

    def createEvent(self, start_time, stop_time, text, color):
        tmp = EventWidget(text, self, color=color)
        y_pos = self.hourToLabel[start_time[0]].pos().y() + 10
        y_stop = self.hourToLabel[stop_time[0]].pos().y() + 10
        height = y_stop - y_pos
        width = self.width() - self.hourToLabel[start_time[0]].width() - 40
        tmp.setGeometry(50, y_pos, width, height)

        self.events.append(tmp)
        tmp.show()

    def resizeEvent(self, event):
        if not self.started:
            return
        for tmp in self.events:
            tmp.hide()
            tmp.deleteLater()

        self.events.clear()

        self.test()
        self.update()
