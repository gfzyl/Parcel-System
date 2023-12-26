# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_manage_postman.ui'
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
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_admin_manage_postman(object):
    def setupUi(self, admin_manage_postman):
        if not admin_manage_postman.objectName():
            admin_manage_postman.setObjectName(u"admin_manage_postman")
        admin_manage_postman.resize(909, 748)
        admin_manage_postman.setStyleSheet(u"\n"
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
"                    padding: 2px;\n"
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
"                QPushButton:hover {\n"
"                    background-color: #45a049;\n"
"                    border: 1px solid #45a049;\n"
"                }\n"
"\n"
"                QTextEdit {\n"
"                    font-size: 14px;\n"
"                    border: 1p"
                        "x solid #ccc;\n"
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
        self.groupBox = QGroupBox(admin_manage_postman)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 881, 461))
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(130, 110, 621, 341))
        self.tableWidget.verticalHeader().setVisible(False)
        self.returnBtn = QPushButton(self.groupBox)
        self.returnBtn.setObjectName(u"returnBtn")
        self.returnBtn.setGeometry(QRect(750, 10, 121, 37))
        self.layoutWidget_4 = QWidget(self.groupBox)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(120, 60, 631, 40))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.workIdInput_3 = QLineEdit(self.layoutWidget_4)
        self.workIdInput_3.setObjectName(u"workIdInput_3")

        self.horizontalLayout_5.addWidget(self.workIdInput_3)

        self.label_11 = QLabel(self.layoutWidget_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.workCity_2 = QComboBox(self.layoutWidget_4)
        self.workCity_2.setObjectName(u"workCity_2")

        self.horizontalLayout_5.addWidget(self.workCity_2)

        self.searchBtn_2 = QPushButton(self.layoutWidget_4)
        self.searchBtn_2.setObjectName(u"searchBtn_2")

        self.horizontalLayout_5.addWidget(self.searchBtn_2)

        self.groupBox_2 = QGroupBox(admin_manage_postman)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 480, 881, 261))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 200, 751, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.createBtn = QPushButton(self.layoutWidget)
        self.createBtn.setObjectName(u"createBtn")

        self.horizontalLayout_4.addWidget(self.createBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.updBtn = QPushButton(self.layoutWidget)
        self.updBtn.setObjectName(u"updBtn")

        self.horizontalLayout_4.addWidget(self.updBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.delBtn = QPushButton(self.layoutWidget)
        self.delBtn.setObjectName(u"delBtn")

        self.horizontalLayout_4.addWidget(self.delBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.layoutWidget_2 = QWidget(self.groupBox_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(70, 30, 751, 40))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.workIdInput = QLineEdit(self.layoutWidget_2)
        self.workIdInput.setObjectName(u"workIdInput")

        self.horizontalLayout.addWidget(self.workIdInput)

        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.pwdInput = QLineEdit(self.layoutWidget_2)
        self.pwdInput.setObjectName(u"pwdInput")

        self.horizontalLayout.addWidget(self.pwdInput)

        self.layoutWidget_3 = QWidget(self.groupBox_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(70, 80, 751, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.nameInput = QLineEdit(self.layoutWidget_3)
        self.nameInput.setObjectName(u"nameInput")

        self.horizontalLayout_2.addWidget(self.nameInput)

        self.label_5 = QLabel(self.layoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.telInput = QLineEdit(self.layoutWidget_3)
        self.telInput.setObjectName(u"telInput")

        self.horizontalLayout_2.addWidget(self.telInput)

        self.label_6 = QLabel(self.layoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.ageInput = QLineEdit(self.layoutWidget_3)
        self.ageInput.setObjectName(u"ageInput")

        self.horizontalLayout_2.addWidget(self.ageInput)

        self.layoutWidget_5 = QWidget(self.groupBox_2)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(70, 140, 251, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.workCityInput1 = QLineEdit(self.layoutWidget_5)
        self.workCityInput1.setObjectName(u"workCityInput1")

        self.horizontalLayout_3.addWidget(self.workCityInput1)

        self.label_8 = QLabel(self.layoutWidget_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)


        self.retranslateUi(admin_manage_postman)

        QMetaObject.connectSlotsByName(admin_manage_postman)
    # setupUi

    def retranslateUi(self, admin_manage_postman):
        admin_manage_postman.setWindowTitle(QCoreApplication.translate("admin_manage_postman", u"\u7ba1\u7406\u5feb\u9012\u5458\u4fe1\u606f", None))
        self.groupBox.setTitle(QCoreApplication.translate("admin_manage_postman", u"\u5feb\u9012\u5458\u4fe1\u606f", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("admin_manage_postman", u"\u5de5\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("admin_manage_postman", u"\u5bc6\u7801", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("admin_manage_postman", u"\u59d3\u540d", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("admin_manage_postman", u"\u7535\u8bdd", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("admin_manage_postman", u"\u5e74\u9f84", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("admin_manage_postman", u"\u5de5\u4f5c\u70b9", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u884c", None));
        self.returnBtn.setText(QCoreApplication.translate("admin_manage_postman", u"\u8fd4\u56de\u4e0a\u4e00\u7ea7", None))
        self.label_10.setText(QCoreApplication.translate("admin_manage_postman", u"\u5de5\u53f7\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("admin_manage_postman", u"\u5de5\u4f5c\u70b9\uff1a", None))
        self.searchBtn_2.setText(QCoreApplication.translate("admin_manage_postman", u"\u67e5\u8be2", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("admin_manage_postman", u"\u9009\u62e9\u8868\u5355\u4e2d\u7684\u5458\u5de5\u4fe1\u606f\u5728\u4e0b\u65b9\u4fee\u6539", None))
        self.createBtn.setText(QCoreApplication.translate("admin_manage_postman", u"\u65b0\u5efa\u5458\u5de5\u4fe1\u606f", None))
        self.updBtn.setText(QCoreApplication.translate("admin_manage_postman", u"\u4fee\u6539\u5458\u5de5\u4fe1\u606f", None))
        self.delBtn.setText(QCoreApplication.translate("admin_manage_postman", u"\u5220\u9664\u5458\u5de5\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("admin_manage_postman", u"\u5de5\u53f7\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("admin_manage_postman", u"\u5bc6\u7801\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("admin_manage_postman", u"\u59d3\u540d\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("admin_manage_postman", u"\u7535\u8bdd\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("admin_manage_postman", u"\u5e74\u9f84\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("admin_manage_postman", u"\u5de5\u4f5c\u70b9\uff1a", None))
        self.label_8.setText("")
    # retranslateUi

