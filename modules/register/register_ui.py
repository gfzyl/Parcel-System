# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_register(object):
    def setupUi(self, register):
        if not register.objectName():
            register.setObjectName(u"register")
        register.resize(623, 442)
        self.verticalLayout = QVBoxLayout(register)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(register)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"\n"
"            QLabel#label {\n"
"                font: 22pt \"\u5e7c\u5706\";\n"
"                font-weight: bold;\n"
"                qproperty-alignment: AlignCenter;\n"
"            }\n"
"        ")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.phoneInput = QLineEdit(register)
        self.phoneInput.setObjectName(u"phoneInput")
        self.phoneInput.setStyleSheet(u"\n"
"            QLineEdit {\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 4px;\n"
"            }\n"
"    ")

        self.gridLayout.addWidget(self.phoneInput, 1, 1, 1, 1)

        self.phtonLabel = QLabel(register)
        self.phtonLabel.setObjectName(u"phtonLabel")
        self.phtonLabel.setStyleSheet(u"\n"
"            QLabel {\n"
"                font: 12pt \"\u5e7c\u5706\";\n"
"                font-weight: bold;\n"
"            }\n"
"        ")

        self.gridLayout.addWidget(self.phtonLabel, 1, 0, 1, 1)

        self.pwdInput = QLineEdit(register)
        self.pwdInput.setObjectName(u"pwdInput")
        self.pwdInput.setStyleSheet(u"\n"
"            QLineEdit {\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 4px;\n"
"            }\n"
"        ")
        self.pwdInput.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.pwdInput, 2, 1, 1, 1)

        self.pwdLabel = QLabel(register)
        self.pwdLabel.setObjectName(u"pwdLabel")
        self.pwdLabel.setStyleSheet(u"\n"
"            QLabel {\n"
"                font: 12pt \"\u5e7c\u5706\";\n"
"                font-weight: bold;\n"
"            }\n"
"        ")

        self.gridLayout.addWidget(self.pwdLabel, 2, 0, 1, 1)

        self.confirmPwdLabel = QLabel(register)
        self.confirmPwdLabel.setObjectName(u"confirmPwdLabel")
        self.confirmPwdLabel.setStyleSheet(u"\n"
"            QLabel {\n"
"                font: 12pt \"\u5e7c\u5706\";\n"
"                font-weight: bold;\n"
"            }\n"
"        ")

        self.gridLayout.addWidget(self.confirmPwdLabel, 3, 0, 1, 1)

        self.confirmPwdInput = QLineEdit(register)
        self.confirmPwdInput.setObjectName(u"confirmPwdInput")
        self.confirmPwdInput.setStyleSheet(u"\n"
"            QLineEdit {\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 4px;\n"
"            }\n"
"    ")
        self.confirmPwdInput.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.confirmPwdInput, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.registerBtn = QPushButton(register)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setStyleSheet(u"\n"
"        QPushButton {\n"
"            padding: 8px 16px;\n"
"            font: 15px \"\u5e7c\u5706\";\n"
"            font-weight: bold;\n"
"            border: 1px solid #4CAF50;\n"
"            border-radius: 4px;\n"
"            color: #fff;\n"
"            background-color: #4CAF50;\n"
"        }\n"
"\n"
"        /* \u9f20\u6807\u60ac\u505c\u65f6\u6309\u94ae\u6837\u5f0f */\n"
"        QPushButton:hover {\n"
"            background-color: #45a049;\n"
"            border: 1px solid #45a049;\n"
"        }\n"
"        ")

        self.verticalLayout.addWidget(self.registerBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(register)

        QMetaObject.connectSlotsByName(register)
    # setupUi

    def retranslateUi(self, register):
        register.setWindowTitle(QCoreApplication.translate("register", u"\u767b\u5165\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("register", u"\u5feb\u9012\u7269\u6d41\u7ba1\u7406\u7cfb\u7edf", None))
        self.phtonLabel.setText(QCoreApplication.translate("register", u"\u624b\u673a\u53f7", None))
        self.pwdLabel.setText(QCoreApplication.translate("register", u"\u5bc6\u7801:", None))
        self.confirmPwdLabel.setText(QCoreApplication.translate("register", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.registerBtn.setText(QCoreApplication.translate("register", u"\u786e\u8ba4\u6ce8\u518c", None))
    # retranslateUi

