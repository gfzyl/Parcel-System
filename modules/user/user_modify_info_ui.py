# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_modify_info.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_user_modify_info(object):
    def setupUi(self, user_modify_info):
        if not user_modify_info.objectName():
            user_modify_info.setObjectName(u"user_modify_info")
        user_modify_info.resize(646, 415)
        user_modify_info.setStyleSheet(u"\n"
"            QLabel {\n"
"                color: #333;\n"
"                font:14px \"\u5e7c\u5706\";\n"
"                font-weight: bold;\n"
"            }\n"
"\n"
"            QLineEdit {\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 4px;\n"
"            }\n"
"\n"
"            QPushButton {\n"
"                padding: 8px 16px;\n"
"                font-size: 15px;\n"
"                font-weight: bold;\n"
"                border: 1px solid #4CAF50;\n"
"                border-radius: 4px;\n"
"                color: #fff;\n"
"                background-color: #4CAF50;\n"
"            }\n"
"\n"
"            #btn_update,\n"
"            #btn_change_password,\n"
"            #btn_change_phone {\n"
"                font-size: 13px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #45a049;\n"
"                border: 1px solid #45a049;\n"
"            }\n"
""
                        "\n"
"        ")
        self.verticalLayout = QVBoxLayout(user_modify_info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QGroupBox(user_modify_info)
        self.tabWidget.setObjectName(u"tabWidget")
        self.gridLayout_2 = QGridLayout(self.tabWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_viewAddressBook = QPushButton(self.tabWidget)
        self.btn_viewAddressBook.setObjectName(u"btn_viewAddressBook")

        self.horizontalLayout.addWidget(self.btn_viewAddressBook)


        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_newPassword = QLineEdit(self.tabWidget)
        self.lineEdit_newPassword.setObjectName(u"lineEdit_newPassword")
        self.lineEdit_newPassword.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.lineEdit_newPassword, 1, 1, 1, 1)

        self.label_new_password = QLabel(self.tabWidget)
        self.label_new_password.setObjectName(u"label_new_password")

        self.gridLayout.addWidget(self.label_new_password, 1, 0, 1, 1)

        self.lineEdit_newPhone = QLineEdit(self.tabWidget)
        self.lineEdit_newPhone.setObjectName(u"lineEdit_newPhone")

        self.gridLayout.addWidget(self.lineEdit_newPhone, 3, 1, 1, 1)

        self.lineEdit_oldPassword = QLineEdit(self.tabWidget)
        self.lineEdit_oldPassword.setObjectName(u"lineEdit_oldPassword")
        self.lineEdit_oldPassword.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.lineEdit_oldPassword, 0, 1, 1, 1)

        self.label_old_password = QLabel(self.tabWidget)
        self.label_old_password.setObjectName(u"label_old_password")

        self.gridLayout.addWidget(self.label_old_password, 0, 0, 1, 1)

        self.btn_changePhone = QPushButton(self.tabWidget)
        self.btn_changePhone.setObjectName(u"btn_changePhone")

        self.gridLayout.addWidget(self.btn_changePhone, 3, 2, 1, 1)

        self.label_new_phone = QLabel(self.tabWidget)
        self.label_new_phone.setObjectName(u"label_new_phone")

        self.gridLayout.addWidget(self.label_new_phone, 3, 0, 1, 1)

        self.label = QLabel(self.tabWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.lineEdit_againPassword = QLineEdit(self.tabWidget)
        self.lineEdit_againPassword.setObjectName(u"lineEdit_againPassword")

        self.gridLayout.addWidget(self.lineEdit_againPassword, 2, 1, 1, 1)

        self.btn_changePassword = QPushButton(self.tabWidget)
        self.btn_changePassword.setObjectName(u"btn_changePassword")

        self.gridLayout.addWidget(self.btn_changePassword, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 5, 1, 1, 1)


        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(user_modify_info)

        QMetaObject.connectSlotsByName(user_modify_info)
    # setupUi

    def retranslateUi(self, user_modify_info):
        user_modify_info.setWindowTitle(QCoreApplication.translate("user_modify_info", u"\u4fee\u6539\u4e2a\u4eba\u4fe1\u606f", None))
        self.tabWidget.setTitle(QCoreApplication.translate("user_modify_info", u"\u4e2a\u4eba\u4fe1\u606f", None))
        self.btn_viewAddressBook.setText(QCoreApplication.translate("user_modify_info", u"\u70b9\u51fb\u67e5\u770b\u5730\u5740\u7c3f\u4fe1\u606f", None))
        self.label_new_password.setText(QCoreApplication.translate("user_modify_info", u"\u65b0\u5bc6\u7801:", None))
        self.label_old_password.setText(QCoreApplication.translate("user_modify_info", u"\u65e7\u5bc6\u7801:", None))
        self.btn_changePhone.setText(QCoreApplication.translate("user_modify_info", u"\u4fee\u6539\u624b\u673a\u53f7", None))
        self.label_new_phone.setText(QCoreApplication.translate("user_modify_info", u"\u65b0\u624b\u673a\u53f7:", None))
        self.label.setText(QCoreApplication.translate("user_modify_info", u"\u65b0\u5bc6\u7801\uff1a", None))
        self.btn_changePassword.setText(QCoreApplication.translate("user_modify_info", u"\u4fee\u6539\u5bc6\u7801", None))
    # retranslateUi

