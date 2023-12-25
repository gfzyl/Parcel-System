# 导入sys
import sys

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget, QTableWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
from ...controller.sql import Sql
# 导入我们生成的界面
from .deliveryman_main_ui import Ui_deliveryman_main
from qt_material import apply_stylesheet

 # 继承QWidget类，以获取其属性和方法
class DeliverymanMainWindow(QWidget, Ui_deliveryman_main):
    logout_signal = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 按键
        self.quitBtn.clicked.connect(self.goto_logout)

    
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
    window = DeliverymanMainWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.show()
    
    # 结束QApplication
    app.exec_()
