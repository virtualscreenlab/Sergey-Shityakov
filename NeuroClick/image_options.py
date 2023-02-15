from base_window import BaseWindow
from clear import delete_extra_files
from image_forming import ImageFormingWindow
from styles import *

import random
from PyQt5.QtWidgets import QRadioButton, QLabel


class ImageOptionsWindow(BaseWindow):
    def __init__(self, start_window, results_window, reaction_products, image_forming_window=None):
        super().__init__()

        self.info_label = QLabel(self)
        self.info_label.setGeometry(200, 190, 253, 40)
        self.info_label.setText('Do you want to visualize the library ?')

        self.no_image_check = QRadioButton('No', self)
        self.no_image_check.setGeometry(200, 220, 253, 40)
        self.no_image_check.toggled.connect(self.no_image_checked)

        self.random_image_check = QRadioButton('Visualize 5 random products', self)
        self.random_image_check.setGeometry(200, 250, 253, 40)
        self.random_image_check.toggled.connect(self.random_image_checked)

        self.both_isomers_check = QRadioButton('Visualize the whole library', self)
        self.both_isomers_check.setGeometry(200, 280, 253, 40)
        self.both_isomers_check.toggled.connect(self.whole_image_checked)

        self.warning_label = QLabel(self)
        self.warning_label.setGeometry(200, 310, 283, 40)
        self.warning_label.setStyleSheet('color: rgb(255, 0, 0);')

        self.start_window = start_window
        self.results_window = results_window
        self.reaction_products = reaction_products
        self.image_forming_window = image_forming_window
        self.image = False
        self.products_to_draw = None

        self.next_button.setText('')

    def calc_memory_usage(self, products_number):
        image_size = products_number * 6
        if image_size >= 1000000:
            self.warning_label.setText(
                f'Warning: file will require nearly {image_size // 1000000 + 1} GB')
        elif image_size >= 1000:
            self.warning_label.setText(
                f'Warning: file will require nearly {image_size // 1000 + 1} MB')

    def no_image_checked(self):
        self.image = False
        self.warning_label.setText('')
        self.next_button.setText('Restart')
        self.next_button.setStyleSheet(back_next_button_stylesheet)
        self.next_button.setEnabled(True)

    def random_image_checked(self):
        self.image = True
        self.warning_label.setText('')

        products_number = len(self.reaction_products)
        if products_number <= 5:
            self.products_to_draw = list(self.reaction_products.keys())
        else:
            start_index = random.randint(0, products_number - 5)
            end_index = start_index + 5
            self.products_to_draw = list(self.reaction_products.keys())[start_index:end_index]

        self.calc_memory_usage(len(self.products_to_draw))
        self.next_button.setText('Next')
        self.activate_next()

    def whole_image_checked(self):
        self.image = True
        self.warning_label.setText('')
        products_number = len(self.reaction_products)
        self.products_to_draw = list(self.reaction_products.keys())
        self.calc_memory_usage(products_number)
        self.next_button.setText('Next')
        self.activate_next()

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.results_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        if not self.image:
            delete_extra_files()
            self.start_window.show()
            self.start_window.input_azides.setText('')
        else:
            self.image_forming_window = ImageFormingWindow(self.start_window, self, self.products_to_draw)
            self.image_forming_window.show()
