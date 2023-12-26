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
        add_address_book.resize(570, 375)
        add_address_book.setMaximumSize(QSize(1000000, 16777215))
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
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.horizontalLayoutProvinceCity = QHBoxLayout()
        self.horizontalLayoutProvinceCity.setObjectName(u"horizontalLayoutProvinceCity")
        self.labelProvince = QLabel(self.groupBoxAddressBook)
        self.labelProvince.setObjectName(u"labelProvince")
        self.labelProvince.setMinimumSize(QSize(130, 0))

        self.horizontalLayoutProvinceCity.addWidget(self.labelProvince)

        self.comboBox_province = QComboBox(self.groupBoxAddressBook)
        self.comboBox_province.addItem("")
        self.comboBox_province.setObjectName(u"comboBox_province")

        self.horizontalLayoutProvinceCity.addWidget(self.comboBox_province)

        self.labelCity = QLabel(self.groupBoxAddressBook)
        self.labelCity.setObjectName(u"labelCity")

        self.horizontalLayoutProvinceCity.addWidget(self.labelCity)

        self.comboBox_city = QComboBox(self.groupBoxAddressBook)
        self.comboBox_city.setObjectName(u"comboBox_city")

        self.horizontalLayoutProvinceCity.addWidget(self.comboBox_city)


        self.gridLayout.addLayout(self.horizontalLayoutProvinceCity, 2, 1, 1, 1)

        self.horizontalLayoutAddButton = QHBoxLayout()
        self.horizontalLayoutAddButton.setObjectName(u"horizontalLayoutAddButton")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(self.groupBoxAddressBook)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_add)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_return = QPushButton(self.groupBoxAddressBook)
        self.btn_return.setObjectName(u"btn_return")
        self.btn_return.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_return)


        self.horizontalLayoutAddButton.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.horizontalLayoutAddButton, 6, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.horizontalLayoutAdd = QHBoxLayout()
        self.horizontalLayoutAdd.setObjectName(u"horizontalLayoutAdd")
        self.labelName = QLabel(self.groupBoxAddressBook)
        self.labelName.setObjectName(u"labelName")

        self.horizontalLayoutAdd.addWidget(self.labelName)

        self.lineEdit_name = QLineEdit(self.groupBoxAddressBook)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.horizontalLayoutAdd.addWidget(self.lineEdit_name)

        self.labelPhone = QLabel(self.groupBoxAddressBook)
        self.labelPhone.setObjectName(u"labelPhone")

        self.horizontalLayoutAdd.addWidget(self.labelPhone)

        self.lineEdit_phone = QLineEdit(self.groupBoxAddressBook)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")

        self.horizontalLayoutAdd.addWidget(self.lineEdit_phone)


        self.gridLayout.addLayout(self.horizontalLayoutAdd, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 6, 2, 1, 1)

        self.horizontalLayoutAddress = QHBoxLayout()
        self.horizontalLayoutAddress.setObjectName(u"horizontalLayoutAddress")
        self.labelAddress = QLabel(self.groupBoxAddressBook)
        self.labelAddress.setObjectName(u"labelAddress")

        self.horizontalLayoutAddress.addWidget(self.labelAddress)

        self.lineEdit_address = QLineEdit(self.groupBoxAddressBook)
        self.lineEdit_address.setObjectName(u"lineEdit_address")

        self.horizontalLayoutAddress.addWidget(self.lineEdit_address)


        self.gridLayout.addLayout(self.horizontalLayoutAddress, 4, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBoxAddressBook)


        self.retranslateUi(add_address_book)

        QMetaObject.connectSlotsByName(add_address_book)
    # setupUi

    def retranslateUi(self, add_address_book):
        add_address_book.setWindowTitle(QCoreApplication.translate("add_address_book", u"\u5730\u5740\u7c3f", None))
        self.groupBoxAddressBook.setTitle(QCoreApplication.translate("add_address_book", u"\u6dfb\u52a0\u5730\u5740\u7c3f", None))
        self.labelProvince.setText(QCoreApplication.translate("add_address_book", u"\u7701\u4efd\uff1a", None))
        self.comboBox_province.setItemText(0, "")

        self.labelCity.setText(QCoreApplication.translate("add_address_book", u"\u5730\u7ea7\u5e02\uff1a", None))
        self.btn_add.setText(QCoreApplication.translate("add_address_book", u"\u786e\u8ba4\u6dfb\u52a0", None))
        self.btn_return.setText(QCoreApplication.translate("add_address_book", u"\u8fd4\u56de\u4e0a\u4e00\u7ea7", None))
        self.labelName.setText(QCoreApplication.translate("add_address_book", u"\u59d3\u540d\uff1a", None))
        self.labelPhone.setText(QCoreApplication.translate("add_address_book", u"\u7535\u8bdd\uff1a", None))
        self.labelAddress.setText(QCoreApplication.translate("add_address_book", u"\u8be6\u7ec6\u5730\u5740\uff1a", None))
    # retranslateUi

