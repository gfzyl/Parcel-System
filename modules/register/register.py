# 导入sys
import sys

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget,QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
from ...controller.sql import Sql
# 导入我们生成的界面
from .register_ui import Ui_register
from qt_material import apply_stylesheet

 # 继承QWidget类，以获取其属性和方法
class RegisterWindow(QWidget,Ui_register):
    confirmSignal = Signal() # 表示确认注册
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.setupUi(self)
        
        # 按键
        self.registerBtn.clicked.connect(self.goto_logout)

    def goto_logout(self):
        # 选择注册成功的时候返回
        # 加入判定是否注册成功的逻辑
        self.confirmSignal.emit()
        self.close()
    
    def userRegister(self, account, pwd,confirmPwd):
        # 判定账户是否已存在
        self.account = self.accountInput.text()
        self.sql=Sql()
        self.sql.connect()
        statement = f"SELECT * FROM deliveryman WHERE delivery_id = {account} AND delivery_pwd = {pwd}"
        return self.sql.execute_query(statement=statement)

        # 判定两次密码是否一致
        self.pwd = self.pwdInput.text()
        self.confirmPwd = self.confirmPwdInput.text()
        
        
        

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = RegisterWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.setWindowOpacity(0.95); 
    window.show()
    
    # 结束QApplication
    app.exec_()
