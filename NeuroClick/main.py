import sys

from logo import LogoWindow
from clear import delete_extra_files

from rdkit import RDLogger
from PyQt5.QtWidgets import QApplication


def application():
    app = QApplication(sys.argv)
    logo_window = LogoWindow()
    logo_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    RDLogger.DisableLog('rdApp.*')
    delete_extra_files()
    application()
