# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_address_book.ui'
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

class Ui_add_address_book(object):
    def setupUi(self, add_address_book):
        if not add_address_book.objectName():
            add_address_book.setObjectName(u"add_address_book")
        add_address_book.resize(626, 329)
        self.verticalLayout = QVBoxLayout(add_address_book)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxAddressBook = QGroupBox(add_address_book)
        self.groupBoxAddressBook.setObjectName(u"groupBoxAddressBook")
        self.groupBoxAddressBook.setStyleSheet(u"\n"
"            QLabel {\n"
"                color: #333;\n"
"                font: 14px \"\u5e7c\u5706\";\n"
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
"            QComboBox {\n"
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
"            QPushButton:hover {\n"
"                background-color: #45a049;\n"
"                borde"
                        "r: 1px solid #45a049;\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #3e8e41;\n"
"            }\n"
"        ")
        self.gridLayout = QGridLayout(self.groupBoxAddressBook)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 0, 1, 1)

        self.horizontalLayoutProvinceCity = QHBoxLayout()
        self.horizontalLayoutProvinceCity.setObjectName(u"horizontalLayoutProvinceCity")
        self.labelProvince = QLabel(self.groupBoxAddressBook)
        self.labelProvince.setObjectName(u"labelProvince")
        self.labelProvince.setMinimumSize(QSize(130, 0))

        self.horizontalLayoutProvinceCity.addWidget(self.labelProvince)

        self.comboBoxProvince = QComboBox(self.groupBoxAddressBook)
        self.comboBoxProvince.setObjectName(u"comboBoxProvince")

        self.horizontalLayoutProvinceCity.addWidget(self.comboBoxProvince)

        self.labelCity = QLabel(self.groupBoxAddressBook)
        self.labelCity.setObjectName(u"labelCity")

        self.horizontalLayoutProvinceCity.addWidget(self.labelCity)

        self.comboBoxCity = QComboBox(self.groupBoxAddressBook)
        self.comboBoxCity.setObjectName(u"comboBoxCity")

        self.horizontalLayoutProvinceCity.addWidget(self.comboBoxCity)


        self.gridLayout.addLayout(self.horizontalLayoutProvinceCity, 2, 1, 1, 1)

        self.horizontalLayoutAddButton = QHBoxLayout()
        self.horizontalLayoutAddButton.setObjectName(u"horizontalLayoutAddButton")
        self.btnAdd = QPushButton(self.groupBoxAddressBook)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setStyleSheet(u"")

        self.horizontalLayoutAddButton.addWidget(self.btnAdd)


        self.gridLayout.addLayout(self.horizontalLayoutAddButton, 6, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.horizontalLayoutAdd = QHBoxLayout()
        self.horizontalLayoutAdd.setObjectName(u"horizontalLayoutAdd")
        self.labelName = QLabel(self.groupBoxAddressBook)
        self.labelName.setObjectName(u"labelName")

        self.horizontalLayoutAdd.addWidget(self.labelName)

        self.lineEditName = QLineEdit(self.groupBoxAddressBook)
        self.lineEditName.setObjectName(u"lineEditName")

        self.horizontalLayoutAdd.addWidget(self.lineEditName)

        self.labelPhone = QLabel(self.groupBoxAddressBook)
        self.labelPhone.setObjectName(u"labelPhone")

        self.horizontalLayoutAdd.addWidget(self.labelPhone)

        self.lineEditPhone = QLineEdit(self.groupBoxAddressBook)
        self.lineEditPhone.setObjectName(u"lineEditPhone")

        self.horizontalLayoutAdd.addWidget(self.lineEditPhone)


        self.gridLayout.addLayout(self.horizontalLayoutAdd, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.horizontalLayoutAddress = QHBoxLayout()
        self.horizontalLayoutAddress.setObjectName(u"horizontalLayoutAddress")
        self.labelAddress = QLabel(self.groupBoxAddressBook)
        self.labelAddress.setObjectName(u"labelAddress")

        self.horizontalLayoutAddress.addWidget(self.labelAddress)

        self.lineEditAddress = QLineEdit(self.groupBoxAddressBook)
        self.lineEditAddress.setObjectName(u"lineEditAddress")

        self.horizontalLayoutAddress.addWidget(self.lineEditAddress)


        self.gridLayout.addLayout(self.horizontalLayoutAddress, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 6, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBoxAddressBook)


        self.retranslateUi(add_address_book)

        QMetaObject.connectSlotsByName(add_address_book)
    # setupUi

    def retranslateUi(self, add_address_book):
        add_address_book.setWindowTitle(QCoreApplication.translate("add_address_book", u"\u5730\u5740\u7c3f", None))
        self.groupBoxAddressBook.setTitle(QCoreApplication.translate("add_address_book", u"\u6dfb\u52a0\u5730\u5740\u7c3f", None))
        self.labelProvince.setText(QCoreApplication.translate("add_address_book", u"\u7701\u4efd\uff1a", None))
        self.labelCity.setText(QCoreApplication.translate("add_address_book", u"\u5730\u7ea7\u5e02\uff1a", None))
        self.btnAdd.setText(QCoreApplication.translate("add_address_book", u"\u786e\u8ba4\u6dfb\u52a0", None))
        self.labelName.setText(QCoreApplication.translate("add_address_book", u"\u59d3\u540d\uff1a", None))
        self.labelPhone.setText(QCoreApplication.translate("add_address_book", u"\u7535\u8bdd\uff1a", None))
        self.labelAddress.setText(QCoreApplication.translate("add_address_book", u"\u8be6\u7ec6\u5730\u5740\uff1a", None))
    # retranslateUi

