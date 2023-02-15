import logS_selection
from base_window import BaseWindow
from styles import *

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QLabel, QTextEdit, QCheckBox


class LogPSelectionWindow(BaseWindow):
    def __init__(self, start_window, physical_properties_selection_window, cols_to_use, threshold_cols, saving_format,
                 logS_selection_window=None):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.info_label = QLabel(self)
        self.info_label.setGeometry(165, 190, 253, 40)
        self.info_label.setText('Select logP descriptors: ')
        self.info_label.setFont(QFont('OldEnglish', 9))
        self.info_label.setStyleSheet(headline_stylesheet)

        self.ilogP_check = QCheckBox(self)
        self.ilogP_check.setGeometry(165, 220, 253, 40)
        self.ilogP_check.setText('iLOGP')
        self.ilogP_check.setFont(QFont('OldEnglish', 9))
        self.ilogP_check.setStyleSheet(checkbox_stylesheet)
        self.ilogP_check.toggled.connect(
            lambda: self.check(self.ilogP_check, self.ilogP_lower_threshold_label, self.ilogP_lower_threshold_edit,
                               self.ilogP_upper_threshold_label, self.ilogP_upper_threshold_edit, 'iLOGP'))

        self.xlogP3_check = QCheckBox(self)
        self.xlogP3_check.setGeometry(165, 255, 253, 40)
        self.xlogP3_check.setText('XLOGP3')
        self.xlogP3_check.setFont(QFont('OldEnglish', 9))
        self.xlogP3_check.setStyleSheet(checkbox_stylesheet)
        self.xlogP3_check.toggled.connect(
            lambda: self.check(self.xlogP3_check, self.xlogP3_lower_threshold_label, self.xlogP3_lower_threshold_edit,
                               self.xlogP3_upper_threshold_label, self.xlogP3_upper_threshold_edit, 'XLOGP3'))

        self.wlogP_check = QCheckBox(self)
        self.wlogP_check.setGeometry(165, 290, 253, 40)
        self.wlogP_check.setText('WLOGP')
        self.wlogP_check.setFont(QFont('OldEnglish', 9))
        self.wlogP_check.setStyleSheet(checkbox_stylesheet)
        self.wlogP_check.toggled.connect(
            lambda: self.check(self.wlogP_check, self.wlogP_lower_threshold_label, self.wlogP_lower_threshold_edit,
                               self.wlogP_upper_threshold_label, self.wlogP_upper_threshold_edit, 'WLOGP'))

        self.mlogP_check = QCheckBox(self)
        self.mlogP_check.setGeometry(165, 325, 253, 40)
        self.mlogP_check.setText('MLOGP')
        self.mlogP_check.setFont(QFont('OldEnglish', 9))
        self.mlogP_check.setStyleSheet(checkbox_stylesheet)
        self.mlogP_check.toggled.connect(
            lambda: self.check(self.mlogP_check, self.mlogP_lower_threshold_label, self.mlogP_lower_threshold_edit,
                               self.mlogP_upper_threshold_label, self.mlogP_upper_threshold_edit, 'MLOGP'))

        self.SILICOSIT_check = QCheckBox(self)
        self.SILICOSIT_check.setGeometry(165, 360, 253, 40)
        self.SILICOSIT_check.setText('SILICOS-IT logP')
        self.SILICOSIT_check.setFont(QFont('OldEnglish', 9))
        self.SILICOSIT_check.setStyleSheet(checkbox_stylesheet)
        self.SILICOSIT_check.toggled.connect(
            lambda: self.check(self.SILICOSIT_check, self.SILICOSIT_lower_threshold_label,
                               self.SILICOSIT_lower_threshold_edit,
                               self.SILICOSIT_upper_threshold_label, self.SILICOSIT_upper_threshold_edit,
                               'Silicos-IT Log P'))

        self.consensus_check = QCheckBox(self)
        self.consensus_check.setGeometry(165, 395, 253, 40)
        self.consensus_check.setText('Consensus logP')
        self.consensus_check.setFont(QFont('OldEnglish', 9))
        self.consensus_check.setStyleSheet(checkbox_stylesheet)
        self.consensus_check.toggled.connect(
            lambda: self.check(self.consensus_check, self.consensus_lower_threshold_label,
                               self.consensus_lower_threshold_edit, self.consensus_upper_threshold_label,
                               self.consensus_upper_threshold_edit, 'Consensus Log P'))

        self.ilogP_lower_threshold_label = QLabel(self)
        self.ilogP_lower_threshold_label.setGeometry(325, 225, 70, 30)
        self.ilogP_lower_threshold_label.setText('from')
        self.ilogP_lower_threshold_label.setVisible(False)

        self.xlogP3_lower_threshold_label = QLabel(self)
        self.xlogP3_lower_threshold_label.setGeometry(325, 260, 70, 30)
        self.xlogP3_lower_threshold_label.setText('from')
        self.xlogP3_lower_threshold_label.setVisible(False)

        self.wlogP_lower_threshold_label = QLabel(self)
        self.wlogP_lower_threshold_label.setGeometry(325, 295, 70, 30)
        self.wlogP_lower_threshold_label.setText('from')
        self.wlogP_lower_threshold_label.setVisible(False)

        self.mlogP_lower_threshold_label = QLabel(self)
        self.mlogP_lower_threshold_label.setGeometry(325, 330, 70, 30)
        self.mlogP_lower_threshold_label.setText('from')
        self.mlogP_lower_threshold_label.setVisible(False)

        self.SILICOSIT_lower_threshold_label = QLabel(self)
        self.SILICOSIT_lower_threshold_label.setGeometry(325, 365, 70, 30)
        self.SILICOSIT_lower_threshold_label.setText('from')
        self.SILICOSIT_lower_threshold_label.setVisible(False)

        self.consensus_lower_threshold_label = QLabel(self)
        self.consensus_lower_threshold_label.setGeometry(325, 400, 70, 30)
        self.consensus_lower_threshold_label.setText('from')
        self.consensus_lower_threshold_label.setVisible(False)

        self.ilogP_lower_threshold_edit = QTextEdit(self)
        self.ilogP_lower_threshold_edit.setGeometry(356, 225, 40, 28)
        self.ilogP_lower_threshold_edit.setText('0')
        self.ilogP_lower_threshold_edit.setVisible(False)

        self.xlogP3_lower_threshold_edit = QTextEdit(self)
        self.xlogP3_lower_threshold_edit.setGeometry(356, 260, 40, 28)
        self.xlogP3_lower_threshold_edit.setText('0')
        self.xlogP3_lower_threshold_edit.setVisible(False)

        self.wlogP_lower_threshold_edit = QTextEdit(self)
        self.wlogP_lower_threshold_edit.setGeometry(356, 295, 40, 28)
        self.wlogP_lower_threshold_edit.setText('0')
        self.wlogP_lower_threshold_edit.setVisible(False)

        self.mlogP_lower_threshold_edit = QTextEdit(self)
        self.mlogP_lower_threshold_edit.setGeometry(356, 330, 40, 28)
        self.mlogP_lower_threshold_edit.setText('0')
        self.mlogP_lower_threshold_edit.setVisible(False)

        self.SILICOSIT_lower_threshold_edit = QTextEdit(self)
        self.SILICOSIT_lower_threshold_edit.setGeometry(356, 365, 40, 28)
        self.SILICOSIT_lower_threshold_edit.setText('0')
        self.SILICOSIT_lower_threshold_edit.setVisible(False)

        self.consensus_lower_threshold_edit = QTextEdit(self)
        self.consensus_lower_threshold_edit.setGeometry(356, 400, 40, 28)
        self.consensus_lower_threshold_edit.setText('0')
        self.consensus_lower_threshold_edit.setVisible(False)

        self.ilogP_upper_threshold_label = QLabel(self)
        self.ilogP_upper_threshold_label.setGeometry(401, 225, 70, 30)
        self.ilogP_upper_threshold_label.setText('to')
        self.ilogP_upper_threshold_label.setVisible(False)

        self.xlogP3_upper_threshold_label = QLabel(self)
        self.xlogP3_upper_threshold_label.setGeometry(401, 260, 70, 30)
        self.xlogP3_upper_threshold_label.setText('to')
        self.xlogP3_upper_threshold_label.setVisible(False)

        self.wlogP_upper_threshold_label = QLabel(self)
        self.wlogP_upper_threshold_label.setGeometry(401, 295, 70, 30)
        self.wlogP_upper_threshold_label.setText('to')
        self.wlogP_upper_threshold_label.setVisible(False)

        self.mlogP_upper_threshold_label = QLabel(self)
        self.mlogP_upper_threshold_label.setGeometry(401, 330, 70, 30)
        self.mlogP_upper_threshold_label.setText('to')
        self.mlogP_upper_threshold_label.setVisible(False)

        self.SILICOSIT_upper_threshold_label = QLabel(self)
        self.SILICOSIT_upper_threshold_label.setGeometry(401, 365, 70, 30)
        self.SILICOSIT_upper_threshold_label.setText('to')
        self.SILICOSIT_upper_threshold_label.setVisible(False)

        self.consensus_upper_threshold_label = QLabel(self)
        self.consensus_upper_threshold_label.setGeometry(401, 400, 70, 30)
        self.consensus_upper_threshold_label.setText('to')
        self.consensus_upper_threshold_label.setVisible(False)

        self.ilogP_upper_threshold_edit = QTextEdit(self)
        self.ilogP_upper_threshold_edit.setGeometry(420, 225, 40, 28)
        self.ilogP_upper_threshold_edit.setText('20')
        self.ilogP_upper_threshold_edit.setVisible(False)

        self.xlogP3_upper_threshold_edit = QTextEdit(self)
        self.xlogP3_upper_threshold_edit.setGeometry(420, 260, 40, 28)
        self.xlogP3_upper_threshold_edit.setText('20')
        self.xlogP3_upper_threshold_edit.setVisible(False)

        self.wlogP_upper_threshold_edit = QTextEdit(self)
        self.wlogP_upper_threshold_edit.setGeometry(420, 295, 40, 28)
        self.wlogP_upper_threshold_edit.setText('20')
        self.wlogP_upper_threshold_edit.setVisible(False)

        self.mlogP_upper_threshold_edit = QTextEdit(self)
        self.mlogP_upper_threshold_edit.setGeometry(420, 330, 40, 28)
        self.mlogP_upper_threshold_edit.setText('20')
        self.mlogP_upper_threshold_edit.setVisible(False)

        self.SILICOSIT_upper_threshold_edit = QTextEdit(self)
        self.SILICOSIT_upper_threshold_edit.setGeometry(420, 365, 40, 28)
        self.SILICOSIT_upper_threshold_edit.setText('20')
        self.SILICOSIT_upper_threshold_edit.setVisible(False)

        self.consensus_upper_threshold_edit = QTextEdit(self)
        self.consensus_upper_threshold_edit.setGeometry(420, 400, 40, 28)
        self.consensus_upper_threshold_edit.setText('20')
        self.consensus_upper_threshold_edit.setVisible(False)

        self.start_window = start_window
        self.physical_properties_selection_window = physical_properties_selection_window
        self.saving_format = saving_format
        self.cols_to_use = cols_to_use
        self.threshold_cols = threshold_cols

        self.logS_selection_window = logS_selection_window

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

    def get_threshold_values(self):
        self.threshold_cols['iLOGP'] = (
            float(self.ilogP_lower_threshold_edit.toPlainText()), float(self.ilogP_upper_threshold_edit.toPlainText()))
        self.threshold_cols['XLOGP3'] = (
            float(self.xlogP3_lower_threshold_edit.toPlainText()),
            float(self.xlogP3_upper_threshold_edit.toPlainText()))
        self.threshold_cols['WLOGP'] = (
            float(self.wlogP_lower_threshold_edit.toPlainText()), float(self.wlogP_upper_threshold_edit.toPlainText()))
        self.threshold_cols['MLOGP'] = (
            float(self.mlogP_lower_threshold_edit.toPlainText()), float(self.mlogP_upper_threshold_edit.toPlainText()))
        self.threshold_cols['Silicos-IT Log P'] = (
            float(self.SILICOSIT_lower_threshold_edit.toPlainText()),
            float(self.SILICOSIT_upper_threshold_edit.toPlainText()))
        self.threshold_cols['Consensus Log P'] = (
            float(self.consensus_lower_threshold_edit.toPlainText()),
            float(self.consensus_upper_threshold_edit.toPlainText()))

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.physical_properties_selection_window.show()

    def next_step(self):
        self.next_clicked = True
        self.get_threshold_values()

        self.logS_selection_window = logS_selection.LogSSelectionWindow(self.start_window, self, self.cols_to_use,
                                                                        self.threshold_cols, self.saving_format)
        self.close()
        self.logS_selection_window.show()

