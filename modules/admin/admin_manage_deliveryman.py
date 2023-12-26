# 导入sys
from ...controller.sql import Sql
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PySide6.QtGui import QIcon

from .admin_manage_deliveryman_ui import Ui_admin_manage_deliveryman
from qt_material import apply_stylesheet

class AdminManageDeliverymanWindow(QWidget, Ui_admin_manage_deliveryman):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 按键
        self.returnBtn.clicked.connect(self.back)
    
        
    
    def back(self):
        self.close()


if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
    window = AdminManageDeliverymanWindow()
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);
    window.show()
    app.exec_()
