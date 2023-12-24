from PySide6.QtWidgets import QApplication, QWidget
from qt_material import apply_stylesheet
from PySide6.QtGui import QIcon

# 导入我们生成的界面
from .admin_main_ui import Ui_admin_main
from .admin_manage_deliveryman_ui import Ui_admin_manage_deliveryman
from .admin_search_deliveryman_ui import Ui_admin_search_deliveryman
from .admin_search_postman_ui import Ui_admin_search_postman
from .admin_manage_postman_ui import Ui_admin_manage_postman
from .admin_search_delivery_ui import Ui_admin_search_delivery
from ..login.login_ui import Ui_login
class MyWindow(QWidget,Ui_admin_main):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.setupUi(self)
        self.btn_query_courier_info.clicked.connect(self.goto_admin_search_deliveryman)
        self.btn_view_all_couriers.clicked.connect(self.goto_admin_manage_deliveryman)
        self.btn_query_courier_info_2.clicked.connect(self.goto_admin_search_postman)
        self.btn_view_all_couriers_2.clicked.connect(self.goto_admin_manage_postman)
        self.btn_query_delivery_info.clicked.connect(self.goto_admin_search_delivery)
        self.btn_logout.clicked.connect(self.goto_login)

        self.deliveryman_search_window = Window1()
        self.deliveryman_manage_window = Window2()
        self.postman_search_window = Window3()
        self.postman_manage_window = Window4()
        self.delivery_search_window = Window5()
        self.login_window = Window6()

    def goto_admin_search_deliveryman(self):
        self.deliveryman_search_window.show()

    def goto_admin_manage_deliveryman(self):
        self.deliveryman_manage_window.show()

    def goto_admin_search_postman(self):
        self.postman_search_window.show()

    def goto_admin_manage_postman(self):
        self.postman_manage_window.show()

    def goto_admin_search_delivery(self):
        self.delivery_search_window.show()

    def goto_login(self):
        self.login_window.show()


class Window1(QWidget,Ui_admin_search_deliveryman):
    def __init__(self):
        super().__init__()
        # 管理员搜索派送员
        self.setupUi(self)

class Window2(QWidget,Ui_admin_manage_deliveryman):
    def __init__(self):
        super().__init__()
        # 管理员管理派送员
        self.setupUi(self)

class Window3(QWidget,Ui_admin_search_postman):
    def __init__(self):
        super().__init__()
        # 管理员搜索快递员
        self.setupUi(self)

class Window4(QWidget,Ui_admin_manage_postman):
    def __init__(self):
        super().__init__()
        # 管理员管理快递员
        self.setupUi(self)

class Window5(QWidget,Ui_admin_search_delivery):
    def __init__(self):
        super().__init__()
        # 管理员搜索快递
        self.setupUi(self)

class Window6(QWidget,Ui_login):
    def __init__(self):
        super().__init__()
        # 返回登录界面
        self.setupUi(self)

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
    window = MyWindow()
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);
    window.show()
    app.exec_()
    
