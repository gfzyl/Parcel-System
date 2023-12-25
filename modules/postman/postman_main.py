# 导入sys
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
# 导入我们生成的界面
from .postman_main_ui import Ui_postman_main
from qt_material import apply_stylesheet


class PostmanMainWindow(QWidget, Ui_postman_main):
    logout_signal = Signal()
    def __init__(self, login_window):
        super().__init__()
        self.setupUi(self)
        
        # 按键
        self.quitBtn.clicked.connect(self.goto_logout)

        # 连接登录信号
        login_window.login_signal.connect(self.receive_login_info)

    def receive_login_info(self, account):
        print(f"当前登录账户ID: {account}")

    
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
    window = PostmanMainWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.setWindowOpacity(0.95); 
    window.show()
    
    # 结束QApplication
    app.exec_()
