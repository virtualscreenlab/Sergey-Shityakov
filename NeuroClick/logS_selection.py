import pharmacokinetics_selection
from base_window import BaseWindow
from styles import *

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QLabel, QTextEdit, QCheckBox


class LogSSelectionWindow(BaseWindow):
    def __init__(self, start_window, logP_selection_window, cols_to_use, threshold_cols, saving_format,
                 pharmacokinetics_selection_window=None):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.info_label = QLabel(self)
        self.info_label.setGeometry(160, 190, 265, 40)
        self.info_label.setText('Select water solubility descriptors:')
        self.info_label.setFont(QFont('OldEnglish', 9))
        self.info_label.setStyleSheet(headline_stylesheet)

        self.ESOL_check = QCheckBox(self)
        self.ESOL_check.setGeometry(160, 220, 253, 40)
        self.ESOL_check.setText('logS (ESOL)')
        self.ESOL_check.setFont(QFont('OldEnglish', 9))
        self.ESOL_check.setStyleSheet(checkbox_stylesheet)
        self.ESOL_check.toggled.connect(self.show_solubility_specifications)
        self.ESOL_check.toggled.connect(self.hide_solubility_specifications)
        self.ESOL_check.toggled.connect(
            lambda: self.check(self.ESOL_check, self.ESOL_lower_threshold_label, self.ESOL_lower_threshold_edit,
                               self.ESOL_upper_threshold_label, self.ESOL_upper_threshold_edit, 'ESOL Log S'))
        self.ESOL_check.toggled.connect(
            lambda: self.check_specification_button(self.mg_ml_button,
                                                    ['ESOL Solubility (mg/ml)', 'Ali Solubility (mg/ml)',
                                                     'Silicos-IT Solubility (mg/ml)']))
        self.ESOL_check.toggled.connect(
            lambda: self.check_specification_button(self.mol_l_button,
                                                    ['ESOL Solubility (mol/l)', 'Ali Solubility (mol/l)',
                                                     'Silicos-IT Solubility (mol/l)']))
        self.ESOL_check.toggled.connect(
            lambda: self.check_specification_button(self.class_button, ['ESOL Class', 'Ali Class', 'Silicos-IT class']))

        self.Ali_check = QCheckBox(self)
        self.Ali_check.setGeometry(160, 255, 253, 40)
        self.Ali_check.setText('LogS (Ali)')
        self.Ali_check.setFont(QFont('OldEnglish', 9))
        self.Ali_check.setStyleSheet(checkbox_stylesheet)
        self.Ali_check.toggled.connect(self.show_solubility_specifications)
        self.Ali_check.toggled.connect(self.hide_solubility_specifications)
        self.Ali_check.toggled.connect(
            lambda: self.check(self.Ali_check, self.Ali_lower_threshold_label, self.Ali_lower_threshold_edit,
                               self.Ali_upper_threshold_label, self.Ali_upper_threshold_edit, 'Ali Log S'))
        self.Ali_check.toggled.connect(
            lambda: self.check_specification_button(self.mg_ml_button,
                                                    ['ESOL Solubility (mg/ml)', 'Ali Solubility (mg/ml)',
                                                     'Silicos-IT Solubility (mg/ml)']))
        self.Ali_check.toggled.connect(
            lambda: self.check_specification_button(self.mol_l_button,
                                                    ['ESOL Solubility (mol/l)', 'Ali Solubility (mol/l)',
                                                     'Silicos-IT Solubility (mol/l)']))
        self.Ali_check.toggled.connect(
            lambda: self.check_specification_button(self.class_button, ['ESOL Class', 'Ali Class', 'Silicos-IT class']))

        self.SILICOSIT_check = QCheckBox(self)
        self.SILICOSIT_check.setGeometry(160, 290, 253, 40)
        self.SILICOSIT_check.setText('logS (SILICOS-IT)')
        self.SILICOSIT_check.setFont(QFont('OldEnglish', 9))
        self.SILICOSIT_check.setStyleSheet(checkbox_stylesheet)
        self.SILICOSIT_check.toggled.connect(self.show_solubility_specifications)
        self.SILICOSIT_check.toggled.connect(self.hide_solubility_specifications)
        self.SILICOSIT_check.toggled.connect(
            lambda: self.check(self.SILICOSIT_check, self.SILICOSIT_lower_threshold_label,
                               self.SILICOSIT_lower_threshold_edit, self.SILICOSIT_upper_threshold_label,
                               self.SILICOSIT_upper_threshold_edit, 'Silicos-IT LogSw'))
        self.SILICOSIT_check.toggled.connect(
            lambda: self.check_specification_button(self.mg_ml_button,
                                                    ['ESOL Solubility (mg/ml)', 'Ali Solubility (mg/ml)',
                                                     'Silicos-IT Solubility (mg/ml)']))
        self.SILICOSIT_check.toggled.connect(
            lambda: self.check_specification_button(self.mol_l_button,
                                                    ['ESOL Solubility (mol/l)', 'Ali Solubility (mol/l)',
                                                     'Silicos-IT Solubility (mol/l)']))
        self.SILICOSIT_check.toggled.connect(
            lambda: self.check_specification_button(self.class_button, ['ESOL Class', 'Ali Class', 'Silicos-IT class']))

        self.ESOL_lower_threshold_label = QLabel(self)
        self.ESOL_lower_threshold_label.setGeometry(320, 225, 70, 30)
        self.ESOL_lower_threshold_label.setText('from')
        self.ESOL_lower_threshold_label.setVisible(False)

        self.Ali_lower_threshold_label = QLabel(self)
        self.Ali_lower_threshold_label.setGeometry(320, 260, 70, 30)
        self.Ali_lower_threshold_label.setText('from')
        self.Ali_lower_threshold_label.setVisible(False)

        self.SILICOSIT_lower_threshold_label = QLabel(self)
        self.SILICOSIT_lower_threshold_label.setGeometry(320, 295, 70, 30)
        self.SILICOSIT_lower_threshold_label.setText('from')
        self.SILICOSIT_lower_threshold_label.setVisible(False)

        self.ESOL_lower_threshold_edit = QTextEdit(self)
        self.ESOL_lower_threshold_edit.setGeometry(351, 225, 40, 28)
        self.ESOL_lower_threshold_edit.setText('-30')
        self.ESOL_lower_threshold_edit.setVisible(False)

        self.Ali_lower_threshold_edit = QTextEdit(self)
        self.Ali_lower_threshold_edit.setGeometry(351, 260, 40, 28)
        self.Ali_lower_threshold_edit.setText('-30')
        self.Ali_lower_threshold_edit.setVisible(False)

        self.SILICOSIT_lower_threshold_edit = QTextEdit(self)
        self.SILICOSIT_lower_threshold_edit.setGeometry(351, 295, 40, 28)
        self.SILICOSIT_lower_threshold_edit.setText('-30')
        self.SILICOSIT_lower_threshold_edit.setVisible(False)

        self.ESOL_upper_threshold_label = QLabel(self)
        self.ESOL_upper_threshold_label.setGeometry(396, 225, 70, 30)
        self.ESOL_upper_threshold_label.setText('to')
        self.ESOL_upper_threshold_label.setVisible(False)

        self.Ali_upper_threshold_label = QLabel(self)
        self.Ali_upper_threshold_label.setGeometry(396, 260, 70, 30)
        self.Ali_upper_threshold_label.setText('to')
        self.Ali_upper_threshold_label.setVisible(False)

        self.SILICOSIT_upper_threshold_label = QLabel(self)
        self.SILICOSIT_upper_threshold_label.setGeometry(396, 295, 70, 30)
        self.SILICOSIT_upper_threshold_label.setText('to')
        self.SILICOSIT_upper_threshold_label.setVisible(False)

        self.ESOL_upper_threshold_edit = QTextEdit(self)
        self.ESOL_upper_threshold_edit.setGeometry(415, 225, 40, 28)
        self.ESOL_upper_threshold_edit.setText('5')
        self.ESOL_upper_threshold_edit.setVisible(False)

        self.Ali_upper_threshold_edit = QTextEdit(self)
        self.Ali_upper_threshold_edit.setGeometry(415, 260, 40, 28)
        self.Ali_upper_threshold_edit.setText('5')
        self.Ali_upper_threshold_edit.setVisible(False)

        self.SILICOSIT_upper_threshold_edit = QTextEdit(self)
        self.SILICOSIT_upper_threshold_edit.setGeometry(415, 295, 40, 28)
        self.SILICOSIT_upper_threshold_edit.setText('5')
        self.SILICOSIT_upper_threshold_edit.setVisible(False)

        self.mg_ml_button = QCheckBox(self)
        self.mg_ml_button.setGeometry(160, 325, 253, 40)
        self.mg_ml_button.setText('Get solubility in mg/ml')
        self.mg_ml_button.setFont(QFont('OldEnglish', 9))
        self.mg_ml_button.setStyleSheet(checkbox_stylesheet)
        self.mg_ml_button.toggled.connect(
            lambda: self.check_specification_button(self.mg_ml_button,
                                                    ['ESOL Solubility (mg/ml)', 'Ali Solubility (mg/ml)',
                                                     'Silicos-IT Solubility (mg/ml)']))
        self.mg_ml_button.setVisible(False)

        self.mol_l_button = QCheckBox(self)
        self.mol_l_button.setGeometry(160, 355, 253, 40)
        self.mol_l_button.setText('Get solubility in mol/l')
        self.mol_l_button.setFont(QFont('OldEnglish', 9))
        self.mol_l_button.setStyleSheet(checkbox_stylesheet)
        self.mol_l_button.toggled.connect(
            lambda: self.check_specification_button(self.mol_l_button,
                                                    ['ESOL Solubility (mol/l)', 'Ali Solubility (mol/l)',
                                                     'Silicos-IT Solubility (mol/l)']))
        self.mol_l_button.setVisible(False)

        self.class_button = QCheckBox(self)
        self.class_button.setGeometry(160, 385, 253, 40)
        self.class_button.setText('Show solubility class')
        self.class_button.setFont(QFont('OldEnglish', 9))
        self.class_button.setStyleSheet(checkbox_stylesheet)
        self.class_button.toggled.connect(
            lambda: self.check_specification_button(self.class_button, ['ESOL Class', 'Ali Class', 'Silicos-IT class']))
        self.class_button.setVisible(False)

        self.start_window = start_window
        self.logP_selection_window = logP_selection_window
        self.cols_to_use = cols_to_use
        self.threshold_cols = threshold_cols
        self.saving_format = saving_format
        self.pharmacokinetics_selection_window = pharmacokinetics_selection_window

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

    def show_solubility_specifications(self):
        self.mg_ml_button.setVisible(True)
        self.mol_l_button.setVisible(True)
        self.class_button.setVisible(True)

    def hide_solubility_specifications(self):
        if not self.ESOL_check.isChecked() and not self.Ali_check.isChecked() and not self.SILICOSIT_check.isChecked():
            self.mg_ml_button.setChecked(False)
            self.mg_ml_button.setVisible(False)
            self.mol_l_button.setChecked(False)
            self.mol_l_button.setVisible(False)
            self.class_button.setChecked(False)
            self.class_button.setVisible(False)

    def check_specification_button(self, button, cols):
        if button.isChecked():
            if self.ESOL_check.isChecked():
                if cols[0] not in self.cols_to_use:
                    self.cols_to_use.append(cols[0])
            else:
                if cols[0] in self.cols_to_use:
                    self.cols_to_use.remove(cols[0])

            if self.Ali_check.isChecked():
                if cols[1] not in self.cols_to_use:
                    self.cols_to_use.append(cols[1])
            else:
                if cols[1] in self.cols_to_use:
                    self.cols_to_use.remove(cols[1])

            if self.SILICOSIT_check.isChecked():
                if cols[2] not in self.cols_to_use:
                    self.cols_to_use.append(cols[2])
            else:
                if cols[2] in self.cols_to_use:
                    self.cols_to_use.remove(cols[2])
        else:
            for col in cols:
                if col in self.cols_to_use:
                    self.cols_to_use.remove(col)

    def get_threshold_values(self):
        self.threshold_cols['ESOL Log S'] = (
            float(self.ESOL_lower_threshold_edit.toPlainText()), float(self.ESOL_upper_threshold_edit.toPlainText()))
        self.threshold_cols['Ali Log S'] = (
            float(self.Ali_lower_threshold_edit.toPlainText()), float(self.Ali_upper_threshold_edit.toPlainText()))
        self.threshold_cols['Silicos-IT LogSw'] = (
            float(self.SILICOSIT_lower_threshold_edit.toPlainText()),
            float(self.SILICOSIT_upper_threshold_edit.toPlainText()))

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.logP_selection_window.show()

    def next_step(self):
        self.next_clicked = True
        self.get_threshold_values()

        self.pharmacokinetics_selection_window = pharmacokinetics_selection.PharmacokineticsSelectionWindow(
            self.start_window, self, self.cols_to_use, self.threshold_cols, self.saving_format
        )
        self.close()
        self.pharmacokinetics_selection_window.show()
