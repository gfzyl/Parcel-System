# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_search_deliveryman.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_admin_search_deliveryman(object):
    def setupUi(self, admin_search_deliveryman):
        if not admin_search_deliveryman.objectName():
            admin_search_deliveryman.setObjectName(u"admin_search_deliveryman")
        admin_search_deliveryman.resize(667, 462)
        admin_search_deliveryman.setStyleSheet(u"\n"
"                QLabel {\n"
"                    color: #333;\n"
"                    font: 14px \"\u5e7c\u5706\";\n"
"                    font-weight: bold;\n"
"                }\n"
"\n"
"                QLineEdit,\n"
"                QComboBox  {\n"
"                    padding: 8px;\n"
"                    font-size: 14px;\n"
"                    border: 1px solid #ccc;\n"
"                    border-radius: 4px;\n"
"                }\n"
"\n"
"                QTableWidget {\n"
"                    font: 14px \"\u5e7c\u5706\";\n"
"                    background-color: #cdefff;\n"
"                }\n"
"\n"
"                QTableWidget::item {\n"
"                    font: 14px \"\u5e7c\u5706\";\n"
"                }\n"
"\n"
"                QHeaderView {\n"
"                    font: bold 16px \"\u5e7c\u5706\";\n"
"                }\n"
"                \n"
"                QTableWidget::item:selected {\n"
"                    background-color: #a6a6a6;\n"
"                }\n"
"\n"
"                QTa"
                        "bleWidget QHeaderView::section {\n"
"                    background-color: #65a3ff;\n"
"                    color: white;\n"
"                    font-weight: bold;\n"
"                    font-size: 16px;\n"
"                    padding: 4px;\n"
"                }\n"
"\n"
"                QTableWidget::item {\n"
"                    padding: 10px;\n"
"                }\n"
"\n"
"                QPushButton {\n"
"                    padding: 8px 16px;\n"
"                    font-size: 15px;\n"
"                    font-weight: bold;\n"
"                    border: 1px solid #4CAF50;\n"
"                    border-radius: 4px;\n"
"                    color: #fff;\n"
"                    background-color: #4CAF50;\n"
"                }\n"
"\n"
"                 QPushButton:hover {\n"
"                    background-color: #45a049;\n"
"                    border: 1px solid #45a049;\n"
"                }\n"
"\n"
"                QTextEdit {\n"
"                    font-size: 14px;\n"
"                    border: 1"
                        "px solid #ccc;\n"
"                    border-radius: 4px;\n"
"                }\n"
"\n"
"                QScrollBar:vertical {\n"
"                    border: 1px solid #ccc;\n"
"                    background: #f0f0f0;\n"
"                    width: 10px;\n"
"                    margin: 0px 0px 0px 0px;\n"
"                }\n"
"\n"
"                QScrollBar::handle:vertical {\n"
"                    background: #4CAF50;\n"
"                    min-height: 20px;\n"
"                }\n"
"            ")
        self.groupBox = QGroupBox(admin_search_deliveryman)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 641, 441))
        self.tableWidget = QTableWidget(self.groupBox)
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
        if (self.tableWidget.rowCount() < 13):
            self.tableWidget.setRowCount(13)
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
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem19)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 90, 621, 341))
        self.tableWidget.verticalHeader().setVisible(False)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 40, 601, 40))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.input1_lineedit = QLineEdit(self.layoutWidget)
        self.input1_lineedit.setObjectName(u"input1_lineedit")

        self.horizontalLayout.addWidget(self.input1_lineedit)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.input2_lineedit = QLineEdit(self.layoutWidget)
        self.input2_lineedit.setObjectName(u"input2_lineedit")

        self.horizontalLayout.addWidget(self.input2_lineedit)

        self.btn_query = QPushButton(self.layoutWidget)
        self.btn_query.setObjectName(u"btn_query")

        self.horizontalLayout.addWidget(self.btn_query)


        self.retranslateUi(admin_search_deliveryman)

        QMetaObject.connectSlotsByName(admin_search_deliveryman)
    # setupUi

    def retranslateUi(self, admin_search_deliveryman):
        admin_search_deliveryman.setWindowTitle(QCoreApplication.translate("admin_search_deliveryman", u"\u67e5\u8be2\u914d\u9001\u5458\u4fe1\u606f", None))
        self.groupBox.setTitle(QCoreApplication.translate("admin_search_deliveryman", u"\u914d\u9001\u5458\u4fe1\u606f", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u5de5\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u59d3\u540d", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u7535\u8bdd", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u5e74\u9f84", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u5de5\u4f5c\u70b91", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u5de5\u4f5c\u70b92", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u5de5\u53f7\uff1a", None))
        self.input1_lineedit.setPlaceholderText(QCoreApplication.translate("admin_search_deliveryman", u"\u9009\u62e9\u6309\u5de5\u53f7\u67e5\u8be2", None))
        self.label_2.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u7535\u8bdd\u53f7\u7801\uff1a", None))
        self.input2_lineedit.setPlaceholderText(QCoreApplication.translate("admin_search_deliveryman", u"\u9009\u62e9\u6309\u7535\u8bdd\u53f7\u7801\u67e5\u8be2", None))
        self.btn_query.setText(QCoreApplication.translate("admin_search_deliveryman", u"\u67e5\u8be2", None))
    # retranslateUi

