# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_main.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_admin_main(object):
    def setupUi(self, admin_main):
        if not admin_main.objectName():
            admin_main.setObjectName(u"admin_main")
        admin_main.resize(565, 306)
        admin_main.setStyleSheet(u"\n"
"            QLabel {\n"
"                color: #333;\n"
"                font:14px \"\u5e7c\u5706\";\n"
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
"            #btn_update,\n"
"            #btn_change_password,\n"
"            #btn_change_phone {\n"
"                font-size: 13px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #45a049;\n"
"                border: 1px solid #45a049;\n"
"            }\n"
""
                        "\n"
"        ")
        self.verticalLayout = QVBoxLayout(admin_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QGroupBox(admin_main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.btn_query_courier_info_2 = QPushButton(self.tabWidget)
        self.btn_query_courier_info_2.setObjectName(u"btn_query_courier_info_2")
        self.btn_query_courier_info_2.setGeometry(QRect(50, 120, 141, 41))
        self.btn_view_all_couriers_2 = QPushButton(self.tabWidget)
        self.btn_view_all_couriers_2.setObjectName(u"btn_view_all_couriers_2")
        self.btn_view_all_couriers_2.setGeometry(QRect(200, 120, 161, 41))
        self.btn_logout = QPushButton(self.tabWidget)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setGeometry(QRect(440, 10, 101, 51))
        self.btn_query_delivery_info = QPushButton(self.tabWidget)
        self.btn_query_delivery_info.setObjectName(u"btn_query_delivery_info")
        self.btn_query_delivery_info.setGeometry(QRect(50, 180, 141, 41))
        self.btn_view_all_couriers = QPushButton(self.tabWidget)
        self.btn_view_all_couriers.setObjectName(u"btn_view_all_couriers")
        self.btn_view_all_couriers.setGeometry(QRect(200, 60, 161, 41))
        self.btn_query_courier_info = QPushButton(self.tabWidget)
        self.btn_query_courier_info.setObjectName(u"btn_query_courier_info")
        self.btn_query_courier_info.setGeometry(QRect(50, 60, 141, 41))

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(admin_main)

        QMetaObject.connectSlotsByName(admin_main)
    # setupUi

    def retranslateUi(self, admin_main):
        admin_main.setWindowTitle(QCoreApplication.translate("admin_main", u"\u7ba1\u7406\u5458\u754c\u9762", None))
        self.tabWidget.setTitle(QCoreApplication.translate("admin_main", u"\u7ba1\u7406\u5458\u4e3b\u754c\u9762", None))
        self.btn_query_courier_info_2.setText(QCoreApplication.translate("admin_main", u"\u67e5\u8be2\u5feb\u9012\u5458\u4fe1\u606f", None))
        self.btn_view_all_couriers_2.setText(QCoreApplication.translate("admin_main", u"\u67e5\u770b\u6240\u6709\u5feb\u9012\u5458", None))
        self.btn_logout.setText(QCoreApplication.translate("admin_main", u"\u9000\u51fa\u767b\u5f55", None))
        self.btn_query_delivery_info.setText(QCoreApplication.translate("admin_main", u"\u67e5\u8be2\u5feb\u9012\u4fe1\u606f", None))
        self.btn_view_all_couriers.setText(QCoreApplication.translate("admin_main", u"\u67e5\u770b\u6240\u6709\u914d\u9001\u5458", None))
        self.btn_query_courier_info.setText(QCoreApplication.translate("admin_main", u"\u67e5\u8be2\u914d\u9001\u5458\u4fe1\u606f", None))
    # retranslateUi

