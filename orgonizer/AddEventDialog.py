from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import QDate

from PyQt5.QtCore import Qt


class AddEventDialog(QDialog):
    def __init__(self, *args):
        super().__init__(*args)
        self.ui = uic.loadUi('AddEventDialog.ui', self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.init_connections()

    def init_connections(self):
        self.ui.timeEditStart.editingFinished.connect(self.start_time_edit_slot)
        self.ui.timeEditStop.editingFinished.connect(self.stop_time_edit_slot)

    def name(self):
        return self.ui.leName.text()

    def date(self):
        return self.ui.dateEdit.date()

    def start_time(self):
        return self.ui.timeEditStart.time()

    def stop_time(self):
        return self.ui.timeEditStop.time()

    def description(self):
        return self.ui.teDescription.toPlainText()

    def start_time_edit_slot(self):
        if self.start_time() > self.stop_time():
            self.ui.timeEditStop.setTime(self.start_time())

    def stop_time_edit_slot(self):
        if self.start_time() > self.stop_time():
            self.ui.timeEditStart.setTime(self.stop_time())
