# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_search_delivery.ui'
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

class Ui_user_search_delivery(object):
    def setupUi(self, user_search_delivery):
        if not user_search_delivery.objectName():
            user_search_delivery.setObjectName(u"user_search_delivery")
        user_search_delivery.resize(1118, 585)
        user_search_delivery.setStyleSheet(u"\n"
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
        self.groupBox = QGroupBox(user_search_delivery)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 1091, 551))
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 15):
            self.tableWidget.setColumnCount(15)
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
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        if (self.tableWidget.rowCount() < 13):
            self.tableWidget.setRowCount(13)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem27)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 120, 1061, 421))
        self.tableWidget.verticalHeader().setVisible(False)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(480, 70, 601, 40))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.parcelIdLabel = QLabel(self.layoutWidget)
        self.parcelIdLabel.setObjectName(u"parcelIdLabel")

        self.horizontalLayout.addWidget(self.parcelIdLabel)

        self.parcelIdInput = QLineEdit(self.layoutWidget)
        self.parcelIdInput.setObjectName(u"parcelIdInput")

        self.horizontalLayout.addWidget(self.parcelIdInput)

        self.searchBtn = QPushButton(self.layoutWidget)
        self.searchBtn.setObjectName(u"searchBtn")

        self.horizontalLayout.addWidget(self.searchBtn)

        self.returnBtn = QPushButton(self.groupBox)
        self.returnBtn.setObjectName(u"returnBtn")
        self.returnBtn.setGeometry(QRect(970, 20, 111, 37))

        self.retranslateUi(user_search_delivery)

        QMetaObject.connectSlotsByName(user_search_delivery)
    # setupUi

    def retranslateUi(self, user_search_delivery):
        user_search_delivery.setWindowTitle(QCoreApplication.translate("user_search_delivery", u"\u67e5\u8be2\u5feb\u9012\u4fe1\u606f", None))
        self.groupBox.setTitle(QCoreApplication.translate("user_search_delivery", u"\u5feb\u9012\u4fe1\u606f", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("user_search_delivery", u"\u5feb\u9012\u5355\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("user_search_delivery", u"\u5bc4\u51fa\u7701", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("user_search_delivery", u"\u5bc4\u51fa\u5e02", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("user_search_delivery", u"\u5bc4\u51fa\u8be6\u7ec6\u5730\u5740", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("user_search_delivery", u"\u5bc4\u4ef6\u4eba\u59d3\u540d", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("user_search_delivery", u"\u5bc4\u4ef6\u4eba\u7535\u8bdd", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("user_search_delivery", u"\u6536\u4ef6\u7701", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("user_search_delivery", u"\u6536\u4ef6\u5e02", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("user_search_delivery", u"\u6536\u4ef6\u8be6\u7ec6\u5730\u5740", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("user_search_delivery", u"\u6536\u4ef6\u4eba\u59d3\u540d", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("user_search_delivery", u"\u6536\u4ef6\u4eba\u7535\u8bdd", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("user_search_delivery", u"\u5907\u6ce8", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("user_search_delivery", u"\u5f53\u524d\u4f4d\u7f6e", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("user_search_delivery", u"\u5f53\u524d\u72b6\u6001", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("user_search_delivery", u"\u9884\u8ba1\u9001\u8fbe\u65f6\u95f4", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem24 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem25 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem26 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem27 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("user_search_delivery", u"\u65b0\u5efa\u884c", None));
        self.parcelIdLabel.setText(QCoreApplication.translate("user_search_delivery", u"\u5feb\u9012\u5355\u53f7", None))
        self.parcelIdInput.setPlaceholderText(QCoreApplication.translate("user_search_delivery", u"\u5728\u6b64\u8f93\u5165\u6709\u6548\u5feb\u9012\u5355\u53f7", None))
        self.searchBtn.setText(QCoreApplication.translate("user_search_delivery", u"\u67e5\u8be2", None))
        self.returnBtn.setText(QCoreApplication.translate("user_search_delivery", u"\u8fd4\u56de\u4e0a\u4e00\u7ea7", None))
    # retranslateUi

