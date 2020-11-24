import sys
from PySide2.QtWidgets import QApplication
from apps.views.home import Home
from apps.models.account import Account

if __name__ == '__main__':
    app = QApplication([])
    print(Account().auth('test', 'test').email)
    home = Home()
    home.show()
    sys.exit(app.exec_())
