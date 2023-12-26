# 导入sys
import sys
import re # 输入账户设置一个正则表达式

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
from ...controller.sql import Sql
# 导入我们生成的界面
from .register_ui import Ui_register
from qt_material import apply_stylesheet


class RegisterWindow(QWidget, Ui_register):
    confirmSignal = Signal()  # 表示确认注册

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 按键
        self.registerBtn.clicked.connect(self.userRegister)


    def userRegister(self):
        # 判定账户是否已存在(注册只针对于user表)
        account = self.accountInput.text()
        pwd = self.pwdInput.text()
        confirm_pwd = self.confirmPwdInput.text()

        if not re.match(r'^1\d{7}$', account):
            QMessageBox.warning(self, "警告", "账号格式不正确，请输入以1开头的8位数字!", QMessageBox.Ok)
            return

        self.sql = Sql()
        self.sql.connect()

        statement = f"SELECT * FROM [user] WHERE user_id = {account}"
        result = self.sql.execute_query(statement=statement)

        if result:
            QMessageBox.warning(self, "警告", "账号已存在，请重新输入！", QMessageBox.Ok)
        else:
            if pwd == '' or confirm_pwd == '':
                QMessageBox.warning(self, "警告", "请输入密码！", QMessageBox.Ok)
            # 判定两次密码是否一致
            elif pwd != confirm_pwd:
                QMessageBox.warning(self, "警告", "两次密码输入不一致，请重新输入！", QMessageBox.Ok)
            else:
                # 将账号密码写入数据库中
                statement = f"INSERT INTO [user] VALUES ('{account}', '{pwd}')"
                self.sql.execute_insert(statement=statement,value=None)
                
                QMessageBox.information(self, "恭喜", "注册成功！返回登录界面！", QMessageBox.Ok)
                self.confirmSignal.emit()  # 发出确认信号
                self.close()


# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")

    # 初始化并展示我们的界面组件
    window = RegisterWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png")
    window.setWindowIcon(appIcon)

    window.setWindowOpacity(0.95)
    window.show()

    # 结束QApplication
    sys.exit(app.exec_())
