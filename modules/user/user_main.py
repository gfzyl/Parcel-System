from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
from .user_main_ui import Ui_user_main
from .user_modify_info import UserModifyInfoWindow
from .user_search_delivery import UserSearchDeliveryWindow
from .user_sendout import UserSendoutWindow
from .myReceive import MyReceiveWindow
from .mySend import MySendWindow    

from qt_material import apply_stylesheet

 # 继承QWidget类，以获取其属性和方法
class UserMainWindow(QWidget, Ui_user_main):
    logout_signal = Signal()
    def __init__(self, login_window):
        super().__init__()
        self.setupUi(self)

        # 按键
        self.logoutBtn.clicked.connect(self.goto_logout)
        self.searchBtn.clicked.connect(self.goto_search_delivery)
        self.sendBtn.clicked.connect(self.goto_user_sendout)
        self.myReceiveBtn.clicked.connect(self.goto_myReceive)
        self.mySendBtn.clicked.connect(self.goto_myReceive)
        self.modifyInfoBtn.clicked.connect(self.goto_user_modify_info)

        # 信号
        login_window.login_signal.connect(self.receive_login_info)


    def receive_login_info(self, account):
        print(f"当前登录账户ID: {account}, 身份:User")
        self.account = account


    def goto_search_delivery(self):
        user_search_delivery_window = UserSearchDeliveryWindow()
        user_search_delivery_window.show()


    def goto_user_sendout(self):
        user_sendout_window = UserSendoutWindow()
        user_sendout_window.show()

    
    def goto_user_modify_info(self):
        user_modify_info_window = UserModifyInfoWindow()
        user_modify_info_window.show()


    def goto_myReceive(self):
        myReceive_window = MyReceiveWindow(user_main_window=self)
        myReceive_window.show()

    
    def goto_mySend(self):
        mySend_window = MySendWindow()
        mySend_window.show()


    def goto_logout(self):
        # 选择退出登录的时候触发信号
        self.logout_signal.emit()
        self.close()


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
