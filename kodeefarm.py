import sys
from PySide2.QtWidgets import QApplication, QMainWindow

from packages.login import Login

from templates.ui_kodeefarm import Ui_KodeeFarm


class KodeeFarm(QMainWindow, Ui_KodeeFarm):
    def __init__(self):
        super(KodeeFarm, self).__init__()
        self.setupUi(self)

    def login(self):
        self.login = Login()
        self.login.show()
    
    def main(self):
        self.kodee_farm = KodeeFarm()
        self.kodee_farm.show()
        self.login()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    kodee_farm = KodeeFarm()
    kodee_farm.main()
    app.exec_()