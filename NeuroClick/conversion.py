import saving_converted_products

from base_window import BaseWindow
from clear import files_to_delete
from styles import *
from time_functions import time_format

import glob
import os
import time
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPalette, QBrush

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
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


class ProcessThread(QThread):
    start_signal = pyqtSignal()
    print_signal = pyqtSignal(str)
    finish_signal = pyqtSignal()

    def __init__(self, window, parent=None):
        super(ProcessThread, self).__init__(parent)
        self.window = window

    def run(self):
        temp_file = 'C:/Users/Anastasiia/Downloads/convert_out.' + self.window.conversion_format
        converted_file = 'conversions/output.' + self.window.conversion_format
        files_to_delete.append(converted_file)

        self.window.clear_log()
        try:
            os.remove(temp_file)
        except Exception:
            pass

        with open(converted_file, 'w') as f:
            f.write('')

        start_time = time.time()

        self.window.driver.get('https://datascience.unm.edu/tomcat/biocomp/convert')
        self.start_signal.emit()
        self.print_signal.emit('Calculations started...\n')
        for i in range(0, self.window.products_length, 50):
            start_index = i
            end_index = min(self.window.products_length, i + 50)
            cur_products = self.window.products[start_index:end_index]
            cur_products = ''.join(cur_products)

            input_select = Select(self.window.driver.find_element(by=By.NAME, value='ifmt'))
            input_select.select_by_value('smiles')
            input_area = self.window.driver.find_element(by=By.NAME, value='intxt')
            input_area.clear()
            input_area.send_keys(cur_products)
            time.sleep(10)

            output_select = Select(self.window.driver.find_element(by=By.NAME, value='ofmt'))
            output_select.select_by_value(self.window.conversion_format)
            if self.window.coordinates['2d']:
                c2d_button = self.window.driver.find_element(by=By.NAME, value='add_2d')
                c2d_button.click()
            if self.window.coordinates['3d']:
                c3d_button = self.window.driver.find_element(by=By.NAME, value='add_3d')
                c3d_button.click()

            convert_button = self.window.driver.find_element(by=By.XPATH, value='/html/body/form[1]/center/button')
            convert_button.click()
            time.sleep(10)

            download_button = self.window.driver.find_element(by=By.XPATH, value='/html/body/form[2]/button')
            download_button.click()
            while not (glob.glob(r'C:\Users\Anastasiia\Downloads\convert_out.' + self.window.conversion_format)):
                time.sleep(1)

            with open(temp_file) as f:
                converted_data = ''.join(f.readlines())
            with open(converted_file, 'a') as f:
                f.write(converted_data)
            os.remove(temp_file)

            self.window.log.moveCursor(QtGui.QTextCursor.End)
            self.msleep(self.window.timeout)
        self.window.driver.close()
        end_time = time.time()
        self.window.hours, self.window.minutes, self.window.seconds = time_format(start_time, end_time)
        self.finish_signal.emit()


class ConversionWindow(BaseWindow):
    def __init__(self, start_window, conversion_format_selection_window, conversion_format, coordinates):
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
        self.process_button.setText('Start conversion')
        self.process_button.setStyleSheet(upload_button_stylesheet)
        self.process_button.clicked.connect(self.start_processing)

        self.back_button.setStyleSheet(back_next_process_button_stylesheet)
        self.next_button.setGeometry(880, 650, 95, 40)

        self.start_window = start_window
        self.conversion_format_selection_window = conversion_format_selection_window
        self.conversion_format = conversion_format
        self.coordinates = coordinates

        with open('output.txt') as f:
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
            self.timeout = 200
        elif 10000 <= self.products_length < 20000:
            self.timeout = 300
        elif 20000 <= self.products_length < 1000000:
            self.timeout = 500
        else:
            self.timeout = 1000

        self.clear_log()
        self.log.setText('Products molecules were successfully uploaded')

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
        self.progress_bar.setValue(round((self.progress_value + 0.01) / self.products_length * 100))
        self.progress_value += 0.01

    def form_stats_log(self, hours, minutes, seconds):
        self.show_log('\n\n')
        self.show_log('====\n')
        self.show_log('Finished!\n')
        self.show_log(f'Time: {hours:02}:{minutes:02}:{seconds:02}.\n')
        self.activate_next(process=True)

    def clear_log(self):
        with open('conversion_log.txt', 'w') as f:
            f.write('')
            f.close()

    def show_log(self, msg):
        with open('conversion_log.txt', 'a') as f:
            f.write(msg)
            f.close()
        with open('conversion_log.txt', 'r') as f:
            data = f.read()
            self.log.setText(data)
            f.close()

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.conversion_format_selection_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        self.saving_converted_products_window = saving_converted_products.SavingConvertedProductsWindow(
            self.start_window, self, self.conversion_format)
        self.saving_converted_products_window.show()
