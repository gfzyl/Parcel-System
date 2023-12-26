# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'address_book.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_address_book(object):
    def setupUi(self, address_book):
        if not address_book.objectName():
            address_book.setObjectName(u"address_book")
        address_book.resize(668, 442)
        self.verticalLayout = QVBoxLayout(address_book)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxAddressBook = QGroupBox(address_book)
        self.groupBoxAddressBook.setObjectName(u"groupBoxAddressBook")
        self.groupBoxAddressBook.setStyleSheet(u"\n"
"            QTableWidget {\n"
"                font: 14px \"\u5e7c\u5706\";\n"
"                background-color: #cdefff;\n"
"            }\n"
"\n"
"            QTableWidget::item {\n"
"                font: 14px \"\u5e7c\u5706\";\n"
"            }\n"
"\n"
"            QHeaderView {\n"
"                font: bold 16px \"\u5e7c\u5706\";\n"
"            }\n"
"\n"
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
"            QTableWidget::item:selected {\n"
"                background-color: #a6a6a6;\n"
"            }\n"
"\n"
"            QTableWidget QHeaderView::section {\n"
"                background-color: #65a3ff;\n"
"                color: white;\n"
"                font-weight: b"
                        "old;\n"
"                font-size: 16px;\n"
"                 padding: 2px;\n"
"            }\n"
"\n"
"            QTableWidget::item {\n"
"                padding: 10px;\n"
"            }\n"
"\n"
"            QTableWidget::item[\u5217\u540d=\"\u8be6\u7ec6\u5730\u5740\"] {\n"
"                width: 300px; /* Adjust the width as needed */\n"
"            }\n"
"        ")
        self.horizontalLayoutAddressBook = QHBoxLayout(self.groupBoxAddressBook)
        self.horizontalLayoutAddressBook.setObjectName(u"horizontalLayoutAddressBook")
        self.tableWidget = QTableWidget(self.groupBoxAddressBook)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 8):
            self.tableWidget.setRowCount(8)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)

        self.horizontalLayoutAddressBook.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.groupBoxAddressBook)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayoutButtons = QVBoxLayout()
        self.verticalLayoutButtons.setObjectName(u"verticalLayoutButtons")
        self.groupBoxActions = QGroupBox(address_book)
        self.groupBoxActions.setObjectName(u"groupBoxActions")
        self.groupBoxActions.setStyleSheet(u"\n"
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
"                border: 1px solid #45a049;\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                background-color: #3e8e41;\n"
"            }\n"
"        ")
        self.horizontalLayoutActions = QHBoxLayout(self.groupBoxActions)
        self.horizontalLayoutActions.setObjectName(u"horizontalLayoutActions")
        self.btn_addAddress = QPushButton(self.groupBoxActions)
        self.btn_addAddress.setObjectName(u"btn_addAddress")
        self.btn_addAddress.setStyleSheet(u"")

        self.horizontalLayoutActions.addWidget(self.btn_addAddress)

        self.btn_modify = QPushButton(self.groupBoxActions)
        self.btn_modify.setObjectName(u"btn_modify")

        self.horizontalLayoutActions.addWidget(self.btn_modify)

        self.btn_delete = QPushButton(self.groupBoxActions)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayoutActions.addWidget(self.btn_delete)


        self.verticalLayoutButtons.addWidget(self.groupBoxActions)

        self.horizontalLayoutAddButton = QHBoxLayout()
        self.horizontalLayoutAddButton.setObjectName(u"horizontalLayoutAddButton")

        self.verticalLayoutButtons.addLayout(self.horizontalLayoutAddButton)


        self.verticalLayout.addLayout(self.verticalLayoutButtons)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(address_book)

        QMetaObject.connectSlotsByName(address_book)
    # setupUi

    def retranslateUi(self, address_book):
        address_book.setWindowTitle(QCoreApplication.translate("address_book", u"\u5730\u5740\u7c3f", None))
        self.groupBoxAddressBook.setTitle(QCoreApplication.translate("address_book", u"\u5730\u5740\u7c3f\u5217\u8868", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("address_book", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("address_book", u"\u59d3\u540d", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("address_book", u"\u7535\u8bdd", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("address_book", u"\u7701\u4efd", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("address_book", u"\u5730\u7ea7\u5e02", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("address_book", u"\u8be6\u7ec6\u5730\u5740", None));
        self.groupBoxActions.setTitle(QCoreApplication.translate("address_book", u"\u7528\u6237\u64cd\u4f5c", None))
        self.btn_addAddress.setText(QCoreApplication.translate("address_book", u"\u6dfb\u52a0\u5730\u5740\u7c3f\u4fe1\u606f", None))
        self.btn_modify.setText(QCoreApplication.translate("address_book", u"\u4fee\u6539", None))
        self.btn_delete.setText(QCoreApplication.translate("address_book", u"\u5220\u9664", None))
    # retranslateUi

