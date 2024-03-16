from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class WeekWindow(QMainWindow):
    def __init__(self, dayWindow, *args):
        super().__init__(*args)
        self.ui = uic.loadUi('WeekWindow.ui', self)
        self.ui.pbDay.clicked.connect(self.open_day_window_slot)
        self.dayWindow = dayWindow

    def open_day_window_slot(self):
        self.dayWindow.show()
        self.hide()
