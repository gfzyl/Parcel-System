# 先导入要该页面
from ..modules.login.login_ui import Ui_login
from PySide6.QtWidgets import QApplication, QWidget
from qt_material import apply_stylesheet
from PySide6.QtGui import QIcon
from .sql import Sql  # 连接数据库


# 导入我们生成的界面
from ..modules.guest.guest_main_ui import Ui_guest_main
from ..modules.user.user_main_ui import Ui_user_main
from ..modules.admin.admin_main_ui import Ui_admin_main
from ..modules.deliveryman.deliveryman_main_ui import Ui_deliveryman_main
from ..modules.postman.postman_main_ui import Ui_postman_main
from ..modules.register.register_ui import Ui_register
from ..modules.admin.admin_main import AdminMainWindow


class LoginWindow(QWidget,Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 判断身份进入不同界面
        self.loginBtn.clicked.connect(self.goto_vary_main)
        self.registerBtn.clicked.connect(self.goto_register)
        self.guestBtn.clicked.connect(self.goto_guest_main)
        

        self.user_main_window = userWindow()
        #self.admin_main_window = adminWindow()
        # 以后就直接引入别的界面就可以
        self.admin_main_window = AdminMainWindow()
        self.guest_main_window = guestWindow()
        self.deliveryman_main_window = deliverymanWindow()
        self.postman_main_window = postmanWindow()
        self.register_window = registerWindow()

    def goto_register(self):
        self.hide()
        self.register_window.show()


    def goto_guest_main(self):
        # 选择退出登录的时候该界面该隐藏
        self.hide()
        self.guest_main_window.show()


    def goto_vary_main(self):
        self.hide()
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


class userWindow(QWidget,Ui_user_main):
    def __init__(self):
        super().__init__()
        # 管理员搜索派送员
        self.setupUi(self)

class adminWindow(QWidget,Ui_admin_main):
    def __init__(self):
        super().__init__()
        # 管理员管理派送员
        self.setupUi(self)

class guestWindow(QWidget,Ui_guest_main):
    def __init__(self):
        super().__init__()
        # 管理员搜索快递员
        self.setupUi(self)

class deliverymanWindow(QWidget,Ui_deliveryman_main):
    def __init__(self):
        super().__init__()
        # 管理员管理快递员
        self.setupUi(self)

class postmanWindow(QWidget,Ui_postman_main):
    def __init__(self):
        super().__init__()
        # 管理员搜索快递
        self.setupUi(self)

class registerWindow(QWidget,Ui_register):
    def __init__(self):
        super().__init__()
        # 返回登录界面
        self.setupUi(self)

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
    
