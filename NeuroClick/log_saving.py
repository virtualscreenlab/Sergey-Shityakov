import saving_products
from base_window import BaseWindow
from my_logging import merge_logs
from styles import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class LogSavingWindow(BaseWindow):
    def __init__(self, start_window, calculations_window, saving_format, reaction_products, results_window=None):
        super().__init__()

        self.download_button = QtWidgets.QPushButton(self)
        self.download_button.clicked.connect(self.download_results)
        self.download_button.setText('Save program log file')
        self.download_button.setGeometry(170, 330, 243, 40)
        self.download_button.setStyleSheet(upload_button_stylesheet)

        self.next_button.setEnabled(True)
        self.next_button.setStyleSheet(back_next_button_stylesheet)

        self.start_window = start_window
        self.calculations_window = calculations_window
        self.calculations_window.results_window = self
        self.saving_format = saving_format
        self.reaction_products = reaction_products
        self.results_window = results_window

        self.output_data = QtWidgets.QTextEdit(self)
        self.output_data.setGeometry(150, 80, 280, 250)
        merge_logs()
        f = open('log.txt', 'r')
        self.output_data.setText(f.read())

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
        self.calculations_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        if self.results_window is None:
            self.results_window = results.ResultsWindow(self.start_window, self, self.saving_format,
                                                        self.reaction_products)
        self.results_window.show()
