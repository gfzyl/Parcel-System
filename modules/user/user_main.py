from PySide6.QtWidgets import QApplication, QWidget
from qt_material import apply_stylesheet
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal

from .user_main_ui import Ui_user_main
from .mySend_ui import Ui_mySend
from .myReceive_ui import Ui_myReceive
from .add_address_book_ui import Ui_add_address_book
from .address_book_ui import Ui_address_book
from .user_modify_info_ui import Ui_user_modify_info
from .user_sendout_ui import Ui_user_sendout
from .user_search_delivery_ui import Ui_user_search_delivery

class UserMainWindow(QWidget,Ui_user_main):
    logout_signal = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.queryBtn.clicked.connect(self.queryFun)
        self.sendBtn.clicked.connect(self.sendFun)
        self.myReceiveBtn.clicked.connect(self.myReceiveFun)
        self.mySendBtn.clicked.connect(self.mySendFun)
        self.modifyInfoBtn.clicked.connect(self.modifyInfoFun)
        self.logoutBtn.clicked.connect(self.logoutFun)

    def queryFun(self):
        self.queryWindow=Window1()
        self.queryWindow.show()


    def sendFun(self):
        self.sendWindow=Window2()
        self.sendWindow.show()

    def myReceiveFun(self):
        self.myReceiveWindow=Window3()
        self.myReceiveWindow.show()

    def mySendFun(self):
        self.mySendWindow=Window4()
        self.mySendWindow.show()

    def modifyInfoFun(self):
        self.modifyInfoWindow=Window5()
        self.modifyInfoWindow.show()

    def logoutFun(self):
        self.logout_signal.emit()
        self.close()


class Window1(QWidget,Ui_user_search_delivery):
    def __init__(self):
        super().__init__()
        #查询快递
        self.setupUi(self)

class Window2(QWidget,Ui_user_sendout):
    def __init__(self):
        super().__init__()
        # 寄快递
        self.setupUi(self)

class Window3(QWidget,Ui_myReceive):
    def __init__(self):
        super().__init__()
        # 我收到的
        self.setupUi(self)

class Window4(QWidget,Ui_mySend):
    def __init__(self):
        super().__init__()
        # 我寄的
        self.setupUi(self)

class Window5(QWidget,Ui_user_modify_info):
    def __init__(self):
        super().__init__()
        # 修改个人信息
        self.setupUi(self)

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = UserMainWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.show()
    
    # 结束QApplication
    app.exec_()
