# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guest_main.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_guest_main(object):
    def setupUi(self, guest_main):
        if not guest_main.objectName():
            guest_main.setObjectName(u"guest_main")
        guest_main.resize(519, 515)
        self.groupBox = QGroupBox(guest_main)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 501, 171))
        self.groupBox.setStyleSheet(u"\n"
"            QLabel {\n"
"                color: #333;\n"
"                font: 14px \"\u5e7c\u5706\";\n"
"                font-weight: bold;\n"
"            }\n"
"\n"
"            QLineEdit,\n"
"            QComboBox {\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 4px;\n"
"            }\n"
"\n"
"        ")
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 431, 134))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.nameInput1 = QLineEdit(self.layoutWidget)
        self.nameInput1.setObjectName(u"nameInput1")

        self.horizontalLayout.addWidget(self.nameInput1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.telInput1 = QLineEdit(self.layoutWidget)
        self.telInput1.setObjectName(u"telInput1")

        self.horizontalLayout.addWidget(self.telInput1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.prvComboBox1 = QComboBox(self.layoutWidget)
        self.prvComboBox1.addItem("")
        self.prvComboBox1.setObjectName(u"prvComboBox1")

        self.horizontalLayout_2.addWidget(self.prvComboBox1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_5)

        self.cityComboBox1 = QComboBox(self.layoutWidget)
        self.cityComboBox1.setObjectName(u"cityComboBox1")

        self.horizontalLayout_2.addWidget(self.cityComboBox1)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.placeInput1 = QLineEdit(self.layoutWidget)
        self.placeInput1.setObjectName(u"placeInput1")

        self.horizontalLayout_3.addWidget(self.placeInput1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox_2 = QGroupBox(guest_main)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 190, 501, 191))
        self.groupBox_2.setStyleSheet(u"\n"
"            QLabel {\n"
"                color: #333;\n"
"                font: 14px \"\u5e7c\u5706\";\n"
"                font-weight: bold;\n"
"            }\n"
"\n"
"            QLineEdit,\n"
"            QComboBox {\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 4px;\n"
"            }\n"
"        ")
        self.layoutWidget_2 = QWidget(self.groupBox_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 40, 431, 134))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.nameInput2 = QLineEdit(self.layoutWidget_2)
        self.nameInput2.setObjectName(u"nameInput2")

        self.horizontalLayout_4.addWidget(self.nameInput2)

        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.telInput2 = QLineEdit(self.layoutWidget_2)
        self.telInput2.setObjectName(u"telInput2")

        self.horizontalLayout_4.addWidget(self.telInput2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.label_8)

        self.prvComboBox2 = QComboBox(self.layoutWidget_2)
        self.prvComboBox2.addItem("")
        self.prvComboBox2.setObjectName(u"prvComboBox2")

        self.horizontalLayout_5.addWidget(self.prvComboBox2)

        self.label_9 = QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.label_9)

        self.cityComboBox2 = QComboBox(self.layoutWidget_2)
        self.cityComboBox2.setObjectName(u"cityComboBox2")

        self.horizontalLayout_5.addWidget(self.cityComboBox2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.placeInput2 = QLineEdit(self.layoutWidget_2)
        self.placeInput2.setObjectName(u"placeInput2")

        self.horizontalLayout_6.addWidget(self.placeInput2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.layoutWidget_3 = QWidget(guest_main)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(30, 390, 431, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"    color: #333;\n"
"    font: 14px \"\u5e7c\u5706\";\n"
"    font-weight: bold;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.notesInput = QLineEdit(self.layoutWidget_3)
        self.notesInput.setObjectName(u"notesInput")
        self.notesInput.setStyleSheet(u"  QLineEdit {\n"
"                padding: 8px;\n"
"                font-size: 14px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 4px;\n"
"            }")

        self.horizontalLayout_7.addWidget(self.notesInput)

        self.layoutWidget1 = QWidget(guest_main)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 450, 480, 39))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.searchBtn = QPushButton(self.layoutWidget1)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setStyleSheet(u"\n"
"             QPushButton {\n"
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
"        ")

        self.horizontalLayout_8.addWidget(self.searchBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.submitBtn = QPushButton(self.layoutWidget1)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setStyleSheet(u"\n"
"             QPushButton {\n"
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
"        ")

        self.horizontalLayout_8.addWidget(self.submitBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.quitBtn = QPushButton(self.layoutWidget1)
        self.quitBtn.setObjectName(u"quitBtn")
        self.quitBtn.setStyleSheet(u"\n"
"             QPushButton {\n"
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
"        ")

        self.horizontalLayout_8.addWidget(self.quitBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.retranslateUi(guest_main)

        QMetaObject.connectSlotsByName(guest_main)
    # setupUi

    def retranslateUi(self, guest_main):
        guest_main.setWindowTitle(QCoreApplication.translate("guest_main", u"\u6e38\u5ba2\u8fdb\u5165", None))
        self.groupBox.setTitle(QCoreApplication.translate("guest_main", u"\u5bc4\u4ef6\u4eba\u5730\u5740\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("guest_main", u"\u5bc4\u4ef6\u4eba\u59d3\u540d", None))
        self.label_2.setText(QCoreApplication.translate("guest_main", u"\u5bc4\u4ef6\u4eba\u7535\u8bdd", None))
        self.label_4.setText(QCoreApplication.translate("guest_main", u"\u7701", None))
        self.prvComboBox1.setItemText(0, "")

        self.label_5.setText(QCoreApplication.translate("guest_main", u"\u5e02", None))
        self.label_6.setText(QCoreApplication.translate("guest_main", u"\u8be6\u7ec6\u5730\u5740", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("guest_main", u"\u6536\u4ef6\u4eba\u5730\u5740\u4fe1\u606f", None))
        self.label_3.setText(QCoreApplication.translate("guest_main", u"\u6536\u4ef6\u4eba\u59d3\u540d", None))
        self.label_7.setText(QCoreApplication.translate("guest_main", u"\u6536\u4ef6\u4eba\u7535\u8bdd", None))
        self.label_8.setText(QCoreApplication.translate("guest_main", u"\u7701", None))
        self.prvComboBox2.setItemText(0, "")

        self.label_9.setText(QCoreApplication.translate("guest_main", u"\u5e02", None))
        self.label_10.setText(QCoreApplication.translate("guest_main", u"\u8be6\u7ec6\u5730\u5740", None))
        self.label_11.setText(QCoreApplication.translate("guest_main", u"\u5907\u6ce8:", None))
        self.searchBtn.setText(QCoreApplication.translate("guest_main", u"\u67e5\u8be2\u8ba2\u5355", None))
        self.submitBtn.setText(QCoreApplication.translate("guest_main", u"\u63d0\u4ea4\u8ba2\u5355", None))
        self.quitBtn.setText(QCoreApplication.translate("guest_main", u"\u8fd4\u56de\u767b\u5f55", None))
    # retranslateUi

