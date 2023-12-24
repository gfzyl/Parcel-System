# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deliverman.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_deliverman(object):
    def setupUi(self, deliverman):
        if not deliverman.objectName():
            deliverman.setObjectName(u"deliverman")
        deliverman.resize(547, 504)
        self.groupBox = QGroupBox(deliverman)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 521, 481))
        self.groupBox.setStyleSheet(u"\n"
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
"            QTableWidget::item:selected {\n"
"                background-color: #a6a6a6;\n"
"            }\n"
"\n"
"            QTableWidget QHeaderView::section {\n"
"                background-color: #65a3ff;\n"
"                color: white;\n"
"                font-weight: bold;\n"
"                font-size: 16px;\n"
"                 padding: 2px;\n"
"            }\n"
"\n"
"            QTableWidget::item {\n"
"                padding: 10px;\n"
"            }\n"
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
"        ")
        self.quitBtn = QPushButton(self.groupBox)
        self.quitBtn.setObjectName(u"quitBtn")
        self.quitBtn.setGeometry(QRect(404, 20, 101, 31))
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 70, 421, 301))
        self.tableWidget.verticalHeader().setVisible(False)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 380, 421, 40))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.confirmBtn = QPushButton(self.groupBox)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setGeometry(QRect(150, 430, 101, 31))

        self.retranslateUi(deliverman)

        QMetaObject.connectSlotsByName(deliverman)
    # setupUi

    def retranslateUi(self, deliverman):
        deliverman.setWindowTitle(QCoreApplication.translate("deliverman", u"\u6d3e\u9001\u5458", None))
        self.groupBox.setTitle(QCoreApplication.translate("deliverman", u"\u5feb\u9012\u4fe1\u606f", None))
        self.quitBtn.setText(QCoreApplication.translate("deliverman", u"\u9000\u51fa\u767b\u5f55", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("deliverman", u"\u5feb\u9012\u5355\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("deliverman", u"\u5b8c\u6574\u7ebf\u8def", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("deliverman", u"\u5f53\u524d\u72b6\u6001", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("deliverman", u"\u9884\u8ba1\u9001\u8fbe\u65f6\u95f4", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("deliverman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("deliverman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("deliverman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("deliverman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("deliverman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("deliverman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("deliverman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("deliverman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("deliverman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("deliverman", u"\u65b0\u5efa\u884c", None));
        self.label.setText(QCoreApplication.translate("deliverman", u"\u5f53\u524d\u4f4d\u7f6e\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("deliverman", u"\u9009\u62e9\u6700\u65b0\u5230\u8fbe\u4f4d\u7f6e\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("deliverman", u"\u9014\u7ecf\u57ce\u5e021", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("deliverman", u"\u9014\u7ecf\u57ce\u5e022", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("deliverman", u"\u9014\u7ecf\u57ce\u5e023", None))

        self.confirmBtn.setText(QCoreApplication.translate("deliverman", u"\u786e\u8ba4\u66f4\u6539", None))
    # retranslateUi

