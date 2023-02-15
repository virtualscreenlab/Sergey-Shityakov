import click_reaction
import physical_properties_selection

from base_window import BaseWindow
from local_dictionaries.reagent_1 import *
from local_dictionaries.reagent_2 import *
from styles import *

from PyQt5 import QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPalette, QBrush


class ProcessThread(QThread):
    start_signal = pyqtSignal()
    print_signal = pyqtSignal(str)
    finish_signal = pyqtSignal()

    def __init__(self, window, parent=None):
        super(ProcessThread, self).__init__(parent)
        self.window = window

    def run(self):
        self.window.clear_log()
        self.window.get_products_clicked = True
        self.start_signal.emit()
        click_reaction.reaction(self.window.selected_isomers, self.window, self)
        self.finish_signal.emit()


class CalculationsWindow(BaseWindow):
    def __init__(self, start_window, saving_options_window, selected_isomers, reaction_type,
                 saving_format, physical_properties_selection_window=None):
        super().__init__()

        self.setFixedSize(1000, 700)

        oImage = QImage("chem_back.jpg")
        sImage = oImage.scaled(QSize(1000, 700))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.start_window = start_window
        self.saving_options_window = saving_options_window
        self.selected_isomers = selected_isomers
        self.reaction_type = reaction_type
        self.saving_format = saving_format
        self.physical_properties_selection_window = physical_properties_selection_window
        self.reaction_products = None

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(170, 100, 700, 35)
        self.progress_bar.setStyleSheet(progress_bar_stylesheet)

        self.log = QtWidgets.QTextEdit(self)
        self.log.setGeometry(170, 180, 700, 290)
        self.log.setReadOnly(True)
        self.cursor = QTextCursor(self.log.document())
        self.log.setTextCursor(self.cursor)

        self.calculate_button = QtWidgets.QPushButton(self)
        self.calculate_button.setText('Get reaction products')
        self.calculate_button.clicked.connect(self.get_products)
        self.calculate_button.setGeometry(190, 468, 660, 50)
        self.calculate_button.setStyleSheet(upload_button_stylesheet)

        self.get_products_clicked = False
        self.back_clicked = False
        self.next_clicked = False

        self.back_button.setStyleSheet(back_next_process_button_stylesheet)

        self.next_button.setGeometry(880, 650, 95, 40)

        self.reagent_1 = ''.join(open('good_reagent_1.txt')).split()
        self.reagent_2 = ''.join(open('good_reagent_2.txt')).split()

        self.process_thread = ProcessThread(self)
        self.process_thread.start_signal.connect(self.start_signal_process)
        self.process_thread.finish_signal.connect(self.finish_signal_process)
        self.process_thread.print_signal.connect(self.print_signal_process)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeout_func)

        products_length = len(self.reagent_1) * len(self.reagent_2)
        if products_length < 1000:
            self.timeout = 100
        elif 1000 <= products_length < 10000:
            self.timeout = 200
        elif 10000 <= products_length < 20000:
            self.timeout = 300
        elif 20000 <= products_length < 1000000:
            self.timeout = 500
        else:
            self.timeout = 1000

        self.clear_log()
        self.log.setText(
            f'All {REAGENT_1[self.reaction_type]} and {REAGENT_2[self.reaction_type]} molecules were processed')

    def get_products(self):
        self.calculate_button.setEnabled(False)
        self.progress_bar.setValue(0)
        self.process_thread.start()

    def start_signal_process(self):
        self.timer.start(self.timeout)

    def print_signal_process(self, msg):
        self.show_log(msg)

    def finish_signal_process(self):
        self.progress_bar.setValue(100)
        click_reaction.form_stats_log(self, self.hours, self.minutes, self.seconds, self.reagent_1, self.reagent_2,
                                      self.total_products,  self.errors)
        self.timer.stop()
        self.calculate_button.setEnabled(True)

    def timeout_func(self):
        self.progress_bar.setValue(round((self.all_candidates) / (len(self.reagent_1) * len(self.reagent_2)) * 100))

    def clear_log(self):
        with open('products_log.txt', 'w') as f:
            f.write('')
            f.close()

    def show_log(self, msg):
        with open('products_log.txt', 'a') as f:
            f.write(msg)
            f.close()
        with open('products_log.txt', 'r') as f:
            data = f.read()
            self.log.setText(data)
            f.close()

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.saving_options_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()

        self.physical_properties_selection_window = physical_properties_selection.PhysicalPropertiesSelectionWindow(
            self.start_window, self, self.saving_format)
        self.physical_properties_selection_window.show()
