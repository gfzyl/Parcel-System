# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_modify_info.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ProfileForm(object):
    def setupUi(self, ProfileForm):
        if not ProfileForm.objectName():
            ProfileForm.setObjectName(u"ProfileForm")
        ProfileForm.resize(646, 415)
        ProfileForm.setStyleSheet(u"\n"
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
        self.verticalLayout = QVBoxLayout(ProfileForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QGroupBox(ProfileForm)
        self.tabWidget.setObjectName(u"tabWidget")
        self.gridLayout_2 = QGridLayout(self.tabWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.tabWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.tabWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.lineEdit = QLineEdit(self.tabWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 4, 1, 1, 1)

        self.btn_change_phone = QPushButton(self.tabWidget)
        self.btn_change_phone.setObjectName(u"btn_change_phone")

        self.gridLayout.addWidget(self.btn_change_phone, 5, 2, 1, 1)

        self.label_new_phone = QLabel(self.tabWidget)
        self.label_new_phone.setObjectName(u"label_new_phone")

        self.gridLayout.addWidget(self.label_new_phone, 5, 0, 1, 1)

        self.label_name = QLabel(self.tabWidget)
        self.label_name.setObjectName(u"label_name")

        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)

        self.btn_change_password = QPushButton(self.tabWidget)
        self.btn_change_password.setObjectName(u"btn_change_password")

        self.gridLayout.addWidget(self.btn_change_password, 3, 2, 1, 1)

        self.label_phone = QLabel(self.tabWidget)
        self.label_phone.setObjectName(u"label_phone")

        self.gridLayout.addWidget(self.label_phone, 1, 0, 1, 1)

        self.old_password_lineedit = QLineEdit(self.tabWidget)
        self.old_password_lineedit.setObjectName(u"old_password_lineedit")

        self.gridLayout.addWidget(self.old_password_lineedit, 2, 1, 1, 1)

        self.btn_update = QPushButton(self.tabWidget)
        self.btn_update.setObjectName(u"btn_update")

        self.gridLayout.addWidget(self.btn_update, 1, 2, 1, 1)

        self.label_old_password = QLabel(self.tabWidget)
        self.label_old_password.setObjectName(u"label_old_password")

        self.gridLayout.addWidget(self.label_old_password, 2, 0, 1, 1)

        self.new_phone_lineedit = QLineEdit(self.tabWidget)
        self.new_phone_lineedit.setObjectName(u"new_phone_lineedit")

        self.gridLayout.addWidget(self.new_phone_lineedit, 5, 1, 1, 1)

        self.name_lineedit = QLineEdit(self.tabWidget)
        self.name_lineedit.setObjectName(u"name_lineedit")
        self.name_lineedit.setAcceptDrops(True)
        self.name_lineedit.setReadOnly(True)

        self.gridLayout.addWidget(self.name_lineedit, 0, 1, 1, 1)

        self.new_password_lineedit = QLineEdit(self.tabWidget)
        self.new_password_lineedit.setObjectName(u"new_password_lineedit")

        self.gridLayout.addWidget(self.new_password_lineedit, 3, 1, 1, 1)

        self.label_new_password = QLabel(self.tabWidget)
        self.label_new_password.setObjectName(u"label_new_password")

        self.gridLayout.addWidget(self.label_new_password, 3, 0, 1, 1)

        self.phone_lineedit = QLineEdit(self.tabWidget)
        self.phone_lineedit.setObjectName(u"phone_lineedit")

        self.gridLayout.addWidget(self.phone_lineedit, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 5, 1, 1, 1)


        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(ProfileForm)

        QMetaObject.connectSlotsByName(ProfileForm)
    # setupUi

    def retranslateUi(self, ProfileForm):
        ProfileForm.setWindowTitle(QCoreApplication.translate("ProfileForm", u"\u4fee\u6539\u4e2a\u4eba\u4fe1\u606f", None))
        self.tabWidget.setTitle(QCoreApplication.translate("ProfileForm", u"\u4e2a\u4eba\u4fe1\u606f", None))
        self.pushButton.setText(QCoreApplication.translate("ProfileForm", u"\u70b9\u51fb\u67e5\u770b\u5730\u5740\u7c3f\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("ProfileForm", u"\u65e7\u624b\u673a\u53f7:", None))
        self.btn_change_phone.setText(QCoreApplication.translate("ProfileForm", u"\u4fee\u6539\u624b\u673a\u53f7", None))
        self.label_new_phone.setText(QCoreApplication.translate("ProfileForm", u"\u65b0\u624b\u673a\u53f7:", None))
        self.label_name.setText(QCoreApplication.translate("ProfileForm", u"\u59d3\u540d:", None))
        self.btn_change_password.setText(QCoreApplication.translate("ProfileForm", u"\u4fee\u6539\u5bc6\u7801", None))
        self.label_phone.setText(QCoreApplication.translate("ProfileForm", u"\u624b\u673a\u53f7:", None))
        self.btn_update.setText(QCoreApplication.translate("ProfileForm", u"\u4fee\u6539", None))
        self.label_old_password.setText(QCoreApplication.translate("ProfileForm", u"\u65e7\u5bc6\u7801:", None))
        self.label_new_password.setText(QCoreApplication.translate("ProfileForm", u"\u65b0\u5bc6\u7801:", None))
    # retranslateUi

