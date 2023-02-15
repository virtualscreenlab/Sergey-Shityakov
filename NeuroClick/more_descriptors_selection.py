import swissADME
from base_window import BaseWindow
from styles import *

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QLabel, QTextEdit, QCheckBox


class MoreDescriptorsSelectionWindow(BaseWindow):
    def __init__(self, start_window, druglikeness_selection_window, cols_to_use, threshold_cols, violations_cols,
                 gi_level, saving_format, swissADME_window=None):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.info_label = QLabel(self)
        self.info_label.setGeometry(155, 190, 275, 40)
        self.info_label.setText('Select even more ADME descriptors:')
        self.info_label.setFont(QFont('OldEnglish', 9))
        self.info_label.setStyleSheet(headline_stylesheet)

        self.logKp_check = QCheckBox(self)
        self.logKp_check.setGeometry(155, 220, 253, 40)
        self.logKp_check.setText('logKp')
        self.logKp_check.setFont(QFont('OldEnglish', 9))
        self.logKp_check.setStyleSheet(checkbox_stylesheet)
        self.logKp_check.toggled.connect(
            lambda: self.check(self.logKp_check, self.logKp_lower_threshold_label, self.logKp_lower_threshold_edit,
                               self.logKp_upper_threshold_label, self.logKp_upper_threshold_edit, 'log Kp (cm/s)'))

        self.ba_check = QCheckBox(self)
        self.ba_check.setGeometry(155, 255, 253, 40)
        self.ba_check.setText('Bioavailability score')
        self.ba_check.setFont(QFont('OldEnglish', 9))
        self.ba_check.setStyleSheet(checkbox_stylesheet)
        self.ba_check.toggled.connect(
            lambda: self.check(self.ba_check, self.ba_lower_threshold_label, self.ba_lower_threshold_edit,
                               self.ba_upper_threshold_label, self.ba_upper_threshold_edit, 'Bioavailability Score'))

        self.sa_check = QCheckBox(self)
        self.sa_check.setGeometry(155, 290, 253, 40)
        self.sa_check.setText('Synthetic accessibility')
        self.sa_check.setFont(QFont('OldEnglish', 9))
        self.sa_check.setStyleSheet(checkbox_stylesheet)
        self.sa_check.toggled.connect(
            lambda: self.check(self.sa_check, self.sa_lower_threshold_label, self.sa_lower_threshold_edit,
                               self.sa_upper_threshold_label, self.sa_upper_threshold_edit, 'Synthetic Accessibility'))

        self.lead_check = QCheckBox(self)
        self.lead_check.setGeometry(155, 325, 253, 40)
        self.lead_check.setText('Leadlikeness')
        self.lead_check.setFont(QFont('OldEnglish', 9))
        self.lead_check.setStyleSheet(checkbox_stylesheet)
        self.lead_check.toggled.connect(
            lambda: self.no_threshold_check(self.lead_check, self.lead_label, self.lead_edit,
                                            'Leadlikeness #violations'))

        self.PAINS_check = QCheckBox(self)
        self.PAINS_check.setGeometry(155, 360, 253, 40)
        self.PAINS_check.setText('PAINS')
        self.PAINS_check.setFont(QFont('OldEnglish', 9))
        self.PAINS_check.setStyleSheet(checkbox_stylesheet)
        self.PAINS_check.toggled.connect(
            lambda: self.no_threshold_check(self.PAINS_check, self.PAINS_label, self.PAINS_edit,
                                            'PAINS #alerts'))

        self.brenk_check = QCheckBox(self)
        self.brenk_check.setGeometry(155, 395, 253, 40)
        self.brenk_check.setText('Brenk')
        self.brenk_check.setFont(QFont('OldEnglish', 9))
        self.brenk_check.setStyleSheet(checkbox_stylesheet)
        self.brenk_check.toggled.connect(
            lambda: self.no_threshold_check(self.brenk_check, self.brenk_label, self.brenk_edit,
                                            'Brenk #alerts'))

        self.logKp_lower_threshold_label = QLabel(self)
        self.logKp_lower_threshold_label.setGeometry(330, 225, 70, 30)
        self.logKp_lower_threshold_label.setText('from')
        self.logKp_lower_threshold_label.setVisible(False)

        self.ba_lower_threshold_label = QLabel(self)
        self.ba_lower_threshold_label.setGeometry(330, 260, 70, 30)
        self.ba_lower_threshold_label.setText('from')
        self.ba_lower_threshold_label.setVisible(False)

        self.sa_lower_threshold_label = QLabel(self)
        self.sa_lower_threshold_label.setGeometry(330, 295, 70, 30)
        self.sa_lower_threshold_label.setText('from')
        self.sa_lower_threshold_label.setVisible(False)

        self.lead_label = QLabel(self)
        self.lead_label.setGeometry(330, 330, 85, 30)
        self.lead_label.setText('max violations')
        self.lead_label.setVisible(False)

        self.PAINS_label = QLabel(self)
        self.PAINS_label.setGeometry(330, 365, 85, 30)
        self.PAINS_label.setText('max violations')
        self.PAINS_label.setVisible(False)

        self.brenk_label = QLabel(self)
        self.brenk_label.setGeometry(330, 400, 85, 30)
        self.brenk_label.setText('max violations')
        self.brenk_label.setVisible(False)

        self.logKp_lower_threshold_edit = QTextEdit(self)
        self.logKp_lower_threshold_edit.setGeometry(361, 225, 40, 28)
        self.logKp_lower_threshold_edit.setText('-30')
        self.logKp_lower_threshold_edit.setVisible(False)

        self.ba_lower_threshold_edit = QTextEdit(self)
        self.ba_lower_threshold_edit.setGeometry(361, 260, 40, 28)
        self.ba_lower_threshold_edit.setText('0')
        self.ba_lower_threshold_edit.setVisible(False)

        self.sa_lower_threshold_edit = QTextEdit(self)
        self.sa_lower_threshold_edit.setGeometry(361, 295, 40, 28)
        self.sa_lower_threshold_edit.setText('1')
        self.sa_lower_threshold_edit.setVisible(False)

        self.lead_edit = QTextEdit(self)
        self.lead_edit.setGeometry(425, 330, 40, 28)
        self.lead_edit.setText('0')
        self.lead_edit.setVisible(False)

        self.PAINS_edit = QTextEdit(self)
        self.PAINS_edit.setGeometry(425, 365, 40, 28)
        self.PAINS_edit.setText('0')
        self.PAINS_edit.setVisible(False)

        self.brenk_edit = QTextEdit(self)
        self.brenk_edit.setGeometry(425, 400, 40, 28)
        self.brenk_edit.setText('0')
        self.brenk_edit.setVisible(False)

        self.logKp_upper_threshold_label = QLabel(self)
        self.logKp_upper_threshold_label.setGeometry(406, 225, 70, 30)
        self.logKp_upper_threshold_label.setText('to')
        self.logKp_upper_threshold_label.setVisible(False)

        self.ba_upper_threshold_label = QLabel(self)
        self.ba_upper_threshold_label.setGeometry(406, 260, 70, 30)
        self.ba_upper_threshold_label.setText('to')
        self.ba_upper_threshold_label.setVisible(False)

        self.sa_upper_threshold_label = QLabel(self)
        self.sa_upper_threshold_label.setGeometry(406, 295, 70, 30)
        self.sa_upper_threshold_label.setText('to')
        self.sa_upper_threshold_label.setVisible(False)

        self.logKp_upper_threshold_edit = QTextEdit(self)
        self.logKp_upper_threshold_edit.setGeometry(425, 225, 40, 28)
        self.logKp_upper_threshold_edit.setText('5')
        self.logKp_upper_threshold_edit.setVisible(False)

        self.ba_upper_threshold_edit = QTextEdit(self)
        self.ba_upper_threshold_edit.setGeometry(425, 260, 40, 28)
        self.ba_upper_threshold_edit.setText('1')
        self.ba_upper_threshold_edit.setVisible(False)

        self.sa_upper_threshold_edit = QTextEdit(self)
        self.sa_upper_threshold_edit.setGeometry(425, 295, 40, 28)
        self.sa_upper_threshold_edit.setText('10')
        self.sa_upper_threshold_edit.setVisible(False)

        self.start_window = start_window
        self.druglikeness_selection_window = druglikeness_selection_window
        self.cols_to_use = cols_to_use
        self.saving_format = saving_format
        self.gi_level = gi_level
        self.swissADME_window = swissADME_window
        self.threshold_cols = threshold_cols
        self.violations_cols = violations_cols

        self.next_button.setEnabled(True)
        self.next_button.setStyleSheet(back_next_button_stylesheet)

    def check(self, button, lower_threshold_label, lower_threshold_edit, upper_threshold_label, upper_threshold_edit,
              col):
        if button.isChecked():
            self.cols_to_use.append(col)
            lower_threshold_label.setVisible(True)
            lower_threshold_edit.setVisible(True)
            upper_threshold_label.setVisible(True)
            upper_threshold_edit.setVisible(True)
        else:
            self.cols_to_use.remove(col)
            lower_threshold_label.setVisible(False)
            lower_threshold_edit.setVisible(False)
            upper_threshold_label.setVisible(False)
            upper_threshold_edit.setVisible(False)

    def no_threshold_check(self, button, label, edit, col):
        if button.isChecked():
            label.setVisible(True)
            edit.setVisible(True)
            self.cols_to_use.append(col)
        else:
            self.cols_to_use.remove(col)
            label.setVisible(False)
            edit.setVisible(False)

    def get_threshold_values(self):
        self.threshold_cols['log Kp (cm/s)'] = (
            float(self.logKp_lower_threshold_edit.toPlainText()), float(self.logKp_upper_threshold_edit.toPlainText()))
        self.threshold_cols['Bioavailability Score'] = (
            float(self.ba_lower_threshold_edit.toPlainText()), float(self.ba_upper_threshold_edit.toPlainText()))
        self.threshold_cols['Synthetic Accessibility'] = (
            float(self.sa_lower_threshold_edit.toPlainText()), float(self.sa_upper_threshold_edit.toPlainText()))

        self.violations_cols['Leadlikeness #violations'] = (
            int(self.lead_edit.toPlainText()))
        self.violations_cols['PAINS #alerts'] = (
            int(self.PAINS_edit.toPlainText()))
        self.violations_cols['Brenk #alerts'] = (
            int(self.brenk_edit.toPlainText()))

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.druglikeness_selection_window.show()

    def next_step(self):
        self.next_clicked = True
        self.get_threshold_values()

        self.swissADME_window = swissADME.SwissADMEWindow(self.start_window, self, self.cols_to_use,
                                                          self.threshold_cols, self.violations_cols, self.gi_level,
                                                          self.saving_format)
        self.close()
        self.swissADME_window.show()
