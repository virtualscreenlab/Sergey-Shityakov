import isomers_selection
import saving_options

from base_window import BaseWindow
from local_dictionaries.reagent_1 import *
from local_dictionaries.reagent_2 import *
from styles import *
from time_functions import time_format

import time
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPalette, QBrush
from rdkit import Chem


class ProcessThread(QThread):
    start_signal = pyqtSignal()
    print_signal = pyqtSignal(str)
    finish_signal = pyqtSignal()

    def __init__(self, window, parent=None):
        super(ProcessThread, self).__init__(parent)
        self.window = window

    def run(self):
        self.window.clear_log()
        start_time = time.time()

        self.print_signal.emit(f'Checking {REAGENT_2[self.window.reaction_type]} molecules...\n\n')
        self.window.total_reagent_2 = len(self.window.reagent_2)
        self.print_signal.emit(f'Found {self.window.total_reagent_2} records.\n')

        self.window.damaged_smiles = 0
        self.window.good_reagent_2 = 0
        self.window.non_reagent_2 = 0
        self.window.mixed_reagents = 0
        self.window.multiple_molecules = 0
        self.window.too_many_groups = 0
        self.window.used_reagent_2 = []

        self.start_signal.emit()

        for i, reagent_2 in enumerate(self.window.reagent_2):
            try:
                reagent_2 = Chem.CanonSmiles(reagent_2)
            except Exception:
                pass
            if reagent_2 in self.window.used_reagent_2:
                continue
            if Chem.MolFromSmiles(reagent_2) is None:
                self.print_signal.emit(f'Warning: could not parse molecule {reagent_2}.\n')
                self.window.damaged_smiles += 1
                continue
            if '.' in reagent_2:
                self.print_signal.emit(f'Warning:{reagent_2} consists of multiple sites.\n')
                self.window.multiple_molecules += 1
                continue
            reagent_2_count = len(
                Chem.MolFromSmiles(reagent_2).GetSubstructMatches(REAGENT_2_PATTERN[self.window.reaction_type]))
            reagent_1_count = len(
                Chem.MolFromSmiles(reagent_2).GetSubstructMatches(REAGENT_1_PATTERN[self.window.reaction_type]))

            if reagent_2_count == 0 and self.window.reaction_type == 'Diels-Alder':
                reagent_2_count = len(
                    Chem.MolFromSmiles(reagent_2).GetSubstructMatches(
                        REAGENT_2_PATTERN[self.window.reaction_type + '2']))
            if reagent_2_count == 0:
                self.print_signal.emit(
                    f'Warning: molecule {reagent_2} contains no {REAGENT_2[self.window.reaction_type]} moiety.\n')
                self.window.non_reagent_2 += 1
                continue
            if (reagent_2_count) > 0 and (reagent_1_count > 0):
                self.print_signal.emit(
                    f'Warning: molecule {reagent_2} contains both {REAGENT_2[self.window.reaction_type]} and'
                    f' {REAGENT_1[self.window.reaction_type]} moiety.\n')
                self.window.mixed_reagents += 1
                continue
            if reagent_2_count > 3:
                self.print_signal.emit(f'Warning: {reagent_2} contains {reagent_2_count} reaction centers.'
                                       f'Its processing will slow down the program dramatically. '
                                       f'At most 3 reaction centers are allowed.\n')
                self.window.too_many_groups += 1
                continue
            self.window.good_reagent_2 += 1
            self.window.used_reagent_2.append(reagent_2)

            with open('good_reagent_2.txt', 'a') as f:
                f.write(f'{reagent_2}\n')
                f.close()
            self.window.log.moveCursor(QtGui.QTextCursor.End)
            self.msleep(self.window.timeout)
        end_time = time.time()
        self.window.hours, self.window.minutes, self.window.seconds = time_format(start_time, end_time)
        self.finish_signal.emit()


