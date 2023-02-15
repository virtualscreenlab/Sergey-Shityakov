import more_descriptors_selection
from base_window import BaseWindow
from styles import *

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QLabel, QTextEdit, QCheckBox


class DruglikenessSelectionWindow(BaseWindow):
    def __init__(self, start_window, phramacokinetics_selection_window, cols_to_use, threshold_cols, gi_level,
                 saving_format,
                 more_descriptors_selection_window=None):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.info_label = QLabel(self)
        self.info_label.setGeometry(165, 190, 253, 40)
        self.info_label.setText('Select druglikeness filters:')
        self.info_label.setFont(QFont('OldEnglish', 9))
        self.info_label.setStyleSheet(headline_stylesheet)

        self.Lipinski_check = QCheckBox(self)
        self.Lipinski_check.setGeometry(165, 220, 253, 40)
        self.Lipinski_check.setText('Lipinski')
        self.Lipinski_check.setFont(QFont('OldEnglish', 9))
        self.Lipinski_check.setStyleSheet(checkbox_stylesheet)
        self.Lipinski_check.toggled.connect(
            lambda: self.check(self.Lipinski_check, self.Lipinski_label, self.Lipinski_edit, 'Lipinski #violations'))

        self.Ghose_check = QCheckBox(self)
        self.Ghose_check.setGeometry(165, 250, 253, 40)
        self.Ghose_check.setText('Ghose')
        self.Ghose_check.setFont(QFont('OldEnglish', 9))
        self.Ghose_check.setStyleSheet(checkbox_stylesheet)
        self.Ghose_check.toggled.connect(
            lambda: self.check(self.Ghose_check, self.Ghose_label, self.Ghose_edit, 'Ghose #violations'))

        self.Veber_check = QCheckBox(self)
        self.Veber_check.setGeometry(165, 280, 253, 40)
        self.Veber_check.setText('Veber')
        self.Veber_check.setFont(QFont('OldEnglish', 9))
        self.Veber_check.setStyleSheet(checkbox_stylesheet)
        self.Veber_check.toggled.connect(
            lambda: self.check(self.Veber_check, self.Veber_label, self.Veber_edit, 'Veber #violations'))

        self.Egan_check = QCheckBox(self)
        self.Egan_check.setGeometry(165, 310, 253, 40)
        self.Egan_check.setText('Egan')
        self.Egan_check.setFont(QFont('OldEnglish', 9))
        self.Egan_check.setStyleSheet(checkbox_stylesheet)
        self.Egan_check.toggled.connect(
            lambda: self.check(self.Egan_check, self.Egan_label, self.Egan_edit, 'Egan #violations'))

        self.Muegge_check = QCheckBox(self)
        self.Muegge_check.setGeometry(165, 340, 253, 40)
        self.Muegge_check.setText('Muegge')
        self.Muegge_check.setFont(QFont('OldEnglish', 9))
        self.Muegge_check.setStyleSheet(checkbox_stylesheet)
        self.Muegge_check.toggled.connect(
            lambda: self.check(self.Muegge_check, self.Muegge_label, self.Muegge_edit, 'Muegge #violations'))

        self.Lipinski_label = QLabel(self)
        self.Lipinski_label.setGeometry(325, 225, 85, 30)
        self.Lipinski_label.setText('max violations')
        self.Lipinski_label.setVisible(False)

        self.Ghose_label = QLabel(self)
        self.Ghose_label.setGeometry(325, 255, 85, 30)
        self.Ghose_label.setText('max violations')
        self.Ghose_label.setVisible(False)

        self.Veber_label = QLabel(self)
        self.Veber_label.setGeometry(325, 285, 85, 30)
        self.Veber_label.setText('max violations')
        self.Veber_label.setVisible(False)

        self.Egan_label = QLabel(self)
        self.Egan_label.setGeometry(325, 315, 85, 30)
        self.Egan_label.setText('max violations')
        self.Egan_label.setVisible(False)

        self.Muegge_label = QLabel(self)
        self.Muegge_label.setGeometry(325, 345, 85, 30)
        self.Muegge_label.setText('max violations')
        self.Muegge_label.setVisible(False)

        self.Lipinski_edit = QTextEdit(self)
        self.Lipinski_edit.setGeometry(420, 225, 40, 28)
        self.Lipinski_edit.setText('0')
        self.Lipinski_edit.setVisible(False)

        self.Ghose_edit = QTextEdit(self)
        self.Ghose_edit.setGeometry(420, 255, 40, 28)
        self.Ghose_edit.setText('0')
        self.Ghose_edit.setVisible(False)

        self.Veber_edit = QTextEdit(self)
        self.Veber_edit.setGeometry(420, 285, 40, 28)
        self.Veber_edit.setText('0')
        self.Veber_edit.setVisible(False)

        self.Egan_edit = QTextEdit(self)
        self.Egan_edit.setGeometry(420, 315, 40, 28)
        self.Egan_edit.setText('0')
        self.Egan_edit.setVisible(False)

        self.Muegge_edit = QTextEdit(self)
        self.Muegge_edit.setGeometry(420, 345, 40, 28)
        self.Muegge_edit.setText('0')
        self.Muegge_edit.setVisible(False)

        self.start_window = start_window
        self.pharmacokinetics_selection_window = phramacokinetics_selection_window
        self.cols_to_use = cols_to_use
        self.threshold_cols = threshold_cols
        self.saving_format = saving_format
        self.violations_cols = {}
        self.gi_level = gi_level
        self.more_descriptors_selection_window = more_descriptors_selection_window

        self.next_button.setEnabled(True)
        self.next_button.setStyleSheet(back_next_button_stylesheet)

    def check(self, button, label, edit, col):
        if button.isChecked():
            label.setVisible(True)
            edit.setVisible(True)
            self.cols_to_use.append(col)
        else:
            self.cols_to_use.remove(col)
            label.setVisible(False)
            edit.setVisible(False)

    def get_threshold_values(self):
        self.violations_cols['Lipinski #violations'] = (
            int(self.Lipinski_edit.toPlainText()))
        self.violations_cols['Ghose #violations'] = (
            int(self.Ghose_edit.toPlainText()))
        self.violations_cols['Veber #violations'] = (
            int(self.Veber_edit.toPlainText()))
        self.violations_cols['Egan #violations'] = (
            int(self.Egan_edit.toPlainText()))
        self.violations_cols['Muegge #violations'] = (
            int(self.Muegge_edit.toPlainText()))

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.pharmacokinetics_selection_window.show()

    def next_step(self):
        self.next_clicked = True
        self.get_threshold_values()
        self.more_descriptors_selection_window = more_descriptors_selection.MoreDescriptorsSelectionWindow(
            self.start_window, self, self.cols_to_use, self.threshold_cols, self.violations_cols, self.gi_level,
            self.saving_format)
        self.close()
        self.more_descriptors_selection_window.show()
