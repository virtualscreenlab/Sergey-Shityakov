import reaction_selection
from base_window import BaseWindow
from styles import *

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush


class LogoWindow(BaseWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(700, 428)

        oImage = QImage("logo.jpg")
        sImage = oImage.scaled(QSize(700, 428))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.back_button.hide()

        self.next_button.setGeometry(310, 260, 80, 40)
        self.next_button.setText('Start')
        self.next_button.setStyleSheet(start_button_stylesheet)
        self.next_button.setEnabled(True)

        self.reaction_selection_window = None

    def next_step(self):
        self.next_clicked = True
        self.close()
        self.reaction_selection_window = reaction_selection.ReactionSelectionWindow(self)
        self.reaction_selection_window.show()
