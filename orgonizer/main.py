from PyQt5.QtWidgets import QApplication
from DayWindow import DayWindow

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open("style.qss").read())
    window = DayWindow()
    window.show()
    window.init_events()

    app.exec()
