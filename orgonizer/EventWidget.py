from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal

from Event import Event


class EventWidget(QLabel):
    colors = {
        'red': 'DC143C',
        'pink': 'C71585',
        'orange': 'FF4500',
        'green': '008000'
    }

    clickedSignal = pyqtSignal()

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
        self.clickedSignal.emit()
