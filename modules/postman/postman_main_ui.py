# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'postman_main.ui'
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

class Ui_postman_main(object):
    def setupUi(self, postman_main):
        if not postman_main.objectName():
            postman_main.setObjectName(u"postman_main")
        postman_main.resize(761, 442)
        self.verticalLayout = QVBoxLayout(postman_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxAddressBook = QGroupBox(postman_main)
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
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 8):
            self.tableWidget.setRowCount(8)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem14)
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
        self.groupBoxActions = QGroupBox(postman_main)
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
        self.searchBtn = QPushButton(self.groupBoxActions)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setStyleSheet(u"")

        self.horizontalLayoutActions.addWidget(self.searchBtn)

        self.addCodeBtn = QPushButton(self.groupBoxActions)
        self.addCodeBtn.setObjectName(u"addCodeBtn")

        self.horizontalLayoutActions.addWidget(self.addCodeBtn)

        self.quitBtn = QPushButton(self.groupBoxActions)
        self.quitBtn.setObjectName(u"quitBtn")

        self.horizontalLayoutActions.addWidget(self.quitBtn)


        self.verticalLayoutButtons.addWidget(self.groupBoxActions)

        self.horizontalLayoutAddButton = QHBoxLayout()
        self.horizontalLayoutAddButton.setObjectName(u"horizontalLayoutAddButton")

        self.verticalLayoutButtons.addLayout(self.horizontalLayoutAddButton)


        self.verticalLayout.addLayout(self.verticalLayoutButtons)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(postman_main)

        QMetaObject.connectSlotsByName(postman_main)
    # setupUi

    def retranslateUi(self, postman_main):
        postman_main.setWindowTitle(QCoreApplication.translate("postman_main", u"\u5feb\u9012\u5458\u4e3b\u754c\u9762", None))
        self.groupBoxAddressBook.setTitle(QCoreApplication.translate("postman_main", u"\u5feb\u9012\u4fe1\u606f", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("postman_main", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("postman_main", u"\u8ba2\u5355\u7f16\u53f7", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("postman_main", u"\u5b8c\u6574\u8def\u7ebf", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("postman_main", u"\u7701\u4efd", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("postman_main", u"\u5730\u7ea7\u5e02", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("postman_main", u"\u8be6\u7ec6\u5730\u5740", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("postman_main", u"\u76ee\u524d\u72b6\u6001", None));
        self.groupBoxActions.setTitle(QCoreApplication.translate("postman_main", u"\u7528\u6237\u64cd\u4f5c", None))
        self.searchBtn.setText(QCoreApplication.translate("postman_main", u"\u67e5\u8be2\u8ba2\u5355", None))
        self.addCodeBtn.setText(QCoreApplication.translate("postman_main", u"\u6dfb\u52a0\u53d6\u4ef6\u7801", None))
        self.quitBtn.setText(QCoreApplication.translate("postman_main", u"\u9000\u51fa\u767b\u5f55", None))
    # retranslateUi

