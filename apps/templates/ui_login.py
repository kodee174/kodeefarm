# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(401, 266)
        self.verticalLayoutWidget = QWidget(Login)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 30, 241, 181))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.message = QLabel(self.verticalLayoutWidget)
        self.message.setObjectName(u"message")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setStyleSheet(u"text-align: center;")

        self.verticalLayout_4.addWidget(self.message)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.username_or_email_txt = QLineEdit(self.verticalLayoutWidget)
        self.username_or_email_txt.setObjectName(u"username_or_email_txt")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.username_or_email_txt)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.password_txt = QLineEdit(self.verticalLayoutWidget)
        self.password_txt.setObjectName(u"password_txt")
        self.password_txt.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password_txt)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(78, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.login_btn = QPushButton(self.verticalLayoutWidget)
        self.login_btn.setObjectName(u"login_btn")

        self.horizontalLayout_2.addWidget(self.login_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"\u0110\u0103ng nh\u1eadp", None))
        self.message.setText("")
        self.label.setText(QCoreApplication.translate("Login", u"T\u00e0i kho\u1ea3n", None))
        self.username_or_email_txt.setText(QCoreApplication.translate("Login", u"test", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"M\u1eadt kh\u1ea9u", None))
        self.password_txt.setText(QCoreApplication.translate("Login", u"test", None))
        self.login_btn.setText(QCoreApplication.translate("Login", u"\u0110\u0103ng nh\u1eadp", None))
    # retranslateUi

