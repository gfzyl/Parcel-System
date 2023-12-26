# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_main.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_user_main(object):
    def setupUi(self, user_main):
        if not user_main.objectName():
            user_main.setObjectName(u"user_main")
        user_main.resize(633, 341)
        user_main.setStyleSheet(u"\n"
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
        self.verticalLayout = QVBoxLayout(user_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QGroupBox(user_main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.gridLayout = QGridLayout(self.tabWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sendBtn = QPushButton(self.tabWidget)
        self.sendBtn.setObjectName(u"sendBtn")

        self.gridLayout.addWidget(self.sendBtn, 4, 2, 1, 1)

        self.searchBtn = QPushButton(self.tabWidget)
        self.searchBtn.setObjectName(u"searchBtn")

        self.gridLayout.addWidget(self.searchBtn, 4, 1, 1, 1)

        self.modifyInfoBtn = QPushButton(self.tabWidget)
        self.modifyInfoBtn.setObjectName(u"modifyInfoBtn")

        self.gridLayout.addWidget(self.modifyInfoBtn, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.label_4 = QLabel(self.tabWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 1, 1, 2)

        self.logoutBtn = QPushButton(self.tabWidget)
        self.logoutBtn.setObjectName(u"logoutBtn")

        self.gridLayout.addWidget(self.logoutBtn, 2, 4, 1, 1)

        self.label_3 = QLabel(self.tabWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 2)

        self.myReceiveBtn = QPushButton(self.tabWidget)
        self.myReceiveBtn.setObjectName(u"myReceiveBtn")

        self.gridLayout.addWidget(self.myReceiveBtn, 6, 1, 1, 1)

        self.label_2 = QLabel(self.tabWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 2)

        self.label_5 = QLabel(self.tabWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 3, 2, 1)

        self.label = QLabel(self.tabWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 4, 1, 1)

        self.mySendBtn = QPushButton(self.tabWidget)
        self.mySendBtn.setObjectName(u"mySendBtn")

        self.gridLayout.addWidget(self.mySendBtn, 6, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)


        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(user_main)

        QMetaObject.connectSlotsByName(user_main)
    # setupUi

    def retranslateUi(self, user_main):
        user_main.setWindowTitle(QCoreApplication.translate("user_main", u"\u7528\u6237\u4e3b\u754c\u9762", None))
        self.tabWidget.setTitle(QCoreApplication.translate("user_main", u"\u7528\u6237\u4e3b\u754c\u9762", None))
        self.sendBtn.setText(QCoreApplication.translate("user_main", u"\u6211\u8981\u5bc4\u5feb\u9012", None))
        self.searchBtn.setText(QCoreApplication.translate("user_main", u"\u6211\u8981\u67e5\u5feb\u9012", None))
        self.modifyInfoBtn.setText(QCoreApplication.translate("user_main", u"\u4fee\u6539\u4e2a\u4eba\u4fe1\u606f", None))
        self.label_4.setText("")
        self.logoutBtn.setText(QCoreApplication.translate("user_main", u"\u9000\u51fa\u767b\u5f55", None))
        self.label_3.setText("")
        self.myReceiveBtn.setText(QCoreApplication.translate("user_main", u"\u6211\u6536\u7684", None))
        self.label_2.setText("")
        self.label_5.setText("")
        self.label.setText("")
        self.mySendBtn.setText(QCoreApplication.translate("user_main", u"\u6211\u5bc4\u7684", None))
    # retranslateUi

