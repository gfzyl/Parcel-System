# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mySend.ui'
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

class Ui_mySend(object):
    def setupUi(self, mySend):
        if not mySend.objectName():
            mySend.setObjectName(u"mySend")
        mySend.resize(591, 535)
        mySend.setStyleSheet(u"\n"
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
        self.groupBox = QGroupBox(mySend)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 561, 511))
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
        if (self.tableWidget.rowCount() < 13):
            self.tableWidget.setRowCount(13)
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
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 70, 521, 421))
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(46)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(28)
        self.returnBtn = QPushButton(self.groupBox)
        self.returnBtn.setObjectName(u"returnBtn")
        self.returnBtn.setGeometry(QRect(430, 20, 111, 37))

        self.retranslateUi(mySend)

        QMetaObject.connectSlotsByName(mySend)
    # setupUi

    def retranslateUi(self, mySend):
        mySend.setWindowTitle(QCoreApplication.translate("mySend", u"\u6211\u5bc4\u7684", None))
        self.groupBox.setTitle(QCoreApplication.translate("mySend", u"\u5feb\u9012\u4fe1\u606f", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mySend", u"\u5feb\u9012\u5355\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mySend", u"\u5f53\u524d\u4f4d\u7f6e", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mySend", u"\u5f53\u524d\u72b6\u6001", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mySend", u"\u9884\u8ba1\u9001\u8fbe\u65f6\u95f4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mySend", u"\u5b8c\u6574\u8def\u7ebf", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("mySend", u"\u65b0\u5efa\u884c", None));
        self.returnBtn.setText(QCoreApplication.translate("mySend", u"\u8fd4\u56de\u4e0a\u4e00\u7ea7", None))
    # retranslateUi

