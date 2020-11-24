import sys
from PySide2.QtWidgets import QApplication, QMainWindow

from apps.templates.ui_home import Ui_Home

class Home(QMainWindow, Ui_Home):
    def __init__(self):
        super(Home, self).__init__()
        self.setupUi(self)
