from base_window import BaseWindow
import conversion_format_selection
from styles import *

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QFileDialog


class SavingProductsWindow(BaseWindow):
    def __init__(self, start_window, swissADME_window, saving_format):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.download_button = QtWidgets.QPushButton(self)
        self.download_button.clicked.connect(self.download_results)
        self.download_button.setText('Download products')
        self.download_button.setGeometry(170, 329, 243, 40)
        self.download_button.setStyleSheet(upload_button_stylesheet)

        self.next_button.setEnabled(True)
        self.next_button.setStyleSheet(back_next_button_stylesheet)

        self.start_window = start_window
        self.swissADME_window = swissADME_window
        self.saving_format = saving_format

        self.output_data = QtWidgets.QTextEdit(self)
        self.output_data.setGeometry(150, 80, 280, 250)
        if self.saving_format == 'csv':
            f = open('output.csv', 'r')
        else:
            f = open('output.txt', 'r')
        self.output_data.setText(f.read())

        if self.output_data.toPlainText() == '':
            self.output_data.setText('No products generated.')
            self.next_button.setEnabled(False)
            self.next_button.setStyleSheet(default_stylesheet)

    def download_results(self):
        text = self.output_data.toPlainText()
        fname = QFileDialog.getSaveFileName(caption='Save file', directory='.')[0]
        try:
            f = open(fname, 'w')
            f.write(text)
        except Exception:
            pass

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.swissADME_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        self.conversion_format_selection_window = conversion_format_selection.ConversionFormatSelectionWindow(
            self.start_window, self)
        self.conversion_format_selection_window.show()
