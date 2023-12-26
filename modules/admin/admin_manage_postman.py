from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PySide6.QtGui import QIcon
from ...controller.sql import Sql
from .admin_manage_postman_ui import Ui_admin_manage_postman
from qt_material import apply_stylesheet

 # 继承QWidget类，以获取其属性和方法
class AdminManagePostmanWindow(QWidget, Ui_admin_manage_postman):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 按键
        self.returnBtn.clicked.connect(self.back)


    def back(self):
        self.close()

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = AdminManagePostmanWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.show()
    
    # 结束QApplication
    app.exec_()
