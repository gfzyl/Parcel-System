from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem,QMessageBox
from qt_material import apply_stylesheet
from datetime import datetime,timedelta
import  re

from .add_address_book_ui import Ui_add_address_book
from .address_book_ui import Ui_address_book
from .myReceive_ui import Ui_myReceive
from .mySend_ui import Ui_mySend
from .user_main_ui import Ui_user_main
from .user_modify_info_ui import Ui_user_modify_info
from .user_search_delivery_ui import Ui_user_search_delivery
from .user_sendout_ui import Ui_user_sendout
from ...controller.sql import Sql
from ...controller.routeMap import route

class UserMainWindow(QWidget,Ui_user_main):
    logout_signal = Signal()
    def __init__(self,loginWindow):
        super().__init__()
        self.setupUi(self)
        self.queryBtn.clicked.connect(self.queryFun)
        self.sendBtn.clicked.connect(self.sendFun)
        self.myReceiveBtn.clicked.connect(self.myReceiveFun)
        self.mySendBtn.clicked.connect(self.mySendFun)
        self.modifyInfoBtn.clicked.connect(self.modifyInfoFun)
        self.logoutBtn.clicked.connect(self.logoutFun)
        loginWindow.login_signal.connect(self.receiveAccount)


    def set_windowStyle(self, window):
        # 设置窗口图标登样式
        window.setWindowIcon(QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png"))
        window.setWindowOpacity(0.95) 


    def receiveAccount(self,account):
        self.account = account

    def queryFun(self):
        self.queryWindow=Window1()
        self.set_windowStyle(self.queryWindow)
        self.queryWindow.show()


    def sendFun(self):
        self.sendWindow=Window2(loginWindow=self)
        self.set_windowStyle(self.sendWindow)
        self.sendWindow.show()

    def myReceiveFun(self):
        self.myReceiveWindow=Window3(loginWindow=self)
        self.set_windowStyle(self.myReceiveWindow)
        self.myReceiveWindow.show()

    def mySendFun(self):
        self.mySendWindow=Window4(loginWindow=self)
        self.set_windowStyle(self.mySendWindow)
        self.mySendWindow.show()

    def modifyInfoFun(self):
        self.modifyInfoWindow=Window5(loginWindow=self)
        self.set_windowStyle(self.modifyInfoWindow)
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
        self.tableWidget.setRowCount(0)
        #self.tableWidget.setColumnWidth(0, 50)      #设置列宽
        self.tableWidget.setColumnWidth(3, 300)
        self.tableWidget.setColumnWidth(8, 300)

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

            # 将查询结果填充到表格中
            for row_num, row_data in enumerate(result):
                print(row_data)
                self.tableWidget.insertRow(row_num)

                item1 = QTableWidgetItem(str(row_data[0]))
                self.tableWidget.setItem(row_num, 0, item1)
                item2 = QTableWidgetItem(str(row_data[3]))
                self.tableWidget.setItem(row_num, 1, item2)
                item3 = QTableWidgetItem(str(row_data[4]))
                self.tableWidget.setItem(row_num, 2, item3)
                item4 = QTableWidgetItem(str(row_data[5]))
                self.tableWidget.setItem(row_num, 3, item4)
                item5 = QTableWidgetItem(str(row_data[6]))
                self.tableWidget.setItem(row_num, 4, item5)
                item6 = QTableWidgetItem(str(row_data[7]))
                self.tableWidget.setItem(row_num, 5, item6)
                item7 = QTableWidgetItem(str(row_data[8]))
                self.tableWidget.setItem(row_num, 6, item7)
                item8 = QTableWidgetItem(str(row_data[9]))
                self.tableWidget.setItem(row_num, 7, item8)
                item9 = QTableWidgetItem(str(row_data[10]))
                self.tableWidget.setItem(row_num, 8, item9)
                item10 = QTableWidgetItem(str(row_data[11]))
                self.tableWidget.setItem(row_num, 9, item10)
                item11 = QTableWidgetItem(str(row_data[12]))
                self.tableWidget.setItem(row_num, 10, item11)
                item12 = QTableWidgetItem(str(row_data[13]))
                self.tableWidget.setItem(row_num, 11, item12)
                item13 = QTableWidgetItem(str(row_data[14]))
                self.tableWidget.setItem(row_num, 12, item13)
                item14 = QTableWidgetItem(str(row_data[15]))
                self.tableWidget.setItem(row_num, 13, item14)
                item15 = QTableWidgetItem(str(row_data[17]))
                self.tableWidget.setItem(row_num, 14, item15)

        else:
            # 处理没有查询结果的情况
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

class Window2(QWidget,Ui_user_sendout):
    def __init__(self,loginWindow):
        super().__init__()
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()
        self.account = loginWindow.account
        statement1 = "SELECT prv_name FROM province"
        result_comboBox1 = self.sql.execute_query(statement1)
        result_list1 = [item[0] for item in result_comboBox1]     # 格式不对，需要转换
        self.comboBox_province1.addItems(result_list1)
        self.comboBox_province2.addItems(result_list1)
        self.comboBox_province1.currentTextChanged.connect(self.change_1)
        self.comboBox_province2.currentTextChanged.connect(self.change_2)
        # 寄快递

        print('值为',self.account)
        statement2 = f"SELECT * FROM address_book WHERE user_id ={self.account}"
        result_comboBox2 = self.sql.execute_query(statement2)
        print(result_comboBox2)  # 格式不对，需要转换
        result_list2=[]
        if result_comboBox2:
            for items in  result_comboBox2:
                result_list2.append('-'.join(items[1:]))    #去除地址簿id,把其他元组元素链接为字符串，然后添加入列表

        print(result_list2)
        self.comboBox_addressBook1.addItems(result_list2)
        self.comboBox_addressBook2.addItems(result_list2)
        self.comboBox_addressBook1.currentTextChanged.connect(self.addDate_1)
        self.comboBox_addressBook2.currentTextChanged.connect(self.addDate_2)

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

            flag_1 =result_name1 and result_phone1 and result_province1 and result_city1 and result_address1
            flag_2 =result_name2 and result_phone2 and result_province2 and result_city2 and result_address2
            if flag_1 and flag_2:
                result_route = route(result_province1, result_province2)
                result_estiDay = int((len(result_route)+1)/2)
                result_status = '未送达'
                cur_date = datetime.now()
                reach_date = cur_date + timedelta(days=result_estiDay)   #预计送达日期
                result_date = str(reach_date.year) +'-'+str(reach_date.month) + '-' +str(reach_date.day)

                statement = "INSERT INTO parcel_info(sender, sender_tel, sender_prv,sender_city,sender_place,recipient, recipient_tel, recipient_prv,recipient_city,recipient_place,notes,cur_place,status,estimated_time) VALUES (%s,%s, %s,%s,%s, %s,%s,%s,%s, %s, %s,%s,%s,%s)"
                values = (
                    result_name1, result_phone1, result_province1, result_city1, result_address1, result_name2,
                    result_phone2,
                    result_province2, result_city2, result_address2, result_extra,result_province1,result_status,result_date)
                self.sql.execute_insert(statement, values)
                QMessageBox.information(self, "恭喜", "提交订单成功！点击确认后将自动跳转到主界面", QMessageBox.Ok)
                self.close()
            else:
                QMessageBox.warning(self, "警告", "请填写完整新信息！", QMessageBox.Ok)

class Window3(QWidget,Ui_myReceive):
    def __init__(self,loginWindow):
        super().__init__()
        # 我收到的
        self.setupUi(self)
        self.sql = Sql()


        self.sql.connect()
        self.account = loginWindow.account
        self.insertData()

        self.tableWidget.setColumnWidth(4, 400)

        self.tableWidget.cellClicked.connect(self.cellClicked)
        self.confirmBtn.clicked.connect(self.confirmAct)
        self.refuseBtn.clicked.connect(self.refuseAct)
        self.returnBtn.clicked.connect(self.back)

    def insertData(self):

        # temp = LoginWindow()     #调用登陆时输入的账号
        #self.account = '120'  # 后面替换

        statement = f"SELECT * FROM parcel_info WHERE recipient_tel = '{self.account}'"
        result = self.sql.execute_query(statement)
        print(result)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)


        # 将查询结果填充到表格中
        for row_num, row_data in enumerate(result):
            print(row_data)
            self.tableWidget.insertRow(row_num)

            result = route(row_data[3], row_data[8])
            result_route = '->'.join(result)
            result_route =result_route + '->'+row_data[9]+'->'+row_data[10]
            print(result_route)

            item1 = QTableWidgetItem(str(row_data[0]))
            self.tableWidget.setItem(row_num, 0, item1)
            item2 = QTableWidgetItem(str(row_data[14]))
            self.tableWidget.setItem(row_num, 1, item2)
            item3 = QTableWidgetItem(str(row_data[15]))
            self.tableWidget.setItem(row_num, 2, item3)
            item4 = QTableWidgetItem(str(row_data[17]))
            self.tableWidget.setItem(row_num, 3, item4)
            item5 = QTableWidgetItem(str(result_route))
            self.tableWidget.setItem(row_num, 4, item5)

    def confirmAct(self):
        result_id = self.tableWidget.item(self.row, 0).text()
        statement = f"SELECT status FROM parcel_info WHERE parcel_id= '{result_id}' "
        result = self.sql.execute_query(statement)
        print('值为',result[0][0])
        if result[0][0]=='已送达':
            statement = f"UPDATE parcel_info SET status = '已签收' WHERE parcel_id= %s "
            value = (result_id,)       #单个元素加上逗号
            self.sql.execute_update(statement,value)
            QMessageBox.information(self, "成功", "你已签收！", QMessageBox.Ok)
            self.insertData()
        elif result[0][0]=='未送达':
            QMessageBox.warning(self, "警告", "快递未送达，暂时无法修改！", QMessageBox.Ok)

        else:
            QMessageBox.warning(self, "警告", "状态无法再次修改！请联系客服处理", QMessageBox.Ok)


    def cellClicked(self,row,column):
        self.row=row
        self.column=column
    def refuseAct(self):
        result_id = self.tableWidget.item(self.row, 0).text()
        statement = f"SELECT status FROM parcel_info WHERE parcel_id= '{result_id}' "
        result = self.sql.execute_query(statement)
        if result[0][0] == '已送达':
            statement = f"UPDATE parcel_info SET status = '已拒收' WHERE parcel_id= %s "
            value = (result_id,)  # 单个元素加上逗号
            self.sql.execute_update(statement, value)
            QMessageBox.information(self, "成功", "你已拒收！", QMessageBox.Ok)
        elif result[0][0] == '未送达':
            QMessageBox.warning(self, "警告", "快递未送达，暂时无法修改！", QMessageBox.Ok)

        else:
            QMessageBox.warning(self, "警告", "状态无法再次修改！请联系客服处理", QMessageBox.Ok)
    def back(self):
        # 清除输入框的搜索条件，确保每次进来都是空的
        self.close()

