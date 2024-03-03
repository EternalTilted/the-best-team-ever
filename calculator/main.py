from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QVBoxLayout

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Калькулятор")
        self.setGeometry(300, 250, 400, 580)
        self.setFixedSize(400, 580)

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

        self.plus = self.create_plus()
        self.minus = self.create_minus()
        self.mult = self.create_mult()
        self.divide = self.create_divide()
        self.open_bracket = self.create_open_bracket()
        self.close_bracket = self.create_close_bracket()
        self.erase = self.create_erase()    # удалить все символы
        self.delete = self.create_delete()  # удалить один символ
        self.equal = self.create_equal()
        self.percent = self.create_percent()

        self.central_widget = QtWidgets.QWidget()
        self.prepare_ui()

    def prepare_ui(self):
        self.setStyleSheet('background: #111; color: #fff; font-size: 32px')
        self.setCentralWidget(self.central_widget)
        vbox = QVBoxLayout(self.central_widget)
        grid = QGridLayout()
        self.setLayout(vbox)
        vbox.addWidget(self.label)
        vbox.addLayout(grid)

        grid.addWidget(self.plus, 4, 3)
        grid.addWidget(self.minus, 3, 3)
        grid.addWidget(self.mult, 2, 3)
        grid.addWidget(self.divide, 1, 3)
        grid.addWidget(self.open_bracket, 1, 1)
        grid.addWidget(self.close_bracket, 1, 2)
        grid.addWidget(self.erase, 1, 0)
        grid.addWidget(self.delete, 2, 0)
        grid.addWidget(self.equal, 5, 3)
        grid.addWidget(self.percent, 2, 2)

    def on_plus_clicked_slot(self):
        self.label.setText(self.label.text() + '+')

    def create_plus(self):
        tmp = QPushButton('+', self)
        tmp.clicked.connect(self.on_plus_clicked_slot)
        self.setButtonStyleSheet(tmp, type='operation')
        return tmp

    def on_minus_clicked_slot(self):
        self.label.setText(self.label.text() + '-')

    def create_minus(self):
        tmp = QPushButton('-', self)
        tmp.clicked.connect(self.on_minus_clicked_slot)
        self.setButtonStyleSheet(tmp, type='operation')
        return tmp

    def on_mult_clicked_slot(self):
        self.label.setText(self.label.text() + '*')

    def create_mult(self):
        tmp = QPushButton('*', self)
        tmp.clicked.connect(self.on_mult_clicked_slot)
        self.setButtonStyleSheet(tmp, type='operation')
        return tmp

    def on_divide_clicked_slot(self):
        self.label.setText(self.label.text() + '/')

    def create_divide(self):
        tmp = QPushButton('/', self)
        tmp.clicked.connect(self.on_divide_clicked_slot)
        self.setButtonStyleSheet(tmp, type='operation')
        return tmp

    def on_open_bracket_clicked_slot(self):
        self.label.setText(self.label.text() + '(')

    def create_open_bracket(self):
        tmp = QPushButton('(', self)
        tmp.clicked.connect(self.on_open_bracket_clicked_slot)
        self.setButtonStyleSheet(tmp, type='operation')
        return tmp

    def on_close_bracket_clicked_slot(self):
        self.label.setText(self.label.text() + ')')

    def create_close_bracket(self):
        tmp = QPushButton(')', self)
        tmp.clicked.connect(self.on_close_bracket_clicked_slot)
        self.setButtonStyleSheet(tmp, type='operation')
        return tmp

    def on_erase_clicked_slot(self):
        self.label.setText('')

    def create_erase(self):
        tmp = QPushButton('C', self)
        tmp.clicked.connect(self.on_erase_clicked_slot)
        self.setButtonStyleSheet(tmp, type='delete')
        return tmp

    def on_delete_clicked_slot(self):
        self.label.setText(self.label.text()[:-1])

    def create_delete(self):
        tmp = QPushButton('CE', self)
        tmp.clicked.connect(self.on_delete_clicked_slot)
        self.setButtonStyleSheet(tmp, type='delete')
        return tmp

    def on_equal_clicked_slot(self):
        if self.label.text() == '':
            self.label.setText('0')
            return

        if self.label.text() == 'SyntaxError':
            return

        try:
            tmp = self.label.text().replace('%', '/100')
            self.label.setText(str(eval(tmp)))
        except SyntaxError:
            self.label.setText('SyntaxError')

    def create_equal(self):
        tmp = QPushButton('=', self)
        tmp.clicked.connect(self.on_equal_clicked_slot)
        self.setButtonStyleSheet(tmp, type='equal')
        return tmp

    def on_percent_clicked_slot(self):
        self.label.setText(self.label.text() + '%')

    def create_percent(self):
        tmp = QPushButton('%', self)
        tmp.clicked.connect(self.on_percent_clicked_slot)
        self.setButtonStyleSheet(tmp, type='operation')
        return tmp

    def setButtonStyleSheet(self, button, type='number'):
        color = '#63d53d'
        background = '#171717'
        if type == 'number':
            color = '#f9f9f9'
            background = '#171717'
        elif type == 'delete':
            color = '#f56464'
            background = '#171717'
        elif type == 'operation':
            color = '#63d53d'
            background = '#171717'
        elif type == 'equal':
            color = '#f9f9f9'
            background = '#318507'

        size = int(self.size().width() / 4 * 0.9)
        button.setFixedSize(size, size)
        styleSheet =str(
        '''
            QPushButton {
                color:  %color;
                font-size: 26px;
                font-weight: bold;
                border: 0px;
                border-radius: %radiuspx;
                border-style: outset;
                background: %background;
                padding: 5px;
                }
            
            QPushButton:hover {
                color:  #171717;
                background: #ccc;
                }
            
            QPushButton:pressed {
                color:  #171717;
                border-style: inset;
                background: #318507;
            }''').replace('%radius', str(size//2)).replace('%color', color).replace('%background', background)
        button.setStyleSheet(styleSheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
