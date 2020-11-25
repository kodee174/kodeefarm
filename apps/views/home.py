import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTableView

from apps.templates.ui_home import Ui_Home

class Home(QMainWindow, Ui_Home):
    def __init__(self):
        super(Home, self).__init__()
        self.setupUi(self)
        
        self.account_btn.clicked.connect(self.handle_click_account)

    def handle_click_account(self):

        tabTexts = [self.tabWidget.tabText(index) for index in range(self.tabWidget.count())]

        if 'text' not in tabTexts:
            self.tabWidget.addTab(QTableView(), 'text')