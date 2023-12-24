# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'postman_main_.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(590, 412)
        self.groupBox = QGroupBox(widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 551, 301))
        self.groupBox.setStyleSheet(u"\n"
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
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        if (self.tableWidget.rowCount() < 8):
            self.tableWidget.setRowCount(8)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 20, 521, 261))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.groupBox_2 = QGroupBox(widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 330, 551, 71))
        self.groupBox_2.setStyleSheet(u"\n"
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
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(209, 23, 131, 31))
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(400, 23, 110, 31))
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 23, 100, 31))

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u5feb\u9012\u5458\u754c\u9762", None))
        self.groupBox.setTitle(QCoreApplication.translate("widget", u"\u5feb\u9012\u4fe1\u606f", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("widget", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("widget", u"\u8ba2\u5355\u7f16\u53f7", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("widget", u"\u5b8c\u6574\u8def\u7ebf", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("widget", u"\u8be6\u7ec6\u5730\u5740", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("widget", u"\u76ee\u524d\u72b6\u6001", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("widget", u"\u7528\u6237\u64cd\u4f5c", None))
        self.pushButton.setText(QCoreApplication.translate("widget", u"\u6dfb\u52a0\u53d6\u4ef6\u7801", None))
        self.pushButton_3.setText(QCoreApplication.translate("widget", u"\u9000\u51fa\u767b\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("widget", u"\u67e5\u8be2\u8ba2\u5355", None))
    # retranslateUi

