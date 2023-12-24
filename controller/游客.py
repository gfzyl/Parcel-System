from PySide6.QtWidgets import QApplication,QWidget
from ui_游客 import Ui_Form
from sql import Sql

class MyWindow(QWidget,Ui_Form):
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

        self.comboBox_11.addItems(result_list )
        self.comboBox_21.addItems(result_list )
        flag=1
        while(flag==1):
            self.comboBox_11.currentTextChanged.connect(self.change_1)
            self.comboBox_21.currentTextChanged.connect(self.change_2)
            if self.pushButton_1.clicked.connect(self.bind):
                flag=0

    def change_1(self):
        result=self.comboBox_11.currentText()
        statement = f"SELECT city_name FROM city, province WHERE city.prv_id=province.prv_id AND province.prv_name='{result}'"
        result_comboBox = self.sql.execute_query(statement)
        result_list = [item[0] for item in result_comboBox]
        self.comboBox_12.clear()
        self.comboBox_12.addItems(result_list)

    def change_2(self):
        result= self.comboBox_21.currentText()
        statement = f"SELECT city_name FROM city, province WHERE city.prv_id=province.prv_id AND province.prv_name='{result}'"
        result_comboBox = self.sql.execute_query(statement)
        result_list = [item[0] for item in result_comboBox]
        self.comboBox_22.clear()
        self.comboBox_22.addItems(result_list)

    def bind(self):
        result_name1 = self.lineEdit_11.text()
        result_phone1 = self.lineEdit_12.text()
        result_province1=self.comboBox_11.currentText()
        result_city1 = self.comboBox_12.currentText()
        result_address1 = self.lineEdit_13.text()

        result_name2 = self.lineEdit_21.text()
        result_phone2 = self.lineEdit_22.text()
        result_province2 = self.comboBox_21.currentText()
        result_city2 = self.comboBox_22.currentText()
        result_address2 = self.lineEdit_23.text()
        result_extra = self.lineEdit_extra.text()
        print(result_name1,result_phone1 ,result_province1,result_city1,result_address1,result_name2, result_phone2, result_province2, result_city2, result_address2,result_extra)

        statement= "INSERT INTO parcel_info(sender, sender_tel, sender_prv,sender_city,sender_place,recipient, recipient_tel, recipient_prv,recipient_city,recipient_place,notes) VALUES (%s, %s, %s,%s,%s,%s, %s, %s,%s,%s,%s)"
        values = (result_name1,result_phone1 ,result_province1,result_city1,result_address1,result_name2, result_phone2, result_province2, result_city2, result_address2,result_extra)
        self.sql.execute_insert(statement, values)

if __name__=='__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
