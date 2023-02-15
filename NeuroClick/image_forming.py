from base_window import BaseWindow
from clear import files_to_delete, delete_extra_files
from image_saving import ImageSavingWindow
from styles import *

import os

from PIL import Image
from PyQt5 import QtWidgets
from PyQt5.Qt import *
from rdkit import Chem
from rdkit.Chem import Draw


def combine_png(png_name):
    file_list = os.listdir('.')
    im_list = []
    new_pic = []

    for x in file_list:
        if 'png' in x:
            new_pic.append(x)

    im1 = Image.open(new_pic[0])
    new_pic.pop(0)
    for i in new_pic:
        img = Image.open(i)
        if img.mode == "RGBA":
            img = img.convert('RGB')
            im_list.append(img)
        else:
            im_list.append(img)
    im1.save(png_name, "PNG", resolution=100.0, save_all=True, append_images=im_list)


class ProcessThread(QThread):
    start_signal = pyqtSignal()
    print_signal = pyqtSignal(str)
    finish_signal = pyqtSignal()

    def __init__(self, window, parent=None):
        super(ProcessThread, self).__init__(parent)
        self.window = window

    def run(self):
        self.window.clear_log()
        self.start_signal.emit()
        self.window.processed_products = 0
        self.print_signal.emit('Drawing triazoles, please wait...\n')
        try:
            for i in range(0, len(self.window.products_to_draw), 330):
                cur_products = self.window.products_to_draw[i: i + 330]
                self.window.processed_products += len(cur_products)
                mols_to_draw = [Chem.MolFromSmiles(product) for product in cur_products]
                img = Draw.MolsToGridImage(mols_to_draw, molsPerRow=5, subImgSize=(400, 400))
                img.save(f'triazoles_{i}.png')
                files_to_delete.append(f'triazoles_{i}.png')
                self.msleep(self.window.timeout)
        except Exception:
            self.print_signal.emit('Troubles drawing triazoles')
        self.print_signal.emit('Finished drawing!\n')
        self.finish_signal.emit()


class ImageFormingWindow(BaseWindow):
    def __init__(self, start_window, image_options_window, products_to_draw, image_saving_window=None):
        super().__init__()

        self.setFixedSize(1000, 700)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(170, 100, 700, 35)

        self.log = QtWidgets.QTextEdit(self)
        self.log.setGeometry(170, 180, 700, 290)
        self.log.setReadOnly(True)
        self.cursor = QTextCursor(self.log.document())
        self.log.setTextCursor(self.cursor)

        self.process_button = QtWidgets.QPushButton(self)
        self.process_button.setGeometry(190, 470, 660, 50)
        self.process_button.setText('Draw molecules')
        self.process_button.setStyleSheet(upload_button_stylesheet)
        self.process_button.clicked.connect(self.start_processing)

        self.next_button.setGeometry(880, 650, 95, 40)

        self.start_window = start_window
        self.image_options_window = image_options_window
        self.image_saving_window = image_saving_window
        self.products_to_draw = products_to_draw
        self.drawings_window = None

        self.process_thread = ProcessThread(self)
        self.process_thread.start_signal.connect(self.start_signal_process)
        self.process_thread.finish_signal.connect(self.finish_signal_process)
        self.process_thread.print_signal.connect(self.print_signal_process)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeout_func)

        products_length = len(self.products_to_draw)
        if products_length < 1000:
            self.timeout = 30
        elif 1000 <= products_length < 10000:
            self.timeout = 60
        elif 10000 <= products_length < 20000:
            self.timeout = 100
        elif 20000 <= products_length < 1000000:
            self.timeout = 300
        else:
            self.timeout = 500

        delete_extra_files('triazoles_only')

    def start_processing(self):
        self.process_button.setEnabled(False)
        self.progress_bar.setValue(0)
        self.process_thread.start()

    def start_signal_process(self):
        self.timer.start(self.timeout)

    def print_signal_process(self, msg):
        self.show_log(msg)

    def finish_signal_process(self):
        self.progress_bar.setValue(100)
        self.timer.stop()
        combine_png('triazoles.png')
        self.process_button.setEnabled(True)
        self.activate_next()

    def timeout_func(self):
        self.progress_bar.setValue(round(self.processed_products / len(self.products_to_draw) * 100))

    def clear_log(self):
        with open('imgs_log.txt', 'w') as f:
            f.write('')
            f.close()

    def show_log(self, msg):
        with open('imgs_log.txt', 'a') as f:
            f.write(msg)
            f.close()
        with open('imgs_log.txt', 'r') as f:
            data = f.read()
            self.log.setText(data)
            f.close()

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.image_options_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        if self.image_saving_window is None:
            self.image_saving_window = ImageSavingWindow(self.start_window, self)
        self.image_saving_window.show()
