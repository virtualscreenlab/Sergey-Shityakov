from clear import delete_extra_files
from styles import *

from PyQt5 import QtWidgets
from PyQt5.Qt import *


class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('NeuroClick')
        self.setFixedSize(600, 700)
        self.setObjectName('MainWindow')

        self.next_button = QtWidgets.QPushButton(self)
        self.next_button.clicked.connect(self.next_step)
        self.next_button.setText('Next')
        self.next_button.setGeometry(480, 650, 95, 40)
        self.next_button.setStyleSheet(default_stylesheet)
        self.next_button.setEnabled(False)

        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.clicked.connect(self.back_step)
        self.back_button.setText('Back')
        self.back_button.setGeometry(30, 650, 95, 40)
        self.back_button.setStyleSheet(back_next_button_stylesheet)

        self.next_clicked = False
        self.back_clicked = False

    def closeEvent(self, event):
        if not self.next_clicked and not self.back_clicked:
            reply = QMessageBox.question \
                (self, 'Confirm exit',
                 "Quit NeuroClick?",
                 QMessageBox.Yes,
                 QMessageBox.No)
            if reply == QMessageBox.Yes:
                delete_extra_files()
                event.accept()
            else:
                event.ignore()
        self.next_clicked = False
        self.back_clicked = False

    def back_step(self):
        pass

    def next_step(self):
        pass

    def activate_next(self, process=False):
        self.next_button.setEnabled(True)
        if process:
            self.next_button.setStyleSheet(back_next_process_button_stylesheet)
        else:
            self.next_button.setStyleSheet(back_next_button_stylesheet)
