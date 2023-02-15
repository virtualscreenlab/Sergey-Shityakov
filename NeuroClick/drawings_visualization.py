from PyQt5.Qt import *


class Label(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self._update()

    def _update(self):
        w = self.window().w - 120 + self.window().delta_horizontal if self.window().w <= 710 else 590
        h = self.window().h - 120 + self.window().delta_vertical if self.window().h <= 674 else 554
        self.move(w, h)
        self.update()

    def mouse_press_event(self, event):
        self.setStyleSheet("QLabel:hover {border-radius: 4px; border: 2px solid #0ff;}")
        self.clicked.emit()
        super(Label, self).mouse_press_event(event)

    def enter_event(self, event):
        self.setStyleSheet("QLabel:hover {border-radius: 4px; border: 1px solid #f00;}")
        super(Label, self).enter_event(event)

    def leave_event(self, event):
        self.setStyleSheet("QLabel {border: none;}")
        super(Label, self).leave_event(event)


class Example(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.unit_UI()
        self.label_1 = Label(self.label)
        self.label_1.show()


    def unit_UI(self):
        self.pixmap = QPixmap("triazoles.png")
        hbox = QHBoxLayout(self)
        self.label = QLabel('text', self)
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(0, 0, 280, 280)
        hbox.addWidget(self.label)


class ScrollArea(QScrollArea):
    def __init__(self, *args, **kwargs):
        super(ScrollArea, self).__init__(*args, **kwargs)
        self.verticalScrollBar().actionTriggered.connect(self.on_action_triggered)
        self.horizontalScrollBar().actionTriggered.connect(self.on_action_triggered)

    def on_action_triggered(self):
        self.window().delta_vertical = self.verticalScrollBar().sliderPosition()
        if self.verticalScrollBar().sliderPosition() == self.verticalScrollBar().maximum():
            self.window().delta_vertical -= 10
        self.window().delta_horizontal = self.horizontalScrollBar().sliderPosition()
        if self.horizontalScrollBar().sliderPosition() == self.horizontalScrollBar().maximum():
            self.window().delta_horizontal -= 10
        self.window().widget.label_1._update()


class VisualizationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NeuroClick')
        self.setFixedSize(700, 700)
        self.setObjectName("MainWindow")
        self.w = 200
        self.h = 200
        self.delta_vertical = 0
        self.delta_horizontal = 0
        self.unit_UI()

    def unit_UI(self):
        self.scroll = ScrollArea(self)
        self.widget = Example(self)
        self.scroll.setBackgroundRole(QPalette.Dark)
        self.scroll.setWidget(self.widget)
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.scroll)

    def resize_event(self, event):
        delta = 0 if self.scroll.contentsRect().width() <= 695 else 20
        self.w = 200
        self.h = 200 + delta
        self.scroll.on_action_triggered()

    