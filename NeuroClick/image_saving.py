from base_window import BaseWindow
from clear import delete_extra_files
from drawings_visualization import VisualizationWindow
from styles import *

import shutil
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel


class ImageSavingWindow(BaseWindow):
    def __init__(self, start_window, image_forming_window):
        super().__init__()

        self.setWindowTitle('NeuroClick')
        self.setFixedSize(600, 700)
        self.setObjectName("MainWindow")

        self.visualize_library = QtWidgets.QPushButton(self)
        self.visualize_library.clicked.connect(self.visualize_images)
        self.visualize_library.setText('View triazoles image')
        self.visualize_library.setGeometry(170, 240, 243, 40)
        self.visualize_library.setStyleSheet(upload_button_stylesheet)

        self.save_library = QtWidgets.QPushButton(self)
        self.save_library.clicked.connect(self.save_images)
        self.save_library.setText('Save image')
        self.save_library.setGeometry(170, 280, 243, 40)
        self.save_library.setStyleSheet(upload_button_stylesheet)

        self.log_label = QLabel(self)
        self.log_label.setGeometry(190, 320, 273, 40)

        self.activate_next()
        self.next_button.setText('Restart')
        self.start_window = start_window
        self.image_forming_window = image_forming_window
        self.visualization_window = None

        self.image_saved = False

    def visualize_images(self):
        if not self.image_saved:
            self.log_label.setText('')
            self.visualization_window = VisualizationWindow()
            self.visualization_window.show()
        else:
            self.log_label.setText('Image already saved. See it locally')

    def save_images(self):
        if not self.image_saved:
            fname = QFileDialog.getExistingDirectory(caption='Save file', directory='.')
            try:
                shutil.move('triazoles.png', fname)
                self.image_saved = True
                self.log_label.setText('Image file downloaded successfully!')
            except Exception:
                pass
        else:
            self.log_label.setText('Image already saved. See it locally')

    def back_step(self):
        self.back_clicked = True
        self.close()
        self.image_forming_window.show()

    def next_step(self):
        self.next_clicked = True
        self.close()
        delete_extra_files()
        self.start_window.show()
        self.start_window.input_azides.setText('')
