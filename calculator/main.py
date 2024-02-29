from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Калькулятор")
        self.setGeometry(300, 250, 400, 600)

        self.label = QLabel('', self)

        self.button_1 = button_1()
        self.button_2 = button_2()
        self.button_3 = button_3()
        self.button_4 = button_4()
        self.button_5 = button_5()
        self.button_6 = button_6()
        self.button_7 = button_7()
        self.button_8 = button_8()
        self.button_9 = button_9()
        self.button_0 = button_0()

        self.plus = plus()
        self.minus = minus()
        self.mult = mult()
        self.divide = divide()
        self.open_braket = open_braket()
        self.close_braket = close_braket()
        self.erase = erase()    # удалить все символы
        self.delete = delete()  # удалить один символ
        self.equal = equal()
        self.percent = percent()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
