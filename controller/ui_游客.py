# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '游客.ui'
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
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(548, 503)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 481, 141))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 431, 111))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_name1 = QLabel(self.layoutWidget)
        self.label_name1.setObjectName(u"label_name1")

        self.horizontalLayout.addWidget(self.label_name1)

        self.lineEdit_11 = QLineEdit(self.layoutWidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout.addWidget(self.lineEdit_11)

        self.label_phone1 = QLabel(self.layoutWidget)
        self.label_phone1.setObjectName(u"label_phone1")

        self.horizontalLayout.addWidget(self.label_phone1)

        self.lineEdit_12 = QLineEdit(self.layoutWidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout.addWidget(self.lineEdit_12)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_province1 = QLabel(self.layoutWidget)
        self.label_province1.setObjectName(u"label_province1")
        self.label_province1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_province1)

        self.comboBox_11 = QComboBox(self.layoutWidget)
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setEditable(True)
        self.comboBox_11.setMaxVisibleItems(100)

        self.horizontalLayout_2.addWidget(self.comboBox_11)

        self.label_city1 = QLabel(self.layoutWidget)
        self.label_city1.setObjectName(u"label_city1")
        self.label_city1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_city1)

        self.comboBox_12 = QComboBox(self.layoutWidget)
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setEditable(True)
        self.comboBox_12.setMaxVisibleItems(100)

        self.horizontalLayout_2.addWidget(self.comboBox_12)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_address1 = QLabel(self.layoutWidget)
        self.label_address1.setObjectName(u"label_address1")

        self.horizontalLayout_3.addWidget(self.label_address1)

        self.lineEdit_13 = QLineEdit(self.layoutWidget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_3.addWidget(self.lineEdit_13)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 160, 481, 141))
        self.layoutWidget_2 = QWidget(self.groupBox_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 20, 431, 111))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_name2 = QLabel(self.layoutWidget_2)
        self.label_name2.setObjectName(u"label_name2")

        self.horizontalLayout_4.addWidget(self.label_name2)

        self.lineEdit_21 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.horizontalLayout_4.addWidget(self.lineEdit_21)

        self.label_phone2 = QLabel(self.layoutWidget_2)
        self.label_phone2.setObjectName(u"label_phone2")

        self.horizontalLayout_4.addWidget(self.label_phone2)

        self.lineEdit_22 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.horizontalLayout_4.addWidget(self.lineEdit_22)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_province2 = QLabel(self.layoutWidget_2)
        self.label_province2.setObjectName(u"label_province2")
        self.label_province2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.label_province2)

        self.comboBox_21 = QComboBox(self.layoutWidget_2)
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setEditable(True)
        self.comboBox_21.setMaxVisibleItems(100)

        self.horizontalLayout_5.addWidget(self.comboBox_21)

        self.label_city2 = QLabel(self.layoutWidget_2)
        self.label_city2.setObjectName(u"label_city2")
        self.label_city2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.label_city2)

        self.comboBox_22 = QComboBox(self.layoutWidget_2)
        self.comboBox_22.setObjectName(u"comboBox_22")
        self.comboBox_22.setEditable(True)
        self.comboBox_22.setMaxVisibleItems(100)

        self.horizontalLayout_5.addWidget(self.comboBox_22)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_address2 = QLabel(self.layoutWidget_2)
        self.label_address2.setObjectName(u"label_address2")

        self.horizontalLayout_6.addWidget(self.label_address2)

        self.lineEdit_23 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.horizontalLayout_6.addWidget(self.lineEdit_23)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.layoutWidget_3 = QWidget(Form)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 320, 481, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_extra = QLabel(self.layoutWidget_3)
        self.label_extra.setObjectName(u"label_extra")

        self.horizontalLayout_7.addWidget(self.label_extra)

        self.lineEdit_extra = QLineEdit(self.layoutWidget_3)
        self.lineEdit_extra.setObjectName(u"lineEdit_extra")

        self.horizontalLayout_7.addWidget(self.lineEdit_extra)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 400, 401, 26))
        self.horizontalLayout_8 = QHBoxLayout(self.widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_1 = QPushButton(self.widget)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.horizontalLayout_8.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_8.addWidget(self.pushButton_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5bc4\u4ef6\u4eba\u5730\u5740\u4fe1\u606f", None))
        self.label_name1.setText(QCoreApplication.translate("Form", u"\u5bc4\u4ef6\u4eba\u59d3\u540d", None))
        self.label_phone1.setText(QCoreApplication.translate("Form", u"\u5bc4\u4ef6\u4eba\u7535\u8bdd", None))
        self.label_province1.setText(QCoreApplication.translate("Form", u"\u7701", None))
        self.comboBox_11.setItemText(0, "")

#if QT_CONFIG(tooltip)
        self.comboBox_11.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_city1.setText(QCoreApplication.translate("Form", u"\u5e02", None))
        self.label_address1.setText(QCoreApplication.translate("Form", u"\u8be6\u7ec6\u5730\u5740", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u6536\u4ef6\u4eba\u5730\u5740\u4fe1\u606f", None))
        self.label_name2.setText(QCoreApplication.translate("Form", u"\u6536\u4ef6\u4eba\u59d3\u540d", None))
        self.label_phone2.setText(QCoreApplication.translate("Form", u"\u6536\u4ef6\u4eba\u7535\u8bdd", None))
        self.label_province2.setText(QCoreApplication.translate("Form", u"\u7701", None))
        self.comboBox_21.setItemText(0, "")

        self.label_city2.setText(QCoreApplication.translate("Form", u"\u5e02", None))
        self.label_address2.setText(QCoreApplication.translate("Form", u"\u8be6\u7ec6\u5730\u5740", None))
        self.label_extra.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4\u8ba2\u5355", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u8ba2\u5355", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u767b\u5f55", None))
    # retranslateUi

