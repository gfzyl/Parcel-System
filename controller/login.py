# 先导入要该页面
from ..modules.login.login_ui import Ui_login
from PySide6.QtWidgets import QApplication, QWidget
from qt_material import apply_stylesheet
from PySide6.QtGui import QIcon
from .sql import Sql  # 连接数据库


# 导入我们生成的界面
from ..modules.guest.guest_main import GuestMainWindow
from ..modules.user.user_main import UserMainWindow
from ..modules.deliveryman.deliveryman_main import DeliverymanMainWindow
from ..modules.postman.postman_main import PostmanMainWindow
from ..modules.register.register import RegisterWindow
from ..modules.admin.admin_main import AdminMainWindow

gg
class LoginWindow(QWidget,Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 判断身份进入不同界面
        self.loginBtn.clicked.connect(self.goto_vary_main)
        self.registerBtn.clicked.connect(self.goto_register)
        self.guestBtn.clicked.connect(self.goto_guest_main)
        
        # 以后就直接引入别的界面就可以
        self.user_main_window = UserMainWindow()
        self.admin_main_window = AdminMainWindow()
        self.guest_main_window = GuestMainWindow()
        self.deliveryman_main_window = DeliverymanMainWindow()
        self.postman_main_window = PostmanMainWindow()
        self.register_window = RegisterWindow()

        # 连接信号,每个界面都有返回登录的操作，最终将返回至登录界面
        self.admin_main_window.logout_signal.connect(self.show_login_window)
        self.guest_main_window.logout_signal.connect(self.show_login_window)
        # 2023-12-25 11:42 现在已经可以实现登录界面到其他页面的跳转


    def show_login_window(self):
        self.show()


    def goto_register(self):
        self.hide()
        self.register_window.show()


    def goto_guest_main(self):
        # 选择退出登录的时候该界面该隐藏
        self.hide()
        self.guest_main_window.show()


    def goto_vary_main(self):
    # 普通用户的账户是数字1开头，派送员的账户是数字2开头，快递员的账户是数字3开头，管理员的账户是数字4开头
        self.account = self.accountInput.text()
        self.pwd = self.pwdInput.text()

        # 假设你的数据库中有不同的表用于存储每种类型的用户信息
        if self.account.startswith('1'):  # 普通用户
            if self.query_user(self.account, self.pwd):
                self.user_main_window.show()

        elif self.account.startswith('2'):  # 派送员
            if self.query_user(self.account, self.pwd):
                self.deliveryman_main_window.show()

        elif self.account.startswith('3'):  # 快递员
            if self.query_user(self.account, self.pwd):
                self.postman_main_window.show()

        elif self.account.startswith('4'):  # 管理员
            if self.query_user(self.account, self.pwd):
                self.admin_main_window.show()

        else:
            print("无效的账号格式")

        self.close()


    def query_deliveryman(self, account, pwd):
        self.sql=Sql()
        self.sql.connect()
        statement = f"SELECT * FROM deliveryman WHERE delivery_id = {account} AND delivery_pwd = {pwd}"
        return self.sql.execute_query(statement=statement)


    def query_postman(self, account, pwd):
        self.sql=Sql()
        self.sql.connect()
        statement = f"SELECT * FROM postman WHERE post_id = {account} AND post_pwd = {pwd}"
        return self.sql.execute_query(statement=statement)

    
    def query_user(self, account, pwd):
        print(account, pwd)
        self.sql=Sql()
        self.sql.connect()
        statement = f"SELECT * FROM [user] WHERE user_id = {account} AND user_pwd = {pwd}"
        return self.sql.execute_query(statement=statement)
        

    def query_admin(self, account, pwd):
        self.sql=Sql()
        self.sql.connect()
        statement = f"SELECT * FROM [user] WHERE user_id = {account} AND user_pwd = {pwd}"
        result = self.sql.execute_query(statement=statement)
        if result and account.startswith('4'):
            return result



# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
    window = LoginWindow()
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);
    window.show()
    app.exec_()
    
