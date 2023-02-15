import druglikeness_selection
from base_window import BaseWindow
from styles import *

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QLabel, QCheckBox, QComboBox


class PharmacokineticsSelectionWindow(BaseWindow):
    def __init__(self, start_window, logS_selection_window, cols_to_use, threshold_cols, saving_format,
                 druglikeness_selection_window=None):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.info_label = QLabel(self)
        self.info_label.setGeometry(200, 160, 280, 40)
        self.info_label.setText('Select pharmacokinetics descriptors:')
        self.info_label.setFont(QFont('OldEnglish', 9))
        self.info_label.setStyleSheet(headline_stylesheet)

        self.gi_check = QCheckBox(self)
        self.gi_check.setGeometry(200, 190, 253, 40)
        self.gi_check.setText('GI absorption')
        self.gi_check.setFont(QFont('OldEnglish', 9))
        self.gi_check.setStyleSheet(checkbox_stylesheet)
        self.gi_check.toggled.connect(self.check_gi)

        self.gi_combobox = QComboBox(self)
        self.gi_combobox.addItem('High')
        self.gi_combobox.addItem('Low')
        self.gi_combobox.setGeometry(330, 200, 60, 25)
        self.gi_combobox.activated[str].connect(self.gi_combobox_changed)
        self.gi_combobox.setVisible(False)

        self.pgp_check = QCheckBox(self)
        self.pgp_check.setGeometry(200, 220, 253, 40)
        self.pgp_check.setText('P-gp substrate')
        self.pgp_check.setFont(QFont('OldEnglish', 9))
        self.pgp_check.setStyleSheet(checkbox_stylesheet)
        self.pgp_check.toggled.connect(lambda: self.check(self.pgp_check, 'Pgp substrate'))

        self.cyp1a2_check = QCheckBox(self)
        self.cyp1a2_check.setGeometry(200, 250, 253, 40)
        self.cyp1a2_check.setText('CYP1A2 inhibitor')
        self.cyp1a2_check.setFont(QFont('OldEnglish', 9))
        self.cyp1a2_check.setStyleSheet(checkbox_stylesheet)
        self.cyp1a2_check.toggled.connect(lambda: self.check(self.cyp1a2_check, 'CYP1A2 inhibitor'))

        self.cyp2c19_check = QCheckBox(self)
        self.cyp2c19_check.setGeometry(200, 280, 253, 40)
        self.cyp2c19_check.setText('CYP2C19 inhibitor')
        self.cyp2c19_check.setFont(QFont('OldEnglish', 9))
        self.cyp2c19_check.setStyleSheet(checkbox_stylesheet)
        self.cyp2c19_check.toggled.connect(lambda: self.check(self.cyp2c19_check, 'CYP2C19 inhibitor'))

        self.cyp2c9_check = QCheckBox(self)
        self.cyp2c9_check.setGeometry(200, 310, 253, 40)
        self.cyp2c9_check.setText('CYP2C9 inhibitor')
        self.cyp2c9_check.setFont(QFont('OldEnglish', 9))
        self.cyp2c9_check.setStyleSheet(checkbox_stylesheet)
        self.cyp2c9_check.toggled.connect(lambda: self.check(self.cyp2c9_check, 'CYP2C9 inhibitor'))

        self.cyp2d6_check = QCheckBox(self)
        self.cyp2d6_check.setGeometry(200, 340, 253, 40)
        self.cyp2d6_check.setText('CYP2D6 inhibitor')
        self.cyp2d6_check.setFont(QFont('OldEnglish', 9))
        self.cyp2d6_check.setStyleSheet(checkbox_stylesheet)
        self.cyp2d6_check.toggled.connect(lambda: self.check(self.cyp2d6_check, 'CYP2D6 inhibitor'))

        self.cyp3a4_check = QCheckBox(self)
        self.cyp3a4_check.setGeometry(200, 370, 253, 40)
        self.cyp3a4_check.setText('CYP3A4 inhibitor')
        self.cyp3a4_check.setFont(QFont('OldEnglish', 9))
        self.cyp3a4_check.setStyleSheet(checkbox_stylesheet)
        self.cyp3a4_check.toggled.connect(lambda: self.check(self.cyp3a4_check, 'CYP3A4 inhibitor'))

        self.bbb_check = QCheckBox(self)
        self.bbb_check.setGeometry(200, 400, 253, 40)
        self.bbb_check.setText('BBB permeant')
        self.bbb_check.setFont(QFont('OldEnglish', 9))
        self.bbb_check.setStyleSheet(checkbox_stylesheet)
        self.bbb_check.toggled.connect(lambda: self.check(self.bbb_check, 'BBB permeant'))

        self.gi_level = None

        self.start_window = start_window
        self.logS_selection_window = logS_selection_window
        self.cols_to_use = cols_to_use
        self.threshold_cols = threshold_cols
        self.saving_format = saving_format
        self.druglikeness_selection_window = druglikeness_selection_window

        self.next_button.setEnabled(True)
        self.next_button.setStyleSheet(back_next_button_stylesheet)

    def check(self, button, col):
        if button.isChecked():
            self.cols_to_use.append(col)
        else:
            self.cols_to_use.remove(col)

    def check_gi(self):
        if self.gi_check.isChecked():
            self.gi_combobox.setVisible(True)
            self.gi_combobox.setItemText(0, 'High')
            self.cols_to_use.append('GI absorption')
            self.gi_level = 'High'
        else:
            self.gi_combobox.setVisible(False)
            self.cols_to_use.remove('GI absorption')

    def gi_combobox_changed(self, text):
        self.gi_level = text

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.logS_selection_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        self.druglikeness_selection_window = druglikeness_selection.DruglikenessSelectionWindow(
            self.start_window, self, self.cols_to_use, self.threshold_cols, self.gi_level, self.saving_format)
        self.druglikeness_selection_window.show()
