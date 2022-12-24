from PyQt5.QtCore import Qt
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
    QLabel,
    QTextBrowser
)

import app_functions as app_functions
from settings import Setting

class main_guiWindow(QMainWindow):
    def __init__(self, setting):
        super().__init__()
        self.setting = setting
        self.setGeometry(100, 100, 800, 650)
        self.setWindowTitle(self.setting.win_title)
        # self.setGeometry(self.setting.win_x, self.setting.win_y, self.setting.win_height, self.setting.win_breadth)
        # self.VLayout1 = QVBoxLayout()
        self.HLayout1 = QHBoxLayout()
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setStyleSheet("QWidget#centralWidget{background-image : url(photos/bg1.jpeg)}")
        self.setCentralWidget(self.centralWidget)
        self.init_elements()
        self.set_geometry()
        self.set_style_sheet()
        self.connect_buttons()
        self.warning_label.setHidden(True)
        self.resolve_device_button.setEnabled(False)
        self.currentDevice = None
        self.currentComplaint = None

        
    def init_elements(self):
        self.device_list = QListWidget(self.centralWidget)
        self.complaints_list = QListWidget(self.centralWidget)
        self.device_data_list = QListWidget(self.centralWidget)
        self.complaints_data_list = QListWidget(self.centralWidget)
        #****************************
        self.device_label = QLabel("Devices", self.centralWidget)
        self.complaint_label = QLabel("Complaints",  self.centralWidget)
        self.last_review_label = QLabel("Last Maintained: ", self.centralWidget)
        self.last_review_data_label = QLabel("12 Dec, 2022", self.centralWidget)
        self.reading_data_label_tds = QLabel("TDS: -", self.centralWidget)
        self.reading_data_label_phval = QLabel("Ph: -", self.centralWidget)
        self.reading_label = QLabel("Reading: ", self.centralWidget)
        self.location_label = QLabel("Location: ", self.centralWidget)
        self.date_issued_label = QLabel("Date Issued: ", self.centralWidget)
        self.time_issued_label = QLabel("Time Issued: ", self.centralWidget)
        self.status_label = QLabel("Status: Unresolved", self.centralWidget)
        self.warning_label = QTextBrowser(self.centralWidget)
        self.warning_label.setText("\n\n\n\n\n         Water quality is not\n          up to the mark !  ")
        #*******************
        self.more_button = QPushButton("More...", self.centralWidget)
        self.view_history_button = QPushButton("View History", self.centralWidget)
        self.resolved_button = QPushButton("Resolved", self.centralWidget)
        self.ignore_button = QPushButton("Ignore", self.centralWidget)  
        self.resolve_device_button = QPushButton("Resolved", self.centralWidget)

    def set_geometry(self):
        self.device_label.setGeometry(120,50,91,31)
        self.complaint_label.setGeometry(120,280,101,31)
        self.last_review_label.setGeometry(420,100,131,20)
        self.last_review_data_label.setGeometry(420, 120, 191, 21)
        self.reading_label.setGeometry(420,150,131,20)
        self.reading_data_label_tds.setGeometry(420, 170, 191, 20)
        self.reading_data_label_phval.setGeometry(420, 190, 191, 21)
        self.location_label.setGeometry(410,330,157,20)
        self.date_issued_label.setGeometry(410,360,241,20)
        self.time_issued_label.setGeometry(410,390,241,20)
        self.status_label.setGeometry(410,420,141,20)
        self.warning_label.setGeometry(670, 70, 251, 201)        
        """tHIS IS warning"""

        self.more_button.setGeometry(530,220,81,20)
        self.view_history_button.setGeometry(120,470,121,21)
        self.ignore_button.setGeometry(530,450,111,25)
        self.resolved_button.setGeometry(410, 450, 111, 25)
        self.resolve_device_button.setGeometry(420, 220,101,21)
        
        self.device_list.setGeometry(121,90,231,161)
        self.complaints_list.setGeometry(120,320,231,151)
        self.device_data_list.setGeometry(400,90,261,161)
        self.complaints_data_list.setGeometry(400,320,261,161)

        
    def set_style_sheet(self):
        self.device_label.setStyleSheet("background-color: rgb(240, 164, 226);\nborder-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n\nfont: 75 12pt 'Ubuntu';\nborder-radius:5;")
        self.complaint_label.setStyleSheet("background-color: rgb(240, 164, 226);\nborder-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n\nfont: 75 12pt 'Ubuntu';\nborder-radius:5;")
        self.last_review_label.setStyleSheet("font: 25 11pt 'URW Bookman';\nbackground-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(231, 170, 255), stop:1 rgba(255, 255, 255, 255));\nborder-radius:5;\n\n")
        self.reading_label.setStyleSheet("font: 25 11pt 'URW Bookman';\nbackground-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(231, 170, 255), stop:1 rgba(255, 255, 255, 255));\nborder-radius:5;\n\n")
        self.last_review_data_label.setStyleSheet("background-color: rgb(255, 255, 255);\nfont: 25 11pt 'URW Bookman';\nborder-radius:3;\n")
        self.reading_data_label_tds.setStyleSheet("background-color: rgb(255, 255, 255);\nfont: 25 11pt 'URW Bookman';\nborder-radius:3;\n")
        self.reading_data_label_phval.setStyleSheet("background-color: rgb(255, 255, 255);\nfont: 25 11pt 'URW Bookman';\nborder-radius:3;\n")
        self.warning_label.setStyleSheet("color:rgb(0, 0, 0);\nbackground-image: url(photos/war1.jpeg);\nfont: 75 12pt 'Ubuntu';\nborder: 3px solid rgb(255,255,255);\n\n")
        self.location_label.setStyleSheet("font: 15 11pt 'URW Bookman';\nbackground-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(127, 179, 249, 255), stop:1 rgba(255, 255, 255, 255));\nborder-radius:5;\n\n")
        self.date_issued_label.setStyleSheet("font: 25 11pt 'URW Bookman';\nbackground-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(127, 179, 249, 255), stop:1 rgba(255, 255, 255, 255));\nborder-radius:9;")
        self.time_issued_label.setStyleSheet("font: 25 11pt 'URW Bookman';\nbackground-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(127, 179, 249, 255), stop:1 rgba(255, 255, 255, 255));\nborder-radius:9;")        
        self.status_label.setStyleSheet("font: 25 11pt 'URW Bookman';\nbackground-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(127, 179, 249, 255), stop:1 rgba(255, 255, 255, 255));\nborder-radius:5;\n\n\n")
        
        self.more_button.setStyleSheet("background-color:rgb(153, 193, 241);\nborder-radius:7;")
        self.view_history_button.setStyleSheet("background-color:rgb(153, 193, 241);\nborder-radius:7;")
        self.ignore_button.setStyleSheet("background-color:rgb(153, 193, 241);\nborder-radius:7;")
        self.resolved_button.setStyleSheet("background-color: rgb(92, 221, 114);\nborder-radius:7;\n")
        self.resolve_device_button.setStyleSheet("background-color: rgb(92, 221, 114);\nborder-radius:7;\n")
        self.warning_label.setStyleSheet("color:rgb(0, 0, 0);\nbackground-image: url(photos/war1.jpeg);\nfont: 75 12pt 'Ubuntu';\nborder: 3px solid rgb(255,255,255);\n\n")
        
        self.device_list.setStyleSheet("font: 25 11pt 'URW Bookman';\nbackground-color:rgb(128, 255, 213);\nborder-radius:9;")
        self.complaints_list.setStyleSheet("font: 25 11pt 'URW Bookman';\nbackground-color:rgb(128, 255, 213);\nborder-radius:9;")
        self.device_data_list.setStyleSheet("font: 25 11pt 'URW Bookman';\nbackground-color:rgb(128, 255, 213);\nborder-radius:9;")
        self.complaints_data_list.setStyleSheet("font: 25 11pt 'URW Bookman';\nbackground-color:rgb(128, 255, 213);\nborder-radius:9;")

    def connect_buttons(self):
        self.resolve_device_button.clicked.connect(self.resolve_device_complaint)

    def resolve_complaint(self):
        self.complaints_list.takeItem(self.complaints_list.currentRow())

    def show_warning(self, device):
        self.currentDevice = device
        self.show_device_data(1)
        
    def resolve_device_complaint(self):
        self.currentDevice.issafe = True

    def show_complaint(self, complaint):
        self.currentComplaint = complaint
        self.show_complaint_data(1)

            
    def show_device_data(self, n):
            if (n == 1):
                texttds = "TDS: " + str(self.currentDevice.tds)
                textphval = "Ph: " + str(self.currentDevice.phval)
                self.reading_data_label_tds.setText(texttds)
                self.reading_data_label_phval.setText(textphval)
                self.warning_label.setHidden(self.currentDevice.issafe)
                self.resolve_device_button.setEnabled(not self.currentDevice.issafe)
                self.warning_label.setText(self.currentDevice.warningText)
            elif(n == -1):
                texttds = "TDS: "
                textphval = "Ph: "
                self.reading_data_label_tds.setText(texttds)
                self.reading_data_label_phval.setText(textphval)
                self.warning_label.setHidden(True)
                self.resolve_device_button.setEnabled(False)
                self.warning_label.setText("")
    
    def show_complaint_data(self, n):
            if (n == 1):
                text_location = "Location: " + str(self.currentComplaint.device.name)
                text_date_issued = "Date Issued: " + self.currentComplaint.beginTime.strftime("%d/%m/%Y")
                text_time_issued = "Time Issued: " + self.currentComplaint.beginTime.strftime("%H:%M:%S")
        
                self.location_label.setText(text_location)
                self.date_issued_label.setText(text_date_issued)
                self.time_issued_label.setText(text_time_issued)
            elif(n == -1):
                text_location = "Location: " 
                text_date_issued = "Date Issued: "
                text_time_issued = "Time Issued: "
        
                self.location_label.setText(text_location)
                self.date_issued_label.setText(text_date_issued)
                self.time_issued_label.setText(text_time_issued)


