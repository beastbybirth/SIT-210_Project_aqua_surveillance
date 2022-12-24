import sys
from time import sleep
from datetime import datetime
from functools import partial
from settings import Setting
from main_window import main_guiWindow
from welcome_gui import welcome_screen
import app_functions as app_functions
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
    QStackedWidget
)
import pyrebase

class Device():
    def __init__(self, name, phval_address, tds_address) -> None:
        self.name = name
        self.phval = 1.0
        self.tds = 1.0
        self.phval_address = phval_address
        self.tds_address = tds_address
        self.issafe = True
        self.warningText = "\n\n\n\n         Water quality is not\n          up to the mark !  "
        
    def check_value(self):
        if(self.tds > 800 or self.phval > 13):
            current_datetime = datetime.now()
            current_time = current_datetime.strftime("%H:%M:%S")
            self.warningText = "\n\n\n\n         Water quality is not\n          up to the mark !\n         Time: "
            self.warningText += current_time
            self.issafe = False


class Devices():
    def __init__(self) -> None:
        self.devices_list = []

    def add_device(self, name, phval_address,tds_address):
        device = Device(name, phval_address, tds_address)
        self.devices_list.append(device)
        return device
    
    def get_device(self, device_name):
        for device in self.devices_list:
            if (device.name == device_name):
                return device
