from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Калькулятор")
        self.setGeometry(300, 250, 400, 600)

        self.label = QLabel('', self)

        self.button_1 = create_button_1()
        self.button_2 = create_button_2()
        self.button_3 = create_button_3()
        self.button_4 = create_button_4()
        self.button_5 = create_button_5()
        self.button_6 = create_button_6()
        self.button_7 = create_button_7()
        self.button_8 = create_button_8()
        self.button_9 = create_button_9()
        self.button_0 = create_button_0()

        self.plus = create_plus()
        self.minus = create_minus()
        self.mult = create_mult()
        self.divide = create_divide()
        self.open_braket = create_open_braket()
        self.close_braket = create_close_braket()
        self.erase = create_erase()    # удалить все символы
        self.delete = create_delete()  # удалить один символ
        self.equal = create_equal()
        self.percent = create_percent()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
