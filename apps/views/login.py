import sys
from PySide2.QtWidgets import QWidget

from apps.templates.ui_login import Ui_Login


class Login(QWidget, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)