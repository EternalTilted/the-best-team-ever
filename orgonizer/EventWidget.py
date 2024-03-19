from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QPoint

from Event import Event


class EventWidget(QLabel):
    colors = {
        'red': 'DC143C',
        'pink': 'C71585',
        'orange': 'FF4500',
        'green': '008000'
    }

    doubleClickedSignal = pyqtSignal()
    contextRequest = pyqtSignal(QPoint)

    def __init__(self, event, *__args, **kwargs):
        super().__init__(*__args)
        self.event = event

        alpha = 50
        color = kwargs['color'] if 'color' in kwargs else self.colors['pink']
        self.setStyleSheet("""
        EventWidget
        {
            background: #%1%2;
            padding-left: 5px;
        }
        EventWidget:hover
        {
            background:#AA%2;
        }
        """.replace('%1', str(alpha)).replace('%2', color))

    def mousePressEvent(self, ev):
        if ev.button() == Qt.RightButton:
            self.contextRequest.emit(ev.pos())

    def mouseDoubleClickEvent(self, a0):
        if a0.button() == Qt.LeftButton:
            self.doubleClickedSignal.emit()
