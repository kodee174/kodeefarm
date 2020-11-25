import sys
from PySide2.QtWidgets import QWidget

from apps.templates.ui_login import Ui_Login
from apps.models.user import User
from .home import Home


class Login(QWidget, Ui_Login):
    user = None
    def __init__(self):
        super(Login, self).__init__()
        self.setAutoFillBackground(True)
        self.setupUi(self)
        self.user = User()
        self.login_btn.clicked.connect(self.login)
        self.home = None

    def login(self):
        username_or_email = self.username_or_email_txt.text()
        password = self.password_txt.text()
        message = None
        if self.is_empty(username_or_email) or self.is_empty(password):
            message = 'Bạn chưa nhập tên tài khoản hoặc\nmật khẩu'
        elif not self.auth(username_or_email, password):
            message = 'Tên tài khoản/email hoặc mật khẩu\nkhông đúng'
        else:
            self.home = Home()
            self.home.show()
            self.close()

        self.message.setText(message)

    def auth(self, username_or_email, password):
        return self.user.auth(username_or_email, password)

    def is_empty(self, data):
        return data == None or data == ''