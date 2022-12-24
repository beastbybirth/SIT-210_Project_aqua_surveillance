from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QLabel
)

import app_functions as app_functions
from settings import Setting

class welcome_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.make_label()
        self.setGeometry(0, 0, 800, 600)
        self.setStyleSheet("QWidget{\nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 142, 175, 255), stop:0.845771 rgba(255, 255, 255, 255))}")
        self.show()

    def make_label(self):
        self.project_name = QLabel("Aqua Surveillance", self)
        self.project_name.setGeometry(280, 90, 461, 71)
        self.project_name.setStyleSheet("background-color:rgba(0,0,0,0);\ncolor:rgb(15, 98, 138);\nfont: 40pt,bold;")
        
        self.welcome_label = QLabel("Welcome  !", self)
        self.welcome_label.setGeometry(350, 380, 181, 51)
        self.welcome_label.setStyleSheet("background-color:rgba(0,0,0,0);\ncolor:rgb(15, 98, 138);\nfont:24pt,bold;")
