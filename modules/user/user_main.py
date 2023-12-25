from PySide6.QtWidgets import QApplication, QWidget,QTableWidgetItem
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
from ...controller.sql import Sql
class UserMainWindow(QWidget,Ui_user_main):
    logout_signal = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.queryBtn.clicked.connect(self.queryFun)
        self.sendBtn.clicked.connect(self.sendFun)
        self.myReceiveBtn.clicked.connect(self.myReceiveFun)
        self.mySendBtn.clicked.connect(self.mySendFun)
        self.modifyInfoBtn.clicked.connect(self.modifyInfoFun)
        self.logoutBtn.clicked.connect(self.logoutFun)

    def queryFun(self):
        self.queryWindow=Window1()
        self.queryWindow.show()


    def sendFun(self):
        self.sendWindow=Window2()
        self.sendWindow.show()

    def myReceiveFun(self):
        self.myReceiveWindow=Window3()
        self.myReceiveWindow.show()

    def mySendFun(self):
        self.mySendWindow=Window4()
        self.mySendWindow.show()

    def modifyInfoFun(self):
        self.modifyInfoWindow=Window5()
        self.modifyInfoWindow.show()

    def logoutFun(self):
        self.logout_signal.emit()
        self.close()


class Window1(QWidget,Ui_user_search_delivery):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()

        # 按键
        self.returnBtn.clicked.connect(self.back)
        self.searchBtn.clicked.connect(self.searchDelivery)

    def back(self):
        # 清除输入框的搜索条件，确保每次进来都是空的
        self.parcelIdInput.clear()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(12)  # 每次看到都有12个空列
        self.close()

    def searchDelivery(self):
        parcel_id = self.parcelIdInput.text()
        statement = f"SELECT * FROM parcel_info WHERE parcel_id = '{parcel_id}'"
        result = self.sql.execute_query(statement=statement)
        if result:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            # 获取表头信息，用于映射数据库字段和表格列
            header_labels = [self.tableWidget.horizontalHeaderItem(col).text() for col in
                             range(self.tableWidget.columnCount())]

            # 将查询结果填充到表格中
            for row_num, row_data in enumerate(result):
                self.tableWidget.insertRow(row_num)
                for col_num, col_label in enumerate(header_labels):
                    # 通过表头信息映射列表中的索引
                    col_data = row_data[col_num] if col_num < len(row_data) else ""
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget.setItem(row_num, col_num, item)
        else:
            # 处理没有查询结果的情况
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

class Window2(QWidget,Ui_user_sendout):
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
        print(result_comboBox2)  # 格式不对，需要转换
        result_list2=[]
        for items in  result_comboBox2:
            result_list2.append('-'.join(items[1:]))    #去除地址簿id,把其他元组元素链接为字符串，然后添加入列表

        print(result_list2)
        self.comboBox_addressBook1.addItems(result_list2)
        self.comboBox_addressBook2.addItems(result_list2)


        self.submitBtn.clicked.connect(self.bind)
        self.returnBtn.clicked.connect(self.goto_logout)

    def goto_logout(self):
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

    def bind(self):                      #写入数据库

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

            result_addressBook1 = self.comboBox_addressBook1.currentText()
            result_addressBook2 = self.comboBox_addressBook2.currentText()

            print(result_name1, result_phone1, result_province1, result_city1, result_address1, result_name2,
                  result_phone2, result_province2, result_city2, result_address2, result_extra)

            statement = "INSERT INTO parcel_info(sender, sender_tel, sender_prv,sender_city,sender_place,recipient, recipient_tel, recipient_prv,recipient_city,recipient_place,notes) VALUES (%s, %s, %s,%s,%s,%s, %s, %s,%s,%s,%s)"
            values = (
            result_name1, result_phone1, result_province1, result_city1, result_address1, result_name2, result_phone2,
            result_province2, result_city2, result_address2, result_extra)
            self.sql.execute_insert(statement, values)

class Window3(QWidget,Ui_myReceive):
    def __init__(self):
        super().__init__()
        # 我收到的
        self.setupUi(self)

class Window4(QWidget,Ui_mySend):
    def __init__(self):
        super().__init__()
        # 我寄的
        self.setupUi(self)

class Window5(QWidget,Ui_user_modify_info):
    def __init__(self):
        super().__init__()
        # 修改个人信息
        self.setupUi(self)

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = UserMainWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png")
    window.setWindowIcon(appIcon)

    window.show()

    # 结束QApplication
    app.exec_()
