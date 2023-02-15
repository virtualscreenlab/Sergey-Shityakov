import calculations
from base_window import BaseWindow
from styles import *

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QRadioButton, QLabel


class SavingOptionsWindow(BaseWindow):
    def __init__(self, start_window, previous_window, reaction_type, selected_isomers=None):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.start_window = start_window
        self.previous_window = previous_window
        self.reaction_type = reaction_type
        self.selected_isomers = selected_isomers
        self.saving_format = 'txt'

        self.info_label = QLabel(self)
        self.info_label.setGeometry(180, 230, 253, 40)
        self.info_label.setText('How to save an output file?')
        self.info_label.setFont(QFont('OldEnglish', 9))
        self.info_label.setStyleSheet(headline_stylesheet)

        self.txt_check = QRadioButton('.txt format (molecules only)', self)
        self.txt_check.setGeometry(180, 260, 253, 40)
        self.txt_check.setFont(QFont('OldEnglish', 9))
        self.txt_check.setStyleSheet(radio_button_stylesheet)
        self.txt_check.setChecked(True)
        self.txt_check.toggled.connect(self.checked_txt)

        self.csv_check = QRadioButton('.csv format (molecules and descriptors)', self)
        self.csv_check.setGeometry(180, 290, 283, 50)
        self.csv_check.setFont(QFont('OldEnglish', 9))
        self.csv_check.setStyleSheet(radio_button_stylesheet)
        self.csv_check.toggled.connect(self.checked_csv)

        self.next_button.setEnabled(True)
        self.next_button.setStyleSheet(back_next_button_stylesheet)

    def checked_txt(self):
        if self.txt_check.isChecked():
            self.saving_format = 'txt'
            self.csv_check.setChecked(False)

    def checked_csv(self):
        if self.csv_check.isChecked():
            self.saving_format = 'csv'
            self.txt_check.setChecked(False)

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.previous_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        self.calculations_window = calculations.CalculationsWindow(self.start_window, self, self.selected_isomers,
                                                                   self.reaction_type, self.saving_format)
        self.calculations_window.show()
