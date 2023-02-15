import conversion
from base_window import BaseWindow
from styles import *

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QLabel, QRadioButton, QComboBox, QApplication

FORMATS_DICT = {
    'abbrev - ChemAxon SMILES Abbreviated Groups': 'abbrevgroup',
    'accord - Accord file format': 'accord',
    'cdx - CDX File Format': 'cdx',
    'cdxml - CDXML File Format': 'cdxml',
    'cml - Chemical Markup Language': 'cml',
    'csmdl - ChemAxon Compressed Mol, Rxn or SDfile': 'csmdl',
    'csmol - ChemAxon Compressed Mol': 'csmol',
    'csrdf - ChemAxon Compressed RDfile': 'csrdf',
    'csrxn - ChemAxon Compressed Rxn': 'csrxn',
    'cssdf - ChemAxon Compressed SDfile': 'cssdf',
    'cube - Gaussian Cube': 'cube',
    'cxsmarts - ChemAxon Extended SMARTS': 'cxsmarts',
    'cxsmiles - ChemAxon Extended SMILES': 'cxsmiles',
    'd2s - Text/Office Document': 'd2s',
    'dna - DNA Sequence': 'dna',
    'fasta - FASTA (Automatic recognition)': 'fasta',
    'fasta:dna - FASTA (DNA sequence)': 'fasta:dna',
    'fasta:peptide - FASTA (peptide sequence)': 'fasta:peptide',
    'fasta:rna - FASTA (RNA sequence)': 'fasta:rna',
    'gout - Gaussian Output Format': 'gout',
    'inchi - InChI': 'inchi',
    'mol - MDL Molfile': 'mol',
    'mol2 - Tripos Mol2': 'mol2',
    'mol:V3 - MDL Extended Molfile (v3000)': 'mol:V3',
    'mrv - ChemAxon Marvin Documents / MRV': 'mrv',
    'name - Name': 'name',
    'pdb - Protein Data Bank': 'pdb',
    'peptide - Peptide Sequence': 'peptide',
    'rdf - MDL RDfile': 'rdf',
    'rgf - MDL Molfile': 'rgf',
    'rna - RNA Sequence': 'rna',
    'rxn - MDL Rxnfile': 'rxn',
    'rxn:V3 - MDL Extended Rxnfile': 'rxn:V3',
    'sdf - MDL SDfile': 'sdf',
    'sdf:V3 - MDL SDfile': 'sdf:V3',
    'skc - SKC File Format': 'skc',
    'smarts - SMARTS': 'smarts',
    'sybyl - Tripos SYBYL molfile': 'sybyl',
    'xyz - XYZ': 'xyz'

}


class ConversionFormatSelectionWindow(BaseWindow):
    def __init__(self, start_window, products_saving_window):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.info_label = QLabel(self)
        self.info_label.setGeometry(135, 220, 260, 40)
        self.info_label.setText('Convert products to other formats:')
        self.info_label.setFont(QFont('OldEnglish', 9))
        self.info_label.setStyleSheet(headline_stylesheet)

        self.format_combobox = QComboBox(self)
        self.format_combobox.addItem('None')
        self.format_combobox.addItems(list(FORMATS_DICT.keys()))
        self.format_combobox.setGeometry(135, 255, 372, 27)
        self.format_combobox.adjustSize()
        self.format_combobox.setFont(QFont('OldEnglish', 8))
        self.format_combobox.activated[str].connect(self.format_combobox_changed)

        self.c2d_check = QRadioButton(self)
        self.c2d_check.setGeometry(135, 280, 253, 40)
        self.c2d_check.setText('Show 2D coordinates')
        self.c2d_check.setFont(QFont('OldEnglish', 9))
        self.c2d_check.setStyleSheet(radio_button_stylesheet)
        self.c2d_check.toggled.connect(self.coordinates_check)

        self.c3d_check = QRadioButton(self)
        self.c3d_check.setGeometry(135, 315, 253, 40)
        self.c3d_check.setText('Show 3D coordinates')
        self.c3d_check.setFont(QFont('OldEnglish', 9))
        self.c3d_check.setStyleSheet(radio_button_stylesheet)
        self.c3d_check.toggled.connect(self.coordinates_check)

        self.conversion_format = None
        self.coordinates = {'2d': False, '3d': False}

        self.start_window = start_window
        self.products_saving_window = products_saving_window

        self.next_button.setEnabled(True)
        self.next_button.setText('Restart')
        self.next_button.setStyleSheet(back_next_button_stylesheet)

    def format_combobox_changed(self, text):
        self.conversion_format = FORMATS_DICT[text]
        if self.conversion_format != 'None':
            self.next_button.setText('Next')

    def coordinates_check(self):
        if self.c2d_check.isChecked():
            self.coordinates['2d'] = True
            self.coordinates['3d'] = False
        if self.c3d_check.isChecked():
            self.coordinates['3d'] = True
            self.coordinates['2d'] = False

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.products_saving_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        if self.conversion_format is None or self.conversion_format == 'None':
            self.start_window.show()
        else:
            self.conversion_window = conversion.ConversionWindow(self.start_window, self, self.conversion_format,
                                                                 self.coordinates)
            self.conversion_window.show()
