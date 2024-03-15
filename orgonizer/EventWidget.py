from PyQt5.QtWidgets import QLabel


class EventWidget(QLabel):
    colors = {
        'red': 'DC143C',
        'pink': 'C71585',
        'orange': 'FF4500',
        'green': '008000'
    }

    def __init__(self, *__args, **kwargs):
        super().__init__(*__args)

        alpha = 50
        color = kwargs['color'] if 'color' in kwargs else self.colors['pink']
        self.setStyleSheet("""
        EventWidget
        {
            background: #%1%2;
            padding-left: 5px;
        }
        """.replace('%1', str(alpha)).replace('%2', color))
