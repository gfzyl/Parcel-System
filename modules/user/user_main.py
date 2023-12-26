from PySide6.QtWidgets import QApplication, QWidget
from qt_material import apply_stylesheet
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal


from .user_main_ui import Ui_user_main
from .user_search_delivery_ui import Ui_user_search_delivery
from .mySend_ui import Ui_mySend
from .myReceive_ui import Ui_myReceive
 # 继承QWidget类，以获取其属性和方法
class UserMainWindow(QWidget, Ui_user_main):
    def __init__(self, login_window):
        super().__init__()
        # 设置界面为我们生成的界面2
        self.setupUi(self)
         
         # 连接登录信号
        login_window.login_signal.connect(self.receive_login_info)

    def receive_login_info(self, account):
        print(f"当前登录账户ID: {account}, 身份:User")


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