class Window4(QWidget,Ui_mySend):
    def __init__(self,loginWindow):
        super().__init__()
        # 我寄的
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()
        self.account=loginWindow.account

        self.tableWidget.setColumnWidth(4, 400)
        self.insertData()
        self.returnBtn.clicked.connect(self.back)

    def insertData(self):
        # temp = LoginWindow()     #调用登陆时输入的账号
        #self.account = '110'  # 后面替换

        statement = f"SELECT * FROM parcel_info WHERE sender_tel = '{self.account}'"
        result = self.sql.execute_query(statement)
        print(result)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        # 将查询结果填充到表格中
        for row_num, row_data in enumerate(result):
            print(row_data)
            self.tableWidget.insertRow(row_num)

            result = route(row_data[3], row_data[8])
            result_route = '->'.join(result)
            result_route = result_route + '->' + row_data[9] + '->' + row_data[10]
            print(result_route)

            item1 = QTableWidgetItem(str(row_data[0]))
            self.tableWidget.setItem(row_num, 0, item1)
            item2 = QTableWidgetItem(str(row_data[14]))
            self.tableWidget.setItem(row_num, 1, item2)
            item3 = QTableWidgetItem(str(row_data[15]))
            self.tableWidget.setItem(row_num, 2, item3)
            item4 = QTableWidgetItem(str(row_data[17]))
            self.tableWidget.setItem(row_num, 3, item4)
            item5 = QTableWidgetItem(str(result_route))
            self.tableWidget.setItem(row_num, 4, item5)



    def back(self):
        self.close()

