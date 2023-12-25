# 导入sys
import sys

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
from ...controller.sql import Sql
# 导入我们生成的界面
from .guest_main_ui import Ui_guest_main
from qt_material import apply_stylesheet

 # 继承QWidget类，以获取其属性和方法
class GuestMainWindow(QWidget,Ui_guest_main):
    logout_signal = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sql=Sql()
        self.sql.connect()
        statement = "SELECT prv_name FROM province"
        result_comboBox = self.sql.execute_query(statement)
        print(result_comboBox)                         #格式不对，需要转换
        result_list = [item[0] for item in result_comboBox]
        print(result_list)

        self.prvComboBox1.addItems(result_list )
        self.prvComboBox2.addItems(result_list )

        self.prvComboBox1.currentTextChanged.connect(self.change_1)
        self.prvComboBox2.currentTextChanged.connect(self.change_2)
        self.submitBtn.clicked.connect(self.bind)
        self.quitBtn.clicked.connect(self.goto_logout)

    
    def change_1(self):
        result=self.prvComboBox1.currentText()
        statement = f"SELECT city_name FROM city, province WHERE city.prv_id = province.prv_id AND province.prv_name ='{result}'"
        result_comboBox = self.sql.execute_query(statement)
        result_list = [item[0] for item in result_comboBox]
        self.cityComboBox1.clear()
        self.cityComboBox1.addItems(result_list)


    def change_2(self):
        result= self.prvComboBox2.currentText()
        statement = f"SELECT city_name FROM city, province WHERE city.prv_id = province.prv_id AND province.prv_name ='{result}'"
        result_comboBox = self.sql.execute_query(statement)
        result_list = [item[0] for item in result_comboBox]
        self.cityComboBox2.clear()
        self.cityComboBox2.addItems(result_list)


    def bind(self):
        result_name1 = self.nameInput1.text()
        result_phone1 = self.telInput1.text()
        result_province1=self.prvComboBox1.currentText()
        result_city1 = self.cityComboBox1.currentText()
        result_address1 = self.placeInput1.text()

        result_name2 = self.nameInput2.text()
        result_phone2 = self.telInput2.text()
        result_province2 = self.prvComboBox2.currentText()
        result_city2 = self.cityComboBox2.currentText()
        result_address2 = self.placeInput2.text()
        result_extra = self.notesInput.text()
        print(result_name1,result_phone1 ,result_province1,result_city1,result_address1,result_name2, result_phone2, result_province2, result_city2, result_address2,result_extra)

        statement= "INSERT INTO parcel_info(sender, sender_tel, sender_prv,sender_city,sender_place,recipient, recipient_tel, recipient_prv,recipient_city,recipient_place,notes) VALUES (%s, %s, %s,%s,%s,%s, %s, %s,%s,%s,%s)"
        values = (result_name1,result_phone1 ,result_province1,result_city1,result_address1,result_name2, result_phone2, result_province2, result_city2, result_address2,result_extra)
        self.sql.execute_insert(statement, values)

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = GuestMainWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.setWindowOpacity(0.95); 
    window.show()
    
    # 结束QApplication
    app.exec_()
