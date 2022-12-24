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
import devices as devices
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

class Complaint():
    def __init__(self, device, complaint_id) -> None:
        self.device = device
        self.resolvedTime = None
        self.beginTime = datetime.now()
        self.isresolved = False
        self.complaint_id = complaint_id
        
    def resolved(self):
        self.resolvedTime = datetime.now()
        self.isresolved = True

class Complaints():
    def __init__(self) -> None:
        self.complaints_list = []
        self.complaints_resolved_list = []
        self.currentTime = datetime.now()
        self.latestId = 23
			
    def add_complaint(self, device):
        complaint = Complaint(device, self.latestId)
        self.complaints_list.append(complaint)
        self.latestId += 1
        return complaint
        
    def resolve_complaint(self, complaint_id):
        index,complaint = self.get_complaint(complaint_id)
        if(index != -1):
            del self.complaints_list[index]
            self.complaints_resolved_list.append(complaint)
            complaint.resolved()
					
    def get_complaint(self, complaint_id):
        for index, complaint in enumerate(self.complaints_list):
            if (complaint_id == complaint.complaint_id):
                return index, complaint
        return -1,-1
