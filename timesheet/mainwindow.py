# coding: utf-8

import sys

from PySide import QtGui

from .utils import days_abbr, generate_time, generate_week


def main():
    app = QtGui.QApplication(sys.argv)
    
    w = MainWindow()
    w.show()
    
    sys.exit(app.exec_())


class DayWidget(QtGui.QWidget):
    def __init__(self, day, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.day = day
        self.setup_ui()

    def setup_ui(self):
        day_label = QtGui.QLabel(self.day, self)
        
        self.morning_start = QtGui.QLineEdit(self)
        self.morning_end = QtGui.QLineEdit(self)
        
        self.afternoon_start = QtGui.QLineEdit(self)
        self.afternoon_end = QtGui.QLineEdit(self)
        
        morning_layout = QtGui.QHBoxLayout()
        morning_layout.addWidget(self.morning_start)
        morning_layout.addWidget(QtGui.QLabel('-', self))
        morning_layout.addWidget(self.morning_end)
        
        afternoon_layout = QtGui.QHBoxLayout()
        afternoon_layout.addWidget(self.afternoon_start)
        afternoon_layout.addWidget(QtGui.QLabel('-', self))
        afternoon_layout.addWidget(self.afternoon_end)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(day_label)
        layout.addLayout(morning_layout)
        layout.addLayout(afternoon_layout)
        
        self.setLayout(layout)
    
    def update_time(self, morning, afternoon):
        self.morning_start.setText(morning[0])
        self.morning_end.setText(morning[1])
        
        self.afternoon_start.setText(afternoon[0])
        self.afternoon_end.setText(afternoon[1])


class MainWindow(QtGui.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        self.days = []
        days_layout = QtGui.QHBoxLayout()
        for day in days_abbr:
            daywidget = DayWidget(day, self)
            days_layout.addWidget(daywidget)
            self.days.append(daywidget)

        gen_time = QtGui.QPushButton('Generate Time')
        gen_time.clicked.connect(self.calculate_time)
        
        update_site = QtGui.QPushButton('Update Site')
        update_site.clicked.connect(self.update_site)
        
        buttons_layout = QtGui.QVBoxLayout()
        buttons_layout.addWidget(gen_time)
        buttons_layout.addWidget(update_site)
        buttons_layout.addStretch()
        
        layout = QtGui.QHBoxLayout()
        layout.addLayout(days_layout)
        layout.addLayout(buttons_layout)
        
        cw = QtGui.QWidget(self)
        cw.setLayout(layout)
        
        self.setCentralWidget(cw)

    def calculate_time(self):
        week = generate_week()
        for day, times in zip(self.days, week):
            day.update_time(*times)

    def update_site(self):
        pass
