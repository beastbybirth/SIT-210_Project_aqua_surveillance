from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QHBoxLayout
)

def add_to_device_list(devices, gui_win):
    gui_win.device_list.addItem(devices.name)

def add_complaints(gui_win):
    complaint = "Complaint No. " + str(gui_win.complaints_list.count() + 1)
    gui_win.complaints_list.addItem(complaint)