class Window5(QWidget,Ui_user_modify_info):
    def __init__(self,loginWindow):
        super().__init__()
        # 修改个人信息
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()

        self.btn_changePassword.clicked.connect(self.changePassword)
        self.btn_changePhone.clicked.connect(self.changePhone)
        self.btn_viewAddressBook.clicked.connect(self.viewAddressBook)
        self.btn_return.clicked.connect(self.back)
        self.account =loginWindow.account

    def changePassword(self):
        result_oldPassword = self.lineEdit_oldPassword.text()
        result_newPassword = self.lineEdit_newPassword.text()
        result_againPassword = self.lineEdit_againPassword.text()

        statement = f"SELECT user_pwd FROM [user] WHERE user_id = {self.account}"
        result = self.sql.execute_query(statement)

        print('值为',self.account)
        print(result[0][0])   #从元组中获取密码
        if result_oldPassword==result[0][0]  :
                if  result_newPassword==result_againPassword and result_newPassword :
                    statement_modifyPassword = f"UPDATE [user] SET user_pwd = %s WHERE user_id= %s"
                    values =(result_newPassword,self.account)
                    self.sql.execute_update(statement_modifyPassword, values)
                    QMessageBox.information(self, "成功", "你已成功修改密码！", QMessageBox.Ok)

                else:
                    QMessageBox.warning(self, "警告", "新密码不一致，请重新检查！！", QMessageBox.Ok)
        if result_oldPassword!=result[0][0]:
            QMessageBox.warning(self, "警告", "旧密码错误！", QMessageBox.Ok)

    def changePhone(self):
        result_newPhone = self.lineEdit_newPhone.text()
        if re.match(r'^1\d{7}$',result_newPhone):
            statement = f"UPDATE [user] SET user_phone = %s WHERE user_id= %s"
            values = (result_newPhone, self.account)
            self.sql.execute_update(statement, values)
            QMessageBox.information(self, "成功", "你已成功修改手机号！", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "警告", "手机号格式错误！请输入以1开头的8位数字", QMessageBox.Ok)

    def viewAddressBook(self):
        self.window_viewAdress = Window_viewAddress(loginWindow=self)
        self.window_viewAdress.show()

    def back(self):
        self.close()

