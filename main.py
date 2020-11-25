import sys
from PySide2.QtWidgets import QApplication

from apps.views.login import Login


if __name__ == '__main__':
    app = QApplication([])
    login = Login()
    login.show()
    sys.exit(app.exec_())
