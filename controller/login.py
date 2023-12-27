# 先导入要该页面
from ..modules.login.login_ui import Ui_login
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from qt_material import apply_stylesheet
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal # 发送给各界面信号，主要发送账号
from .sql import Sql  # 连接数据库


# 导入我们生成的界面
from ..modules.guest.guest_main import GuestMainWindow
from ..modules.user.user_main import UserMainWindow
from ..modules.deliveryman.deliveryman_main import DeliverymanMainWindow
from ..modules.postman.postman_main import PostmanMainWindow
from ..modules.register.register import RegisterWindow
from ..modules.admin.admin_main import AdminMainWindow


class LoginWindow(QWidget,Ui_login):
    # 专门为后续界面提供成功登录的账号
    login_signal = Signal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 判断身份进入不同界面,然后创建对象
        self.loginBtn.clicked.connect(self.goto_vary_main)
        self.registerBtn.clicked.connect(self.goto_register)
        self.guestBtn.clicked.connect(self.goto_guest_main)
        

    def show_login_window(self):
        self.show()


    def goto_register(self):
        self.hide()
        self.register_window = RegisterWindow()
        self.set_windowStyle(self.register_window)
        self.register_window.show()
        self.register_window.confirmSignal.connect(self.show_login_window)
        self.register_window.cancelSignal.connect(self.show_login_window)


    def goto_guest_main(self):
        # 选择退出登录的时候该界面该隐藏
        self.hide()
        self.guest_main_window = GuestMainWindow()
        self.set_windowStyle(self.guest_main_window)
        self.guest_main_window.show()
        self.guest_main_window.logout_signal.connect(self.show_login_window)


    def goto_vary_main(self):
        # 普通用户的账户是数字1开头，派送员的账户是数字2开头，快递员的账户是数字3开头，管理员的账户是数字4开头
        self.account = self.accountInput.text()
        self.pwd = self.pwdInput.text()

        if self.account.startswith('1'):  # 普通用户
            if self.query_user(self.account, self.pwd):
                self.user_main_window = UserMainWindow(login_window=self)
                self.login_signal.emit(self.account)# 发射登录信号
                self.set_windowStyle(self.user_main_window)
                self.hide()
                self.user_main_window.show()
                self.user_main_window.logout_signal.connect(self.show_login_window)
            else:
                QMessageBox.warning(self, "警告", "账号或密码输入错误，请重新输入！", QMessageBox.Ok)



        elif self.account.startswith('2'):  # 派送员
            if self.query_deliveryman(self.account, self.pwd):
                self.login_signal.emit(self.account)# 发射登录信号
                self.deliveryman_main_window = DeliverymanMainWindow(login_window=self)
                self.set_windowStyle(self.deliveryman_main_window)
                self.hide()
                self.deliveryman_main_window.show()
                self.deliveryman_main_window.logout_signal.connect(self.show_login_window)
            else:
                QMessageBox.warning(self, "警告", "账号或密码输入错误，请重新输入！", QMessageBox.Ok)


        elif self.account.startswith('3'):  # 快递员
            if self.query_postman(self.account, self.pwd):
                self.login_signal.emit(self.account)# 发射登录信号
                self.postman_main_window = PostmanMainWindow(login_window=self)
                self.set_windowStyle(self.postman_main_window)
                self.hide()
                self.postman_main_window.show()
                self.postman_main_window.logout_signal.connect(self.show_login_window)
            else:
                QMessageBox.warning(self, "警告", "账号或密码输入错误，请重新输入！", QMessageBox.Ok)


        elif self.account.startswith('4'):  # 管理员
            if self.query_admin(self.account, self.pwd):
                self.admin_main_window = AdminMainWindow()
                self.set_windowStyle(self.admin_main_window)
                self.hide()
                self.admin_main_window.show()
                self.admin_main_window.logout_signal.connect(self.show_login_window)
            else:
                QMessageBox.warning(self, "警告", "账号或密码输入错误，请重新输入！", QMessageBox.Ok)


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


             
    def set_windowStyle(self, window):
        # 设置窗口图标登样式
        window.setWindowIcon(QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png"))
        window.setWindowOpacity(0.95) 



# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
    login_window = LoginWindow()
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png")
    login_window.setWindowOpacity(0.95)
    login_window.setWindowIcon(appIcon)
    login_window.show()
    app.exec_()
    
