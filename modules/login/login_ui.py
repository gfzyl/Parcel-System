# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(603, 334)
        self.verticalLayout = QVBoxLayout(login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"\u5e7c\u5706\";\n"
"    font-weight: bold;\n"
"}")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel#label {\n"
"	font: 22pt \"\u5e7c\u5706\";\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.lineEdit_account = QLineEdit(login)
        self.lineEdit_account.setObjectName(u"lineEdit_account")
        self.lineEdit_account.setStyleSheet(u"QLineEdit {\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"}")

        self.gridLayout.addWidget(self.lineEdit_account, 1, 1, 1, 1)

        self.label_3 = QLabel(login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"\u5e7c\u5706\";\n"
"    font-weight: bold;\n"
"}")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_password = QLineEdit(login)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setStyleSheet(u"QLineEdit {\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_password, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton_login = QPushButton(login)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"	font: 15px \"\u5e7c\u5706\";\n"
"    font-weight: bold;\n"
"    border: 1px solid #4CAF50;\n"
"    border-radius: 4px;\n"
"    color: #fff;\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"/* \u9f20\u6807\u60ac\u505c\u65f6\u6309\u94ae\u6837\u5f0f */\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"    border: 1px solid #45a049;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_login)

        self.pushButton_register = QPushButton(login)
        self.pushButton_register.setObjectName(u"pushButton_register")
        self.pushButton_register.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"	font: 15px \"\u5e7c\u5706\";\n"
"    font-weight: bold;\n"
"    border: 1px solid #4CAF50;\n"
"    border-radius: 4px;\n"
"    color: #fff;\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"/* \u9f20\u6807\u60ac\u505c\u65f6\u6309\u94ae\u6837\u5f0f */\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"    border: 1px solid #45a049;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_register)

        self.pushButton = QPushButton(login)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"/* \u8bbe\u7f6e\u6309\u94ae\u6837\u5f0f */\n"
"QPushButton {\n"
"    padding: 8px 16px;\n"
"	font: 15px \"\u5e7c\u5706\";\n"
"    font-weight: bold;\n"
"    border: 1px solid #4CAF50;\n"
"    border-radius: 4px;\n"
"    color: #fff;\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"/* \u9f20\u6807\u60ac\u505c\u65f6\u6309\u94ae\u6837\u5f0f */\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"    border: 1px solid #45a049;\n"
"}\n"
"\n"
"/* \u6e38\u5ba2\u8bbf\u95ee\u6309\u94ae\u6837\u5f0f */\n"
"QPushButton#pushButton_visitor {\n"
"    color: #333;\n"
"    background-color: #ddd;\n"
"    border: 1px solid #ddd;\n"
"}\n"
"\n"
"/* \u9f20\u6807\u60ac\u505c\u65f6\u6e38\u5ba2\u8bbf\u95ee\u6309\u94ae\u6837\u5f0f */\n"
"QPushButton#pushButton_visitor:hover {\n"
"    background-color: #bbb;\n"
"    border: 1px solid #bbb;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"\u767b\u5165\u7cfb\u7edf", None))
        self.label_2.setText(QCoreApplication.translate("login", u"\u8d26\u53f7:", None))
        self.label.setText(QCoreApplication.translate("login", u"\u5feb\u9012\u7269\u6d41\u7ba1\u7406\u7cfb\u7edf", None))
        self.label_3.setText(QCoreApplication.translate("login", u"\u5bc6\u7801:", None))
        self.pushButton_login.setText(QCoreApplication.translate("login", u"\u767b\u5f55", None))
        self.pushButton_register.setText(QCoreApplication.translate("login", u"\u6ce8\u518c", None))
        self.pushButton.setText(QCoreApplication.translate("login", u"\u6e38\u5ba2\u8bbf\u95ee", None))
    # retranslateUi

