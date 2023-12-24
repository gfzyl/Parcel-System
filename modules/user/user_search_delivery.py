# 导入sys
import sys

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
# 导入我们生成的界面
from user_search_delivery_ui import Ui_user_search_delivery
from qt_material import apply_stylesheet

 # 继承QWidget类，以获取其属性和方法
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_user_search_delivery()
        self.ui.setupUi(self)

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = MyWidget()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.setWindowOpacity(0.95); 
    window.show()
    
    # 结束QApplication
    app.exec_()