class ProcessWindow(BaseWindow):
    def __init__(self, start_window, reagent_2_window, reagent_2, reaction_type):
        super().__init__()

        self.setFixedSize(1000, 700)

        oImage = QImage("chem_back.jpg")
        sImage = oImage.scaled(QSize(1000, 700))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.start_window = start_window
        self.reagent_2_window = reagent_2_window
        self.reagent_2 = reagent_2
        self.reaction_type = reaction_type

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(170, 100, 700, 35)
        self.progress_bar.setStyleSheet(progress_bar_stylesheet)

        self.log = QtWidgets.QTextEdit(self)
        self.log.setGeometry(170, 180, 700, 290)
        self.log.setReadOnly(True)
        self.cursor = QTextCursor(self.log.document())
        self.log.setTextCursor(self.cursor)

        self.process_button = QtWidgets.QPushButton(self)
        self.process_button.setGeometry(190, 468, 660, 50)
        self.process_button.setText(f'Start {REAGENT_2[self.reaction_type]}s processing')
        self.process_button.setStyleSheet(upload_button_stylesheet)
        self.process_button.clicked.connect(self.start_processing)

        self.back_button.setStyleSheet(back_next_process_button_stylesheet)
        self.next_button.setGeometry(880, 650, 95, 40)

        self.process_thread = ProcessThread(self)
        self.process_thread.start_signal.connect(self.start_signal_process)
        self.process_thread.finish_signal.connect(self.finish_signal_process)
        self.process_thread.print_signal.connect(self.print_signal_process)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeout_func)

        reagent_2_length = len(self.reagent_2)
        if reagent_2_length < 1000:
            self.timeout = 100
        elif 1000 <= reagent_2_length < 10000:
            self.timeout = 200
        elif 10000 <= reagent_2_length < 20000:
            self.timeout = 300
        elif 20000 <= reagent_2_length < 1000000:
            self.timeout = 500
        else:
            self.timeout = 1000

        self.clear_log()
        self.clear_reagent_2()
        self.log.setText(f'Ready, {REAGENT_2[self.reaction_type]} molecules were successfully uploaded')

    def start_processing(self):
        self.process_button.setEnabled(False)
        self.progress_bar.setValue(0)
        self.process_thread.start()

    def start_signal_process(self):
        self.progress_value = 0
        self.progress_bar.setValue(0)
        self.timer.start(self.timeout)

    def print_signal_process(self, msg):
        self.show_log(msg)

    def finish_signal_process(self):
        self.timer.stop()
        self.process_button.setEnabled(True)
        self.progress_bar.setValue(100)
        self.form_stats_log(self.hours, self.minutes, self.seconds, self.total_reagent_2, self.good_reagent_2,
                            self.damaged_smiles, self.non_reagent_2, self.mixed_reagents, self.multiple_molecules,
                            self.too_many_groups)

    def timeout_func(self):
        self.progress_bar.setValue(round((self.progress_value + 1) / self.total_reagent_2 * 100))
        self.progress_value += 1

    def form_stats_log(self, hours, minutes, seconds, total_reagent_2, good_reagent_2, damaged_smiles,
                       non_reagent_2, mixed_reagents, multiple_molecules, too_many_groups):
        self.show_log('\n\n')
        self.show_log('====\n')
        self.show_log('Finished loading!\n')
        self.show_log(f'Time: {hours:02}:{minutes:02}:{seconds:02}.\n')
        self.show_log(f'Successfully loaded {good_reagent_2} {REAGENT_2[self.reaction_type]} '
                      f'({round(good_reagent_2 / total_reagent_2 * 100, 2)}%).\n')

        self.show_log('Following molecules were dropped out:\n')
        self.show_log(f'{damaged_smiles} records contain damaged smiles '
                      f'({round(damaged_smiles / total_reagent_2 * 100, 2)}%).\n')
        self.show_log(f'{non_reagent_2} molecules contain no {REAGENT_2[self.reaction_type]} moiety '
                      f'({round(non_reagent_2 / total_reagent_2 * 100, 2)}%).\n')

        self.show_log(
            f'{mixed_reagents} molecules contain both {REAGENT_2[self.reaction_type]} and '
            f'{REAGENT_1[self.reaction_type]} moiety '
            f'({round(mixed_reagents / total_reagent_2 * 100, 2)}%).\n')
        self.show_log(f'{multiple_molecules} consist of multiple sites '
                      f'({round(multiple_molecules / total_reagent_2 * 100, 2)}%).\n')
        self.show_log(
            f'{too_many_groups} {REAGENT_2[self.reaction_type]} contain too many {REAGENT_2[self.reaction_type]} moieties '
            f'({round(too_many_groups / total_reagent_2 * 100, 2)}%).\n')
        self.activate_next(process=True)

    def clear_log(self):
        with open('reagent_2_log.txt', 'w') as f:
            f.write('')
            f.close()

    def clear_reagent_2(self):
        with open('good_reagent_2.txt', 'w') as f:
            f.write('')
            f.close()

    def show_log(self, msg):
        with open('reagent_2_log.txt', 'a') as f:
            f.write(msg)
            f.close()
        with open('reagent_2_log.txt', 'r') as f:
            data = f.read()
            self.log.setText(data)
            f.close()

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.reagent_2_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        if self.reaction_type == 'Azide-alkyne cycloaddition':
            self.isomers_selection_window = isomers_selection.IsomersSelectionWindow(self.start_window, self,
                                                                                     self.reaction_type)
            self.isomers_selection_window.show()
        else:
            self.saving_options_window = saving_options.SavingOptionsWindow(self.start_window, self, self.reaction_type)
            self.saving_options_window.show()
