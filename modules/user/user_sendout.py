from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QIcon
from ...controller.sql import Sql

from .user_sendout_ui import Ui_user_sendout
from qt_material import apply_stylesheet

 # 继承QWidget类，以获取其属性和方法
class UserSendoutWindow(QWidget, Ui_user_sendout):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()
        statement1 = "SELECT prv_name FROM province"
        result_comboBox1 = self.sql.execute_query(statement1)
        result_list1 = [item[0] for item in result_comboBox1]     # 格式不对，需要转换
        self.comboBox_province1.addItems(result_list1)
        self.comboBox_province2.addItems(result_list1)
        self.comboBox_province1.currentTextChanged.connect(self.change_1)
        self.comboBox_province2.currentTextChanged.connect(self.change_2)
        # 寄快递


        statement2 = "SELECT * FROM address_book"
        result_comboBox2 = self.sql.execute_query(statement2)
        result_list2=[]
        for items in  result_comboBox2:
            result_list2.append('-'.join(items[1:]))    #去除地址簿id,把其他元组元素链接为字符串，然后添加入列表

        self.comboBox_addressBook1.addItems(result_list2)
        self.comboBox_addressBook2.addItems(result_list2)
        self.comboBox_addressBook1.currentTextChanged.connect(self.addDate_1)
        self.comboBox_addressBook2.currentTextChanged.connect(self.addDate_2)

        # 按键
        self.submitBtn.clicked.connect(self.bind)
        self.returnBtn.clicked.connect(self.back)


    def back(self):
            self.close()


    def change_1(self):
            result = self.comboBox_province1.currentText()
            statement = f"SELECT city_name FROM city, province WHERE city.prv_id = province.prv_id AND province.prv_name ='{result}'"
            result_comboBox = self.sql.execute_query(statement)
            result_list = [item[0] for item in result_comboBox]
            self.comboBox_city1.clear()
            self.comboBox_city1.addItems(result_list)

    def change_2(self):
            result = self.comboBox_province2.currentText()
            statement = f"SELECT city_name FROM city, province WHERE city.prv_id = province.prv_id AND province.prv_name ='{result}'"
            result_comboBox = self.sql.execute_query(statement)
            result_list = [item[0] for item in result_comboBox]
            self.comboBox_city2.clear()
            self.comboBox_city2.addItems(result_list)


    def addDate_1(self):
        str = self.comboBox_addressBook1.currentText()
        list = str.split('-')
        self.lineEdit_name1.setText(list[0])
        self.lineEdit_phone1.setText(list[1])
        self.comboBox_province1.setCurrentText(list[2])
        self.comboBox_city1.setCurrentText(list[3])
        self.lineEdit_address1.setText(list[4])


    def addDate_2(self):
        str = self.comboBox_addressBook2.currentText()
        list = str.split('-')
        self.lineEdit_name2.setText(list[0])
        self.lineEdit_phone2.setText(list[1])
        self.comboBox_province2.setCurrentText(list[2])
        self.comboBox_city2.setCurrentText(list[3])
        self.lineEdit_address2.setText(list[4])


    def bind(self): # 写入数据库

            result_name1 = self.lineEdit_name1.text()
            result_phone1 = self.lineEdit_phone1.text()
            result_province1 = self.comboBox_province1.currentText()
            result_city1 =self.comboBox_city1.currentText()
            result_address1 = self.lineEdit_address1.text()
            result_name2 = self.lineEdit_name2.text()
            result_phone2 = self.lineEdit_phone2.text()
            result_province2 = self.comboBox_province2.currentText()
            result_city2 = self.comboBox_city2.currentText()
            result_address2 = self.lineEdit_address2.text()
            result_extra = self.lineEdit_extra.text()

            statement = "INSERT INTO parcel_info(sender, sender_tel, sender_prv,sender_city,sender_place,recipient, recipient_tel, recipient_prv,recipient_city,recipient_place,notes) VALUES (%s, %s, %s,%s,%s,%s, %s, %s,%s,%s,%s)"

            values = (
            result_name1, result_phone1, result_province1, result_city1, result_address1, result_name2, result_phone2,
            result_province2, result_city2, result_address2, result_extra)

            self.sql.execute_insert(statement, values)
            QMessageBox.information(self, "恭喜", "寄件成功！", QMessageBox.Ok)
           


# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = UserSendoutWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.setWindowOpacity(0.95); 
    window.show()
    
    # 结束QApplication
    app.exec_()
