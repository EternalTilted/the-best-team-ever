from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QDate

from EventManager import EventManager
from EventWidget import EventWidget
import random


class WeekWindow(QMainWindow):
    def __init__(self, dayWindow, *args):
        super().__init__(*args)
        self.ui = uic.loadUi('WeekWindow.ui', self)
        self.dayWindow = dayWindow
        self.hourToLabelList = [{}]
        self.dayNumberToButton = {}
        self.init_dicts()

        for button in self.dayNumberToButton.values():
            button.clicked.connect(self.day_changed_slot)

        self.eventWidgets = []
        self.eventManager = EventManager()

    def resizeEvent(self, event):
        for tmp in self.eventWidgets:
            self.set_event_geometry(tmp)

    def day_changed_slot(self):
        self.dayWindow.currentDayNumber = list(self.dayNumberToButton.keys())[list(self.dayNumberToButton.values()).index(self.sender())]
        self.dayWindow.currentDay = QDate.currentDate().addDays(self.dayWindow.currentDayNumber - QDate.currentDate().dayOfWeek())
        self.dayWindow.update_days_style()
        self.dayWindow.clear_events()
        self.dayWindow.init_events()
        self.dayWindow.show()
        self.hide()

    def clear_events(self):
        for event in self.eventWidgets:
            event.deleteLater()
        self.eventWidgets.clear()

    def init_events(self):
        currDay = QDate.currentDate()
        startDay = currDay.addDays(1 - currDay.dayOfWeek())
        stopDay = currDay.addDays(7 - currDay.dayOfWeek())
        for event in self.eventManager.get_by_interval(startDay, stopDay):
            self.create_event(event)

    def create_event(self, event):
        color = random.choice(list(EventWidget.colors.values()))
        text = f'<b>{event.name}</b><br/>{event.description}'
        tmp = EventWidget(event, text, self, color=color)
        self.set_event_geometry(tmp)

        self.eventWidgets.append(tmp)
        tmp.show()

    def set_event_geometry(self, tmp):
        dayIndex = tmp.event.date.dayOfWeek()
        hour_height = (self.hourToLabelList[dayIndex][tmp.event.start_time.hour() + 1].pos().y() -
                       self.hourToLabelList[dayIndex][tmp.event.start_time.hour()].pos().y())

        x_pos = self.hourToLabelList[dayIndex][tmp.event.start_time.hour()].pos().x() + 10
        y_pos = (self.hourToLabelList[dayIndex][tmp.event.start_time.hour()].pos().y() +
                 self.hourToLabelList[dayIndex][tmp.event.start_time.hour()].height() // 2 +
                 round(hour_height * tmp.event.start_time.minute() / 60) +
                 self.ui.menuBar.height())
        y_stop = (self.hourToLabelList[dayIndex][tmp.event.stop_time.hour()].pos().y() +
                  self.hourToLabelList[dayIndex][tmp.event.stop_time.hour()].height() // 2 +
                  round(hour_height * tmp.event.stop_time.minute() / 60) +
                  self.ui.menuBar.height())
        height = max(y_stop - y_pos, 20)
        width = self.hourToLabelList[dayIndex][tmp.event.start_time.hour()].width() - 20
        tmp.setGeometry(x_pos, y_pos, width, height)

    def init_dicts(self):
        self.hourToLabelList.append({
            0: self.ui.line_1,
            1: self.ui.line_2,
            2: self.ui.line_3,
            3: self.ui.line_4,
            4: self.ui.line_5,
            5: self.ui.line_6,
            6: self.ui.line_7,
            7: self.ui.line_8,
            8: self.ui.line_9,
            9: self.ui.line_10,
            10: self.ui.line_11,
            11: self.ui.line_12,
            12: self.ui.line_13,
            13: self.ui.line_14,
            14: self.ui.line_15,
            15: self.ui.line_16,
            16: self.ui.line_17,
            17: self.ui.line_18,
            18: self.ui.line_19,
            19: self.ui.line_20,
            20: self.ui.line_21,
            21: self.ui.line_22,
            22: self.ui.line_23,
            23: self.ui.line_24,
            24: self.ui.line_25
        })

        self.hourToLabelList.append({
            0: self.ui.line_31,
            1: self.ui.line_32,
            2: self.ui.line_33,
            3: self.ui.line_34,
            4: self.ui.line_35,
            5: self.ui.line_36,
            6: self.ui.line_37,
            7: self.ui.line_38,
            8: self.ui.line_39,
            9: self.ui.line_40,
            10: self.ui.line_41,
            11: self.ui.line_42,
            12: self.ui.line_43,
            13: self.ui.line_44,
            14: self.ui.line_45,
            15: self.ui.line_46,
            16: self.ui.line_47,
            17: self.ui.line_48,
            18: self.ui.line_49,
            19: self.ui.line_50,
            20: self.ui.line_51,
            21: self.ui.line_52,
            22: self.ui.line_53,
            23: self.ui.line_54,
            24: self.ui.line_55
        })

        self.hourToLabelList.append({
            0: self.ui.line_61,
            1: self.ui.line_62,
            2: self.ui.line_63,
            3: self.ui.line_64,
            4: self.ui.line_65,
            5: self.ui.line_66,
            6: self.ui.line_67,
            7: self.ui.line_68,
            8: self.ui.line_69,
            9: self.ui.line_70,
            10: self.ui.line_71,
            11: self.ui.line_72,
            12: self.ui.line_73,
            13: self.ui.line_74,
            14: self.ui.line_75,
            15: self.ui.line_76,
            16: self.ui.line_77,
            17: self.ui.line_78,
            18: self.ui.line_79,
            19: self.ui.line_80,
            20: self.ui.line_81,
            21: self.ui.line_82,
            22: self.ui.line_83,
            23: self.ui.line_84,
            24: self.ui.line_85
        })

        self.hourToLabelList.append({
            0: self.ui.line_91,
            1: self.ui.line_92,
            2: self.ui.line_93,
            3: self.ui.line_94,
            4: self.ui.line_95,
            5: self.ui.line_96,
            6: self.ui.line_97,
            7: self.ui.line_98,
            8: self.ui.line_99,
            9: self.ui.line_100,
            10: self.ui.line_101,
            11: self.ui.line_102,
            12: self.ui.line_103,
            13: self.ui.line_104,
            14: self.ui.line_105,
            15: self.ui.line_106,
            16: self.ui.line_107,
            17: self.ui.line_108,
            18: self.ui.line_109,
            19: self.ui.line_110,
            20: self.ui.line_111,
            21: self.ui.line_112,
            22: self.ui.line_113,
            23: self.ui.line_114,
            24: self.ui.line_115
        })

        self.hourToLabelList.append({
            0: self.ui.line_121,
            1: self.ui.line_122,
            2: self.ui.line_123,
            3: self.ui.line_124,
            4: self.ui.line_125,
            5: self.ui.line_126,
            6: self.ui.line_127,
            7: self.ui.line_128,
            8: self.ui.line_129,
            9: self.ui.line_130,
            10: self.ui.line_131,
            11: self.ui.line_132,
            12: self.ui.line_133,
            13: self.ui.line_134,
            14: self.ui.line_135,
            15: self.ui.line_136,
            16: self.ui.line_137,
            17: self.ui.line_138,
            18: self.ui.line_139,
            19: self.ui.line_140,
            20: self.ui.line_141,
            21: self.ui.line_142,
            22: self.ui.line_143,
            23: self.ui.line_144,
            24: self.ui.line_145
        })

        self.hourToLabelList.append({
            0: self.ui.line_151,
            1: self.ui.line_152,
            2: self.ui.line_153,
            3: self.ui.line_154,
            4: self.ui.line_155,
            5: self.ui.line_156,
            6: self.ui.line_157,
            7: self.ui.line_158,
            8: self.ui.line_159,
            9: self.ui.line_160,
            10: self.ui.line_161,
            11: self.ui.line_162,
            12: self.ui.line_163,
            13: self.ui.line_164,
            14: self.ui.line_165,
            15: self.ui.line_166,
            16: self.ui.line_167,
            17: self.ui.line_168,
            18: self.ui.line_169,
            19: self.ui.line_170,
            20: self.ui.line_171,
            21: self.ui.line_172,
            22: self.ui.line_173,
            23: self.ui.line_174,
            24: self.ui.line_175
        })

        self.hourToLabelList.append({
            0: self.ui.line_181,
            1: self.ui.line_182,
            2: self.ui.line_183,
            3: self.ui.line_184,
            4: self.ui.line_185,
            5: self.ui.line_186,
            6: self.ui.line_187,
            7: self.ui.line_188,
            8: self.ui.line_189,
            9: self.ui.line_190,
            10: self.ui.line_191,
            11: self.ui.line_192,
            12: self.ui.line_193,
            13: self.ui.line_194,
            14: self.ui.line_195,
            15: self.ui.line_196,
            16: self.ui.line_197,
            17: self.ui.line_198,
            18: self.ui.line_199,
            19: self.ui.line_200,
            20: self.ui.line_201,
            21: self.ui.line_202,
            22: self.ui.line_203,
            23: self.ui.line_204,
            24: self.ui.line_205
        })

        self.dayNumberToButton = {
            1: self.ui.pbDay1,
            2: self.ui.pbDay2,
            3: self.ui.pbDay3,
            4: self.ui.pbDay4,
            5: self.ui.pbDay5,
            6: self.ui.pbDay6,
            7: self.ui.pbDay7
        }