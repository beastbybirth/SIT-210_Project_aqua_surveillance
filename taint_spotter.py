#setting = Setting object.

import sys
from time import sleep
from functools import partial
from settings import Setting
from main_window import main_guiWindow
from welcome_gui import welcome_screen
import app_functions as app_functions
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
import devices as devices
import complaints as complaints
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

setting = Setting()
devicess = devices.Devices()
complaintss = complaints.Complaints()
#setting up the database
firebase = pyrebase.initialize_app(setting.config)  
db = firebase.database()

pycalcApp = QApplication(sys.argv)
main_Widget = QStackedWidget()

gui_win = main_guiWindow(setting)
welcome_gui = welcome_screen()
# gui_win.make_buttons()
# gui_win.show()
main_Widget.addWidget(welcome_gui)
main_Widget.addWidget(gui_win)
main_Widget.setGeometry(50, 50, 1000, 600)

timer_init = QTimer()
timer_database = QTimer()
timer_label = QTimer()

def resolve_complaint():
    complaint_id = gui_win.currentComplaint.complaint_id
    complaintss.resolve_complaint(complaint_id)
    gui_win.resolve_complaint()
    
def begin_timer_init():
    timer_init.start(2000)
    timer_init.timeout.connect(flip_screen)

def flip_screen():
    main_Widget.setCurrentIndex(1)
    add_device("IBN Boys", "phval", "tds")
    add_device("Square One", "phval2", "tds2")
    add_device("Edison", "phval3", "tds3")
    add_complaint("IBN Boys")
    add_complaint("IBN Boys")
    add_complaint("Square One")
    timer_init.stop()

def update_values():
    for device in devicess.devices_list:
        device.phval = db.child(device.phval_address).get().val()
        device.tds = db.child(device.tds_address).get().val()
        device.check_value()

def update_label():
    currentRowDevice = gui_win.device_list.currentRow()
    currentRowComplaint = gui_win.complaints_list.currentRow()
    """print(str(currentRow))"""
    if currentRowDevice >= 0:
        currentDevice =  devicess.devices_list[currentRowDevice]
        gui_win.show_warning(currentDevice)
    else: 
        gui_win.show_device_data(-1)
        
    if currentRowComplaint >= 0:
        currentComplaint = complaintss.complaints_list[currentRowComplaint]
        gui_win.show_complaint(currentComplaint)
    else:
        gui_win.show_complaint_data(-1)
        
def update():
    update_values()
    update_label()
def add_complaint(device_name):
    complDevice = devicess.get_device(device_name)
    complaint = complaintss.add_complaint(complDevice)
    gui_win.complaints_list.addItem(str(complaint.complaint_id))

def add_device(device_name,phval_address,tds_address):
    device = devicess.add_device(device_name,phval_address,tds_address)
    gui_win.device_list.addItem(device.name)


def begin_timer_label():
    timer_label.start(200)
    timer_label.timeout.connect(update)
    
gui_win.resolved_button.clicked.connect(resolve_complaint)
begin_timer_init()

begin_timer_label()

main_Widget.show()

sys.exit(pycalcApp.exec())