class Window_viewAddress(QWidget,Ui_address_book):
    def __init__(self,loginWindow):
        super().__init__()
        # 修改个人信息
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()

        self.account =loginWindow.account
        self.insertData()
        self.tableWidget.cellClicked.connect(self.cellClicked)
        self.btn_addAddress.clicked.connect(self.addAddress)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_return.clicked.connect(self.back)

    def insertData(self):

        # temp = LoginWindow()     #调用登陆时输入的账号

        statement = f"SELECT * FROM address_book WHERE user_id = '{self.account}'"
        result = self.sql.execute_query(statement)
        print(result)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        # 将查询结果填充到表格中
        for row_num, row_data in enumerate(result):
            print(row_data)
            self.tableWidget.insertRow(row_num)

            item1 = QTableWidgetItem(str(row_num))
            self.tableWidget.setItem(row_num, 0, item1)
            item2 = QTableWidgetItem(str(row_data[1]))
            self.tableWidget.setItem(row_num, 1, item2)
            item3 = QTableWidgetItem(str(row_data[2]))
            self.tableWidget.setItem(row_num, 2, item3)
            item4 = QTableWidgetItem(str(row_data[3]))
            self.tableWidget.setItem(row_num, 3, item4)
            item5 = QTableWidgetItem(str(row_data[4]))
            self.tableWidget.setItem(row_num, 4, item5)
            item6 = QTableWidgetItem(str(row_data[5]))
            self.tableWidget.setItem(row_num, 5, item6)

    def cellClicked(self, row, column):
        self.row = row
        self.column = column

    def addAddress(self):
        self.window_addAdress = Window_addAddress(loginWindow=self)
        self.window_addAdress.show()

    def delete(self):
        result_name = self.tableWidget.item(self.row, 1).text()
        result_phone = self.tableWidget.item(self.row, 2).text()
        result_province = self.tableWidget.item(self.row, 3).text()
        result_city = self.tableWidget.item(self.row, 4).text()
        result_address = self.tableWidget.item(self.row, 5).text()

        statement = f"DELETE FROM address_book WHERE name= %s AND phone =%s AND province=%s AND city=%s AND place=%s"
        value = (result_name, result_phone, result_province, result_city, result_address)  # 单个元素加上逗号
        self.sql.execute_update(statement, value)
        QMessageBox.information(self, "成功", "你已成功删除一条地址簿信息！", QMessageBox.Ok)
        self.insertData()

    def back(self):
        self.close()


class Window_addAddress(QWidget,Ui_add_address_book):
    def __init__(self,loginWindow):
        super().__init__()
        # 修改个人信息
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()
        self.account=loginWindow.account

        statement = "SELECT prv_name FROM province"
        result_comboBox = self.sql.execute_query(statement)
        print(result_comboBox)  # 格式不对，需要转换
        result_list = [item[0] for item in result_comboBox]
        print(result_list)
        self.comboBox_province.addItems(result_list)
        self.comboBox_province.currentTextChanged.connect(self.change_1)
        self.btn_add.clicked.connect(self.bind)
        self.btn_add.clicked.connect( loginWindow.insertData)
        self.btn_return.clicked.connect(self.back)

    def change_1(self):
        result = self.comboBox_province.currentText()
        statement = f"SELECT city_name FROM city, province WHERE city.prv_id = province.prv_id AND province.prv_name ='{result}'"
        result_comboBox = self.sql.execute_query(statement)
        result_list = [item[0] for item in result_comboBox]
        self.comboBox_city.clear()
        self.comboBox_city.addItems(result_list)

    def bind(self,loginWindow):
        result_name = self.lineEdit_name.text()
        result_phone = self.lineEdit_phone.text()
        result_province = self.comboBox_province.currentText()
        result_city = self.comboBox_city.currentText()
        result_address = self.lineEdit_address.text()

        statement = "INSERT INTO address_book (user_id,name,phone,province,city,place) VALUES (%s,%s, %s, %s,%s,%s)"
        values = (self.account,result_name, result_phone, result_province, result_city, result_address)
        self.sql.execute_insert(statement, values)
        QMessageBox.information(self, "成功", "你已成功添加一条地址簿信息", QMessageBox.Ok)
        self.close()
        loginWindow.insertData()

    def back(self):
        self.close()

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
