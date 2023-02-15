import saving_options
from base_window import BaseWindow
from styles import *

from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont


class IsomersSelectionWindow(BaseWindow):
    def __init__(self, start_window, reagent_2_process_window, reaction_type):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.start_window = start_window
        self.reagent_2_process_window = reagent_2_process_window
        self.reaction_type = reaction_type

        self.isomer_1_4_check = QRadioButton('Generate only 1,4-isomer', self)
        self.isomer_1_4_check.setGeometry(200, 240, 253, 40)
        self.isomer_1_4_check.setFont(QFont('OldEnglish', 9))
        self.isomer_1_4_check.setStyleSheet(radio_button_stylesheet)
        self.isomer_1_4_check.toggled.connect(self.checked_1_4)

        self.isomer_1_5_check = QRadioButton('Generate only 1,5-isomer', self)
        self.isomer_1_5_check.setGeometry(200, 270, 253, 40)
        self.isomer_1_5_check.setFont(QFont('OldEnglish', 9))
        self.isomer_1_5_check.setStyleSheet(radio_button_stylesheet)
        self.isomer_1_5_check.toggled.connect(self.checked_1_5)

        self.both_isomers_check = QRadioButton('Generate both isomers', self)
        self.both_isomers_check.setGeometry(200, 300, 253, 40)
        self.both_isomers_check.setFont(QFont('OldEnglish', 9))
        self.both_isomers_check.setStyleSheet(radio_button_stylesheet)
        self.both_isomers_check.toggled.connect(self.checked_both)

        self.selected_isomers = []

    def checked_1_4(self):
        self.selected_isomers.clear()
        if self.isomer_1_4_check.isChecked():
            self.selected_isomers.append('1_4')
            self.isomer_1_5_check.setChecked(False)
            self.both_isomers_check.setChecked(False)
            self.next_button.setEnabled(True)
            self.next_button.setStyleSheet(back_next_button_stylesheet)

    def checked_1_5(self):
        self.selected_isomers.clear()
        if self.isomer_1_5_check.isChecked():
            self.selected_isomers.append('1_5')
            self.isomer_1_4_check.setChecked(False)
            self.both_isomers_check.setChecked(False)
            self.next_button.setEnabled(True)
            self.next_button.setStyleSheet(back_next_button_stylesheet)

    def checked_both(self):
        self.selected_isomers.clear()
        if self.both_isomers_check.isChecked():
            self.selected_isomers.append('both')
            self.isomer_1_4_check.setChecked(False)
            self.isomer_1_5_check.setChecked(False)
            self.next_button.setEnabled(True)
            self.next_button.setStyleSheet(back_next_button_stylesheet)

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.reagent_2_process_window.show()

    def next_step(self):
        if len(self.selected_isomers) != 1:
            raise Exception('Please, select exactly one configuration of isomers')
        self.next_clicked = True
        self.close()

        self.isaving_options_window = saving_options.SavingOptionsWindow(self.start_window, self, self.reaction_type,
                                                                         self.selected_isomers[0])
        self.isaving_options_window.show()
