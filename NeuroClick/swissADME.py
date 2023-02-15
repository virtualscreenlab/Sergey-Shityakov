import saving_products
from base_window import BaseWindow
from downloads_filtering import filter
from styles import *
from time_functions import time_format

import glob
import os
import pandas as pd
import time
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPalette, QBrush

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


def create_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_prefs = {"download.default_directory": r"C:\Users\Anastasiia\Downloads"}  # (windows)
    chrome_options.experimental_options["prefs"] = chrome_prefs
    driver = webdriver.Chrome(options=chrome_options,
                              service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    return driver


def get_correct_mol_number(mol_string, number):
    cur_number = int(mol_string.split(' ')[1])
    return mol_string.replace(str(cur_number), str(cur_number + number))


class ProcessThread(QThread):
    start_signal = pyqtSignal()
    print_signal = pyqtSignal(str)
    finish_signal = pyqtSignal()

    def __init__(self, window, parent=None):
        super(ProcessThread, self).__init__(parent)
        self.window = window

    def run(self):
        self.window.clear_log()
        try:
            os.remove('C:/Users/Anastasiia/Downloads/swissadme.csv')
        except Exception:
            pass
        start_time = time.time()

        self.window.result_df = pd.DataFrame({})
        self.window.driver.get('http://www.swissadme.ch/')
        self.start_signal.emit()
        self.print_signal.emit('ADME calculations started...\n')
        for i in range(0, self.window.products_length, 5):
            start_index = i
            end_index = min(self.window.products_length, i + 5)
            adme_products = []
            for product in self.window.products[start_index:end_index]:
                if len(product) < 200:
                    adme_products.append(product)
            adme_products = ''.join(adme_products)
            # print(adme_products)

            input_field = self.window.driver.find_element(by=By.XPATH,
                                                          value='/html/body/div/div[3]/div[2]/div/div[4]/form/textarea')
            input_field.clear()
            input_field.send_keys(adme_products)
            submit_button = self.window.driver.find_element(by=By.ID, value='submitButton')
            submit_button.click()
            save_csv_button = self.window.driver.find_element(by=By.XPATH,
                                                              value='/html/body/div/div[3]/div[2]/div/div[7]/a[1]/img')
            save_csv_button.click()
            while not (glob.glob(r'C:\Users\Anastasiia\Downloads\swissadme.csv')):
                time.sleep(2)

            df = pd.read_csv('C:/Users/Anastasiia/Downloads/swissadme.csv')

            df = df.loc[:, df.columns.isin(self.window.cols_to_use)]
            df['Molecule'] = df['Molecule'].apply(get_correct_mol_number, args=(i,))
            filter(i, df, self.window.cols_to_use, self.window.threshold_cols, self.window.violations_cols,
                   self.window.gi_level, self.window.saving_format)
            os.remove('C:/Users/Anastasiia/Downloads/swissadme.csv')
            self.window.log.moveCursor(QtGui.QTextCursor.End)
            self.msleep(self.window.timeout)
        self.window.driver.close()
        end_time = time.time()
        self.window.hours, self.window.minutes, self.window.seconds = time_format(start_time, end_time)
        self.finish_signal.emit()


class SwissADMEWindow(BaseWindow):
    def __init__(self, start_window, more_descriptors_selection_window, cols_to_use, threshold_cols, violations_cols,
                 gi_level, saving_format):
        super().__init__()

        self.setFixedSize(1000, 700)

        oImage = QImage("chem_back.jpg")
        sImage = oImage.scaled(QSize(1000, 700))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

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
        self.process_button.setText('Start products processing')
        self.process_button.setStyleSheet(upload_button_stylesheet)
        self.process_button.clicked.connect(self.start_processing)

        self.back_button.setStyleSheet(back_next_process_button_stylesheet)
        self.next_button.setGeometry(880, 650, 95, 40)

        self.start_window = start_window
        self.more_descriptors_selection_window = more_descriptors_selection_window
        self.cols_to_use = cols_to_use
        self.threshold_cols = threshold_cols
        self.violations_cols = violations_cols
        self.gi_level = gi_level
        self.saving_format = saving_format

        with open('products.txt') as f:
            self.products = f.readlines()

        self.process_thread = ProcessThread(self)
        self.process_thread.start_signal.connect(self.start_signal_process)
        self.process_thread.finish_signal.connect(self.finish_signal_process)
        self.process_thread.print_signal.connect(self.print_signal_process)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeout_func)

        self.products_length = len(self.products)
        if self.products_length < 1000:
            self.timeout = 50
        elif 1000 <= self.products_length < 10000:
            self.timeout = 150
        elif 10000 <= self.products_length < 20000:
            self.timeout = 250
        elif 20000 <= self.products_length < 1000000:
            self.timeout = 450
        else:
            self.timeout = 950

        self.clear_log()
        self.log.setText('Products were successfully uploaded')

    def start_processing(self):
        self.log.setText('Connecting the remote server, please wait a minute...')
        self.driver = create_driver()
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
        self.form_stats_log(self.hours, self.minutes, self.seconds)

    def timeout_func(self):
        self.progress_bar.setValue(round((self.progress_value + 0.005) / self.products_length * 100))
        self.progress_value += 0.005

    def form_stats_log(self, hours, minutes, seconds):
        self.show_log('\n\n')
        self.show_log('====\n')
        self.show_log('Finished calculating!\n')
        self.show_log(f'Time: {hours:02}:{minutes:02}:{seconds:02}.\n')
        self.activate_next(process=True)

    def clear_log(self):
        with open('swissADME_log.txt', 'w') as f:
            f.write('')
            f.close()

    def show_log(self, msg):
        with open('swissADME_log.txt', 'a') as f:
            f.write(msg)
            f.close()
        with open('swissADME_log.txt', 'r') as f:
            data = f.read()
            self.log.setText(data)
            f.close()

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.more_descriptors_selection_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        self.saving_products_window = saving_products.SavingProductsWindow(self.start_window, self, self.saving_format)
        self.saving_products_window.show()
