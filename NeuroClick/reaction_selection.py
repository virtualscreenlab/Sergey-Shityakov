import reagent_1_uploading
from base_window import BaseWindow
from styles import *

import sys

from PyQt5.QtWidgets import QComboBox, QLabel, QRadioButton, QApplication
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont


class ReactionSelectionWindow(BaseWindow):
    def __init__(self, logo_window):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.info_label = QLabel(self)
        self.info_label.setGeometry(130, 160, 273, 40)
        self.info_label.setText('Select the reaction of your interest:')
        self.info_label.setFont(QFont('OldEnglish', 9))
        self.info_label.setStyleSheet(headline_stylesheet)

        self.click_reactions_check = QRadioButton('Click reactions', self)
        self.click_reactions_check.setGeometry(130, 190, 253, 40)
        self.click_reactions_check.setFont(QFont('OldEnglish', 9))
        self.click_reactions_check.setStyleSheet(radio_button_stylesheet)
        self.click_reactions_check.toggled.connect(
            lambda: self.checked(self.click_reactions_check, self.click_reactions_combobox))

        self.click_reactions_combobox = QComboBox(self)
        self.click_reactions_combobox.addItem('None')
        self.click_reactions_combobox.addItem('Azide-alkyne cycloaddition')
        self.click_reactions_combobox.addItem('Diels-Alder')
        self.click_reactions_combobox.setGeometry(315, 200, 180, 25)
        self.click_reactions_combobox.activated[str].connect(self.combobox_changed)
        self.click_reactions_combobox.setVisible(False)

        self.logo_window = logo_window
        self.reaction_type = 'None'

    def checked(self, button, combobox):
        if button.isChecked():
            combobox.setVisible(True)
        else:
            combobox.setVisible(False)
            self.next_button.setEnabled(False)
            self.next_button.setStyleSheet(default_stylesheet)

    def combobox_changed(self, text):
        self.reaction_type = text
        if self.reaction_type != 'None':
            self.next_button.setEnabled(True)
            self.next_button.setStyleSheet(back_next_button_stylesheet)
        print(self.reaction_type)

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.logo_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        self.uploading_window = reagent_1_uploading.Reagent1Window(self, self.reaction_type)
        self.uploading_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReactionSelectionWindow()
    window.show()
    sys.exit(app.exec_())
