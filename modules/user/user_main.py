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
class UserMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_user_main()
        self.ui.setupUi(self)

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
