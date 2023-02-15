import logP_selection
from base_window import BaseWindow
from styles import *

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QLabel, QTextEdit, QCheckBox


class PhysicalPropertiesSelectionWindow(BaseWindow):
    def __init__(self, start_window, calculations_window, saving_format, logP_selection_window=None):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.info_label = QLabel(self)
        self.info_label.setGeometry(145, 160, 253, 40)
        self.info_label.setText('Select physical properties: ')
        self.info_label.setFont(QFont('OldEnglish', 9))
        self.info_label.setStyleSheet(headline_stylesheet)

        self.molecular_weight_check = QCheckBox(self)
        self.molecular_weight_check.setGeometry(145, 190, 253, 40)
        self.molecular_weight_check.setText('Molecular weight (g/mol)')
        self.molecular_weight_check.setFont(QFont('OldEnglish', 9))
        self.molecular_weight_check.setStyleSheet(checkbox_stylesheet)
        self.molecular_weight_check.toggled.connect(
            lambda: self.check(self.molecular_weight_check, self.molecular_weight_lower_threshold_label,
                               self.molecular_weight_lower_threshold_edit, self.molecular_weight_upper_threshold_label,
                               self.molecular_weight_upper_threshold_edit, 'MW'))

        self.heavy_atoms_check = QCheckBox(self)
        self.heavy_atoms_check.setGeometry(145, 225, 253, 40)
        self.heavy_atoms_check.setText('Heavy atoms')
        self.heavy_atoms_check.setFont(QFont('OldEnglish', 9))
        self.heavy_atoms_check.setStyleSheet(checkbox_stylesheet)
        self.heavy_atoms_check.toggled.connect(
            lambda: self.check(self.heavy_atoms_check, self.heavy_atoms_lower_threshold_label,
                               self.heavy_atoms_lower_threshold_edit, self.heavy_atoms_upper_threshold_label,
                               self.heavy_atoms_upper_threshold_edit, '#Heavy atoms'))

        self.aromatic_heavy_atoms_check = QCheckBox(self)
        self.aromatic_heavy_atoms_check.setGeometry(145, 260, 253, 40)
        self.aromatic_heavy_atoms_check.setText('Aromatic heavy atoms')
        self.aromatic_heavy_atoms_check.setFont(QFont('OldEnglish', 9))
        self.aromatic_heavy_atoms_check.setStyleSheet(checkbox_stylesheet)
        self.aromatic_heavy_atoms_check.toggled.connect(
            lambda: self.check(self.aromatic_heavy_atoms_check, self.aromatic_heavy_atoms_lower_threshold_label,
                               self.aromatic_heavy_atoms_lower_threshold_edit,
                               self.aromatic_heavy_atoms_upper_threshold_label,
                               self.aromatic_heavy_atoms_upper_threshold_edit, '#Aromatic heavy atoms'))

        self.fraction_csp3_check = QCheckBox(self)
        self.fraction_csp3_check.setGeometry(145, 295, 253, 40)
        self.fraction_csp3_check.setText('Fraction Csp3')
        self.fraction_csp3_check.setFont(QFont('OldEnglish', 9))
        self.fraction_csp3_check.setStyleSheet(checkbox_stylesheet)
        self.fraction_csp3_check.toggled.connect(
            lambda: self.check(self.fraction_csp3_check, self.fraction_csp3_lower_threshold_label,
                               self.fraction_csp3_lower_threshold_edit,
                               self.fraction_csp3_upper_threshold_label, self.fraction_csp3_upper_threshold_edit,
                               'Fraction Csp3'))

        self.rotatable_bonds_check = QCheckBox(self)
        self.rotatable_bonds_check.setGeometry(145, 330, 253, 40)
        self.rotatable_bonds_check.setText('Rotatable bonds')
        self.rotatable_bonds_check.setFont(QFont('OldEnglish', 9))
        self.rotatable_bonds_check.setStyleSheet(checkbox_stylesheet)
        self.rotatable_bonds_check.toggled.connect(
            lambda: self.check(self.rotatable_bonds_check, self.rotatable_bonds_lower_threshold_label,
                               self.rotatable_bonds_lower_threshold_edit,
                               self.rotatable_bonds_upper_threshold_label, self.rotatable_bonds_upper_threshold_edit,
                               '#Rotatable bonds'))

        self.h_acceptors_check = QCheckBox(self)
        self.h_acceptors_check.setGeometry(145, 365, 253, 40)
        self.h_acceptors_check.setText('H-bond acceptors')
        self.h_acceptors_check.setFont(QFont('OldEnglish', 9))
        self.h_acceptors_check.setStyleSheet(checkbox_stylesheet)
        self.h_acceptors_check.toggled.connect(
            lambda: self.check(self.h_acceptors_check, self.h_acceptors_lower_threshold_label,
                               self.h_acceptors_lower_threshold_edit, self.h_acceptors_upper_threshold_label,
                               self.h_acceptors_upper_threshold_edit, '#H-bond acceptors'))

        self.h_donors_check = QCheckBox(self)
        self.h_donors_check.setGeometry(145, 400, 253, 40)
        self.h_donors_check.setText('H-bond donors')
        self.h_donors_check.setFont(QFont('OldEnglish', 9))
        self.h_donors_check.setStyleSheet(checkbox_stylesheet)
        self.h_donors_check.toggled.connect(
            lambda: self.check(self.h_donors_check, self.h_donors_lower_threshold_label,
                               self.h_donors_lower_threshold_edit, self.h_donors_upper_threshold_label,
                               self.h_donors_upper_threshold_edit, '#H-bond donors'))

        self.molar_refractivity_check = QCheckBox(self)
        self.molar_refractivity_check.setGeometry(145, 435, 253, 40)
        self.molar_refractivity_check.setText('Molar refractivity')
        self.molar_refractivity_check.setFont(QFont('OldEnglish', 9))
        self.molar_refractivity_check.setStyleSheet(checkbox_stylesheet)
        self.molar_refractivity_check.toggled.connect(
            lambda: self.check(self.molar_refractivity_check, self.molar_refractivity_lower_threshold_label,
                               self.molar_refractivity_lower_threshold_edit,
                               self.molar_refractivity_upper_threshold_label,
                               self.molar_refractivity_upper_threshold_edit, 'MR'))

        self.tpsa_check = QCheckBox(self)
        self.tpsa_check.setGeometry(145, 470, 253, 40)
        self.tpsa_check.setText('TPSA')
        self.tpsa_check.setFont(QFont('OldEnglish', 9))
        self.tpsa_check.setStyleSheet(checkbox_stylesheet)
        self.tpsa_check.toggled.connect(
            lambda: self.check(self.tpsa_check, self.tpsa_lower_threshold_label,
                               self.tpsa_lower_threshold_edit, self.tpsa_upper_threshold_label,
                               self.tpsa_upper_threshold_edit, 'TPSA'))

        self.molecular_weight_lower_threshold_label = QLabel(self)
        self.molecular_weight_lower_threshold_label.setGeometry(341, 195, 70, 30)
        self.molecular_weight_lower_threshold_label.setText('from')
        self.molecular_weight_lower_threshold_label.setVisible(False)

        self.heavy_atoms_lower_threshold_label = QLabel(self)
        self.heavy_atoms_lower_threshold_label.setGeometry(341, 230, 70, 30)
        self.heavy_atoms_lower_threshold_label.setText('from')
        self.heavy_atoms_lower_threshold_label.setVisible(False)

        self.aromatic_heavy_atoms_lower_threshold_label = QLabel(self)
        self.aromatic_heavy_atoms_lower_threshold_label.setGeometry(341, 265, 70, 30)
        self.aromatic_heavy_atoms_lower_threshold_label.setText('from')
        self.aromatic_heavy_atoms_lower_threshold_label.setVisible(False)

        self.fraction_csp3_lower_threshold_label = QLabel(self)
        self.fraction_csp3_lower_threshold_label.setGeometry(341, 300, 70, 30)
        self.fraction_csp3_lower_threshold_label.setText('from')
        self.fraction_csp3_lower_threshold_label.setVisible(False)

        self.rotatable_bonds_lower_threshold_label = QLabel(self)
        self.rotatable_bonds_lower_threshold_label.setGeometry(341, 335, 70, 30)
        self.rotatable_bonds_lower_threshold_label.setText('from')
        self.rotatable_bonds_lower_threshold_label.setVisible(False)

        self.h_acceptors_lower_threshold_label = QLabel(self)
        self.h_acceptors_lower_threshold_label.setGeometry(341, 370, 70, 30)
        self.h_acceptors_lower_threshold_label.setText('from')
        self.h_acceptors_lower_threshold_label.setVisible(False)

        self.h_donors_lower_threshold_label = QLabel(self)
        self.h_donors_lower_threshold_label.setGeometry(341, 405, 70, 30)
        self.h_donors_lower_threshold_label.setText('from')
        self.h_donors_lower_threshold_label.setVisible(False)

        self.molar_refractivity_lower_threshold_label = QLabel(self)
        self.molar_refractivity_lower_threshold_label.setGeometry(341, 440, 70, 30)
        self.molar_refractivity_lower_threshold_label.setText('from')
        self.molar_refractivity_lower_threshold_label.setVisible(False)

        self.tpsa_lower_threshold_label = QLabel(self)
        self.tpsa_lower_threshold_label.setGeometry(341, 475, 70, 30)
        self.tpsa_lower_threshold_label.setText('from')
        self.tpsa_lower_threshold_label.setVisible(False)

        self.molecular_weight_lower_threshold_edit = QTextEdit(self)
        self.molecular_weight_lower_threshold_edit.setGeometry(372, 195, 40, 28)
        self.molecular_weight_lower_threshold_edit.setText('0')
        self.molecular_weight_lower_threshold_edit.setVisible(False)

        self.heavy_atoms_lower_threshold_edit = QTextEdit(self)
        self.heavy_atoms_lower_threshold_edit.setGeometry(372, 230, 40, 28)
        self.heavy_atoms_lower_threshold_edit.setText('0')
        self.heavy_atoms_lower_threshold_edit.setVisible(False)

        self.aromatic_heavy_atoms_lower_threshold_edit = QTextEdit(self)
        self.aromatic_heavy_atoms_lower_threshold_edit.setGeometry(372, 265, 40, 28)
        self.aromatic_heavy_atoms_lower_threshold_edit.setText('0')
        self.aromatic_heavy_atoms_lower_threshold_edit.setVisible(False)

        self.fraction_csp3_lower_threshold_edit = QTextEdit(self)
        self.fraction_csp3_lower_threshold_edit.setGeometry(372, 300, 40, 28)
        self.fraction_csp3_lower_threshold_edit.setText('0')
        self.fraction_csp3_lower_threshold_edit.setVisible(False)

        self.rotatable_bonds_lower_threshold_edit = QTextEdit(self)
        self.rotatable_bonds_lower_threshold_edit.setGeometry(372, 335, 40, 28)
        self.rotatable_bonds_lower_threshold_edit.setText('0')
        self.rotatable_bonds_lower_threshold_edit.setVisible(False)

        self.h_acceptors_lower_threshold_edit = QTextEdit(self)
        self.h_acceptors_lower_threshold_edit.setGeometry(372, 370, 40, 28)
        self.h_acceptors_lower_threshold_edit.setText('0')
        self.h_acceptors_lower_threshold_edit.setVisible(False)

        self.h_donors_lower_threshold_edit = QTextEdit(self)
        self.h_donors_lower_threshold_edit.setGeometry(372, 405, 40, 28)
        self.h_donors_lower_threshold_edit.setText('0')
        self.h_donors_lower_threshold_edit.setVisible(False)

        self.molar_refractivity_lower_threshold_edit = QTextEdit(self)
        self.molar_refractivity_lower_threshold_edit.setGeometry(372, 440, 40, 28)
        self.molar_refractivity_lower_threshold_edit.setText('0')
        self.molar_refractivity_lower_threshold_edit.setVisible(False)

        self.tpsa_lower_threshold_edit = QTextEdit(self)
        self.tpsa_lower_threshold_edit.setGeometry(372, 475, 40, 28)
        self.tpsa_lower_threshold_edit.setText('0')
        self.tpsa_lower_threshold_edit.setVisible(False)

        self.molecular_weight_upper_threshold_label = QLabel(self)
        self.molecular_weight_upper_threshold_label.setGeometry(417, 195, 70, 30)
        self.molecular_weight_upper_threshold_label.setText('to')
        self.molecular_weight_upper_threshold_label.setVisible(False)

        self.heavy_atoms_upper_threshold_label = QLabel(self)
        self.heavy_atoms_upper_threshold_label.setGeometry(417, 230, 70, 30)
        self.heavy_atoms_upper_threshold_label.setText('to')
        self.heavy_atoms_upper_threshold_label.setVisible(False)

        self.aromatic_heavy_atoms_upper_threshold_label = QLabel(self)
        self.aromatic_heavy_atoms_upper_threshold_label.setGeometry(417, 265, 70, 30)
        self.aromatic_heavy_atoms_upper_threshold_label.setText('to')
        self.aromatic_heavy_atoms_upper_threshold_label.setVisible(False)

        self.fraction_csp3_upper_threshold_label = QLabel(self)
        self.fraction_csp3_upper_threshold_label.setGeometry(417, 300, 70, 30)
        self.fraction_csp3_upper_threshold_label.setText('to')
        self.fraction_csp3_upper_threshold_label.setVisible(False)

        self.rotatable_bonds_upper_threshold_label = QLabel(self)
        self.rotatable_bonds_upper_threshold_label.setGeometry(417, 335, 70, 30)
        self.rotatable_bonds_upper_threshold_label.setText('to')
        self.rotatable_bonds_upper_threshold_label.setVisible(False)

        self.h_acceptors_upper_threshold_label = QLabel(self)
        self.h_acceptors_upper_threshold_label.setGeometry(417, 370, 70, 30)
        self.h_acceptors_upper_threshold_label.setText('to')
        self.h_acceptors_upper_threshold_label.setVisible(False)

        self.h_donors_upper_threshold_label = QLabel(self)
        self.h_donors_upper_threshold_label.setGeometry(417, 405, 40, 28)
        self.h_donors_upper_threshold_label.setText('to')
        self.h_donors_upper_threshold_label.setVisible(False)

        self.molar_refractivity_upper_threshold_label = QLabel(self)
        self.molar_refractivity_upper_threshold_label.setGeometry(417, 440, 40, 28)
        self.molar_refractivity_upper_threshold_label.setText('to')
        self.molar_refractivity_upper_threshold_label.setVisible(False)

        self.tpsa_upper_threshold_label = QLabel(self)
        self.tpsa_upper_threshold_label.setGeometry(417, 475, 40, 28)
        self.tpsa_upper_threshold_label.setText('to')
        self.tpsa_upper_threshold_label.setVisible(False)

        self.molecular_weight_upper_threshold_edit = QTextEdit(self)
        self.molecular_weight_upper_threshold_edit.setGeometry(436, 195, 40, 28)
        self.molecular_weight_upper_threshold_edit.setText('1000')
        self.molecular_weight_upper_threshold_edit.setVisible(False)

        self.heavy_atoms_upper_threshold_edit = QTextEdit(self)
        self.heavy_atoms_upper_threshold_edit.setGeometry(436, 230, 40, 28)
        self.heavy_atoms_upper_threshold_edit.setText('200')
        self.heavy_atoms_upper_threshold_edit.setVisible(False)

        self.aromatic_heavy_atoms_upper_threshold_edit = QTextEdit(self)
        self.aromatic_heavy_atoms_upper_threshold_edit.setGeometry(436, 265, 40, 28)
        self.aromatic_heavy_atoms_upper_threshold_edit.setText('200')
        self.aromatic_heavy_atoms_upper_threshold_edit.setVisible(False)

        self.fraction_csp3_upper_threshold_edit = QTextEdit(self)
        self.fraction_csp3_upper_threshold_edit.setGeometry(436, 300, 40, 28)
        self.fraction_csp3_upper_threshold_edit.setText('1')
        self.fraction_csp3_upper_threshold_edit.setVisible(False)

        self.rotatable_bonds_upper_threshold_edit = QTextEdit(self)
        self.rotatable_bonds_upper_threshold_edit.setGeometry(436, 335, 40, 28)
        self.rotatable_bonds_upper_threshold_edit.setText('100')
        self.rotatable_bonds_upper_threshold_edit.setVisible(False)

        self.h_acceptors_upper_threshold_edit = QTextEdit(self)
        self.h_acceptors_upper_threshold_edit.setGeometry(436, 370, 40, 28)
        self.h_acceptors_upper_threshold_edit.setText('100')
        self.h_acceptors_upper_threshold_edit.setVisible(False)

        self.h_donors_upper_threshold_edit = QTextEdit(self)
        self.h_donors_upper_threshold_edit.setGeometry(436, 405, 40, 28)
        self.h_donors_upper_threshold_edit.setText('100')
        self.h_donors_upper_threshold_edit.setVisible(False)

        self.molar_refractivity_upper_threshold_edit = QTextEdit(self)
        self.molar_refractivity_upper_threshold_edit.setGeometry(436, 440, 40, 28)
        self.molar_refractivity_upper_threshold_edit.setText('200')
        self.molar_refractivity_upper_threshold_edit.setVisible(False)

        self.tpsa_upper_threshold_edit = QTextEdit(self)
        self.tpsa_upper_threshold_edit.setGeometry(436, 475, 40, 28)
        self.tpsa_upper_threshold_edit.setText('200')
        self.tpsa_upper_threshold_edit.setVisible(False)

        self.start_window = start_window
        self.calculations_window = calculations_window
        self.saving_format = saving_format
        self.logP_selection_window = logP_selection_window
        self.cols_to_use = ['Molecule', 'Canonical SMILES']
        self.threshold_cols = {}

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
        self.threshold_cols['MW'] = (
            float(self.molecular_weight_lower_threshold_edit.toPlainText()),
            float(self.molecular_weight_upper_threshold_edit.toPlainText()))
        self.threshold_cols['#Heavy atoms'] = (
            int(self.heavy_atoms_lower_threshold_edit.toPlainText()),
            int(self.heavy_atoms_upper_threshold_edit.toPlainText()))
        self.threshold_cols['#Aromatic heavy atoms'] = (
            int(self.aromatic_heavy_atoms_lower_threshold_edit.toPlainText()),
            int(self.aromatic_heavy_atoms_upper_threshold_edit.toPlainText()))
        self.threshold_cols['Fraction Csp3'] = (
            float(self.fraction_csp3_lower_threshold_edit.toPlainText()),
            float(self.fraction_csp3_upper_threshold_edit.toPlainText()))
        self.threshold_cols['#Rotatable bonds'] = (
            int(self.rotatable_bonds_lower_threshold_edit.toPlainText()),
            int(self.rotatable_bonds_upper_threshold_edit.toPlainText()))
        self.threshold_cols['#H-bond acceptors'] = (
            int(self.h_acceptors_lower_threshold_edit.toPlainText()),
            int(self.h_acceptors_upper_threshold_edit.toPlainText()))
        self.threshold_cols['#H-bond donors'] = (
            int(self.h_donors_lower_threshold_edit.toPlainText()),
            int(self.h_donors_upper_threshold_edit.toPlainText()))
        self.threshold_cols['MR'] = (
            float(self.molar_refractivity_lower_threshold_edit.toPlainText()),
            float(self.molar_refractivity_upper_threshold_edit.toPlainText()))
        self.threshold_cols['TPSA'] = (
            float(self.tpsa_lower_threshold_edit.toPlainText()),
            float(self.tpsa_upper_threshold_edit.toPlainText()))

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.calculations_window.show()

    def next_step(self):
        self.next_clicked = True
        self.get_threshold_values()
        self.logP_selection_window = logP_selection.LogPSelectionWindow(self.start_window, self, self.cols_to_use,
                                                                        self.threshold_cols, self.saving_format)
        self.close()
        self.logP_selection_window.show()
