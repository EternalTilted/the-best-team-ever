from PyQt5.QtWidgets import QApplication
from DayWindow import DayWindow

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = DayWindow()
    window.show()
    window.test()

    app.exec()
