# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_sendout.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_user_sendout(object):
    def setupUi(self, user_sendout):
        if not user_sendout.objectName():
            user_sendout.setObjectName(u"user_sendout")
        user_sendout.resize(545, 619)
        self.groupBox = QGroupBox(user_sendout)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 521, 241))
        self.groupBox.setStyleSheet(u"\n"
"            QLabel {\n"
"                color: #333;\n"
"                font: 14px \"\u5e7c\u5706\";\n"
"                font-weight: bold;\n"
"            }\n"
"\n"
"            QLineEdit,\n"
"            QComboBox {\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 4px;\n"
"            }\n"
"\n"
"        ")
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 501, 201))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_name1 = QLineEdit(self.layoutWidget)
        self.lineEdit_name1.setObjectName(u"lineEdit_name1")

        self.horizontalLayout.addWidget(self.lineEdit_name1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_phone1 = QLineEdit(self.layoutWidget)
        self.lineEdit_phone1.setObjectName(u"lineEdit_phone1")

        self.horizontalLayout.addWidget(self.lineEdit_phone1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox_province1 = QComboBox(self.layoutWidget)
        self.comboBox_province1.addItem("")
        self.comboBox_province1.setObjectName(u"comboBox_province1")

        self.horizontalLayout_2.addWidget(self.comboBox_province1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_5)

        self.comboBox_city1 = QComboBox(self.layoutWidget)
        self.comboBox_city1.setObjectName(u"comboBox_city1")

        self.horizontalLayout_2.addWidget(self.comboBox_city1)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_address1 = QLineEdit(self.layoutWidget)
        self.lineEdit_address1.setObjectName(u"lineEdit_address1")

        self.gridLayout.addWidget(self.lineEdit_address1, 0, 1, 1, 1)

        self.label_in_address_book = QLabel(self.layoutWidget)
        self.label_in_address_book.setObjectName(u"label_in_address_book")

        self.gridLayout.addWidget(self.label_in_address_book, 1, 0, 1, 1)

        self.comboBox_addressBook1 = QComboBox(self.layoutWidget)
        self.comboBox_addressBook1.addItem("")
        self.comboBox_addressBook1.setObjectName(u"comboBox_addressBook1")

        self.gridLayout.addWidget(self.comboBox_addressBook1, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.groupBox_2 = QGroupBox(user_sendout)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 250, 521, 241))
        self.groupBox_2.setStyleSheet(u"\n"
"            QLabel {\n"
"                color: #333;\n"
"                font: 14px \"\u5e7c\u5706\";\n"
"                font-weight: bold;\n"
"            }\n"
"\n"
"            QLineEdit,\n"
"            QComboBox {\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 4px;\n"
"            }\n"
"        ")
        self.layoutWidget_2 = QWidget(self.groupBox_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 20, 501, 201))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_name2 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_name2.setObjectName(u"lineEdit_name2")

        self.horizontalLayout_4.addWidget(self.lineEdit_name2)

        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.lineEdit_phone2 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_phone2.setObjectName(u"lineEdit_phone2")

        self.horizontalLayout_4.addWidget(self.lineEdit_phone2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.label_8)

        self.comboBox_province2 = QComboBox(self.layoutWidget_2)
        self.comboBox_province2.addItem("")
        self.comboBox_province2.setObjectName(u"comboBox_province2")

        self.horizontalLayout_5.addWidget(self.comboBox_province2)

        self.label_9 = QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.label_9)

        self.comboBox_city2 = QComboBox(self.layoutWidget_2)
        self.comboBox_city2.setObjectName(u"comboBox_city2")

        self.horizontalLayout_5.addWidget(self.comboBox_city2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_address2 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_address2.setObjectName(u"lineEdit_address2")

        self.gridLayout_2.addWidget(self.lineEdit_address2, 0, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_in_address_book1 = QLabel(self.layoutWidget_2)
        self.label_in_address_book1.setObjectName(u"label_in_address_book1")

        self.gridLayout_2.addWidget(self.label_in_address_book1, 1, 0, 1, 1)

        self.comboBox_addressBook2 = QComboBox(self.layoutWidget_2)
        self.comboBox_addressBook2.addItem("")
        self.comboBox_addressBook2.setObjectName(u"comboBox_addressBook2")

        self.gridLayout_2.addWidget(self.comboBox_addressBook2, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.layoutWidget_3 = QWidget(user_sendout)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 500, 501, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"    color: #333;\n"
"    font: 14px \"\u5e7c\u5706\";\n"
"    font-weight: bold;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.lineEdit_extra = QLineEdit(self.layoutWidget_3)
        self.lineEdit_extra.setObjectName(u"lineEdit_extra")
        self.lineEdit_extra.setStyleSheet(u"  QLineEdit {\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 4px;\n"
"            }")

        self.horizontalLayout_7.addWidget(self.lineEdit_extra)

        self.layoutWidget1 = QWidget(user_sendout)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 560, 501, 40))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.submitBtn = QPushButton(self.layoutWidget1)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setStyleSheet(u"\n"
"             QPushButton {\n"
"                padding: 8px 16px;\n"
"                font-size: 15px;\n"
"                font-weight: bold;\n"
"                border: 1px solid #4CAF50;\n"
"                border-radius: 4px;\n"
"                color: #fff;\n"
"                background-color: #4CAF50;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #45a049;\n"
"                border: 1px solid #45a049;\n"
"            }\n"
"        ")

        self.horizontalLayout_8.addWidget(self.submitBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.returnBtn = QPushButton(self.layoutWidget1)
        self.returnBtn.setObjectName(u"returnBtn")
        self.returnBtn.setStyleSheet(u"\n"
"             QPushButton {\n"
"                padding: 8px 16px;\n"
"                font-size: 15px;\n"
"                font-weight: bold;\n"
"                border: 1px solid #4CAF50;\n"
"                border-radius: 4px;\n"
"                color: #fff;\n"
"                background-color: #4CAF50;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #45a049;\n"
"                border: 1px solid #45a049;\n"
"            }\n"
"        ")

        self.horizontalLayout_8.addWidget(self.returnBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.retranslateUi(user_sendout)

        QMetaObject.connectSlotsByName(user_sendout)
    # setupUi

    def retranslateUi(self, user_sendout):
        user_sendout.setWindowTitle(QCoreApplication.translate("user_sendout", u"\u7528\u6237\u5bc4\u4ef6", None))
        self.groupBox.setTitle(QCoreApplication.translate("user_sendout", u"\u5bc4\u4ef6\u4eba\u5730\u5740\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("user_sendout", u"\u5bc4\u4ef6\u4eba\u59d3\u540d:", None))
        self.label_2.setText(QCoreApplication.translate("user_sendout", u"\u5bc4\u4ef6\u4eba\u7535\u8bdd:", None))
        self.label_4.setText(QCoreApplication.translate("user_sendout", u"\u7701:", None))
        self.comboBox_province1.setItemText(0, "")

        self.label_5.setText(QCoreApplication.translate("user_sendout", u"\u5e02:", None))
        self.label_6.setText(QCoreApplication.translate("user_sendout", u"\u8be6\u7ec6\u5730\u5740:", None))
        self.label_in_address_book.setText(QCoreApplication.translate("user_sendout", u"\u5728\u5730\u5740\u7c3f\u4e2d\u9009\u62e9", None))
        self.comboBox_addressBook1.setItemText(0, "")

        self.groupBox_2.setTitle(QCoreApplication.translate("user_sendout", u"\u6536\u4ef6\u4eba\u5730\u5740\u4fe1\u606f", None))
        self.label_3.setText(QCoreApplication.translate("user_sendout", u"\u6536\u4ef6\u4eba\u59d3\u540d:", None))
        self.label_7.setText(QCoreApplication.translate("user_sendout", u"\u6536\u4ef6\u4eba\u7535\u8bdd:", None))
        self.label_8.setText(QCoreApplication.translate("user_sendout", u"\u7701:", None))
        self.comboBox_province2.setItemText(0, "")

        self.label_9.setText(QCoreApplication.translate("user_sendout", u"\u5e02:", None))
        self.label_10.setText(QCoreApplication.translate("user_sendout", u"\u8be6\u7ec6\u5730\u5740:", None))
        self.label_in_address_book1.setText(QCoreApplication.translate("user_sendout", u"\u5728\u5730\u5740\u7c3f\u4e2d\u9009\u62e9", None))
        self.comboBox_addressBook2.setItemText(0, "")

        self.label_11.setText(QCoreApplication.translate("user_sendout", u"\u5907\u6ce8:", None))
        self.submitBtn.setText(QCoreApplication.translate("user_sendout", u"\u63d0\u4ea4\u8ba2\u5355", None))
        self.returnBtn.setText(QCoreApplication.translate("user_sendout", u"\u8fd4\u56de\u4e0a\u4e00\u7ea7", None))
    # retranslateUi

