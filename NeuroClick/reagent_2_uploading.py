import reagent_2_processing
from base_window import BaseWindow
from local_dictionaries.reagent_2 import REAGENT_2
from styles import *

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QFileDialog


class Reagent2Window(BaseWindow):
    def __init__(self, start_window, reagent_1_process_window, reaction_type):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.start_window = start_window
        self.reagent_1_process_window = reagent_1_process_window
        self.reaction_type = reaction_type

        self.input_reagent_2 = QtWidgets.QTextEdit(self)
        self.input_reagent_2.setGeometry(150, 80, 280, 250)
        self.input_reagent_2.textChanged.connect(self.activate_next)

        self.load_reagent_2_button = QtWidgets.QPushButton(self)
        self.load_reagent_2_button.clicked.connect(self.read_input_from_file)
        self.load_reagent_2_button.setText('Upload ' + REAGENT_2[self.reaction_type] + 's')
        self.load_reagent_2_button.setGeometry(170, 329, 243, 40)
        self.load_reagent_2_button.setStyleSheet(upload_button_stylesheet)

    def activate_next(self):
        text = self.input_reagent_2.toPlainText()
        if text != '':
            self.next_button.setEnabled(True)
            self.next_button.setStyleSheet(back_next_button_stylesheet)
        else:
            self.next_button.setEnabled(False)
            self.next_button.setStyleSheet(default_stylesheet)

    def read_input_from_file(self):
        fname = QFileDialog.getOpenFileName(caption='Open file', directory='.')[0]
        try:
            f = open(fname, 'r')
            with f:
                data = f.read()
                self.input_reagent_2.setText(data)
        except Exception:
            pass

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.reagent_1_process_window.show()

    def next_step(self):
        self.next_clicked = True
        reagent_2 = self.input_reagent_2.toPlainText().split('\n')
        self.close()
        self.process_window = reagent_2_processing.ProcessWindow(self.start_window, self, reagent_2, self.reaction_type)
        self.process_window.show()
