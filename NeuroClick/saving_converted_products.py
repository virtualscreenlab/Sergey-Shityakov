from base_window import BaseWindow
import conversion_format_selection
from styles import *

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QFileDialog


class SavingConvertedProductsWindow(BaseWindow):
    def __init__(self, start_window, conversion_window, conversion_format):
        super().__init__()

        oImage = QImage('chem_back_2.jpg')
        sImage = oImage.scaled(QSize(600, 898))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.download_button = QtWidgets.QPushButton(self)
        self.download_button.setText('Save converted file')
        self.download_button.setGeometry(170, 329, 243, 40)
        self.download_button.setStyleSheet(upload_button_stylesheet)
        self.download_button.clicked.connect(self.download_results)

        #self.next_button.setEnabled(False)
        #self.next_button.setStyleSheet(back_next_button_stylesheet)

        self.start_window = start_window
        self.conversion_window = conversion_window
        self.conversion_format = conversion_format

        self.output_data = QtWidgets.QTextEdit(self)
        self.output_data.setGeometry(150, 80, 280, 250)
        converted_file = 'conversions/output.' + self.conversion_format
        with open(converted_file, 'r') as f:
            self.output_data.setText(f.read())

        if self.output_data.toPlainText() == '':
            self.output_data.setText('Error while conversion')
            self.next_button.setEnabled(False)
            self.next_button.setStyleSheet(default_stylesheet)

    def download_results(self):
        text = self.output_data.toPlainText()
        fname = QFileDialog.getSaveFileName(caption='Save file', directory='.')[0]
        try:
            with open(fname, 'w') as f:
                f.write(text)
        except Exception:
            pass

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.conversion_window.show()

    def next_step(self):
        pass
        # self.next_clicked = True
        # self.close()
        # self.conversion_format_selection_window = conversion_format_selection.ConversionFormatSelectionWindow(
        #     self.start_window, self)
        # self.conversion_format_selection_window.show()
