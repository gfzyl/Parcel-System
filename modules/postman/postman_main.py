from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from qt_material import apply_stylesheet

from .postman_main_ui import Ui_postman_main
from .postman_code_ui import Ui_postman_code
from .postman_search_delivery_ui import Ui_postman_search_delivery
from ...controller.sql import Sql

 # 继承QWidget类，以获取其属性和方法
class PostmanMainWindow(QWidget,Ui_postman_main):
    logout_signal = Signal()
    def __init__(self,loginWindow):
        super().__init__()
        # 设置界面为我们生成的界面
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()
        loginWindow.login_signal.connect(self.receiveAccount)
        self.btn_search.clicked.connect(self.searchFun)
        self.btn_addCode.clicked.connect(self.addCodeFun)
        self.btn_return.clicked.connect(self.logoutFun)
        self.tableWidget.cellClicked.connect(self.cellClicked)


    def receiveAccount(self, account):
        self.account = account
        self.insertData()      #防止找不到self.account

    def insertData(self):

        print('hhhhhh')
        statement = f"SELECT * FROM parcel_info WHERE post_id = '{self.account}'"
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
            item2 = QTableWidgetItem(str(row_data[0]))
            self.tableWidget.setItem(row_num, 1, item2)
            item3 = QTableWidgetItem(str(row_data[7]))
            self.tableWidget.setItem(row_num, 2, item3)
            item4 = QTableWidgetItem(str(row_data[8]))
            self.tableWidget.setItem(row_num, 3, item4)
            item5 = QTableWidgetItem(str(row_data[9]))
            self.tableWidget.setItem(row_num, 4, item5)
            item6 = QTableWidgetItem(str(row_data[15]))
            self.tableWidget.setItem(row_num, 5, item6)
            item7 = QTableWidgetItem(str(row_data[16]))
            self.tableWidget.setItem(row_num, 6, item7)

    def cellClicked(self,row,column):
        self.row=row
        self.column=column
        self.parcelId = self.tableWidget.item(self.row, 1).text()


    def searchFun(self):
        self.searchWindow=Window1(loginWindow=self)
        self.searchWindow.show()
    def addCodeFun(self):
        self.addCodeWindow=Window2(postmanWindow=self)
        self.addCodeWindow.show()

    def logoutFun(self):
        self.logout_signal.emit()
        self.close()

class Window1(QWidget,Ui_postman_search_delivery):
    def __init__(self,loginWindow):
        super().__init__()
        # 添加取件码
        self.setupUi(self)
        self.sql=Sql()
        self.sql.connect()
        self.account = loginWindow.account
        self.btn_return.clicked.connect(self.back)
        self.btn_search.clicked.connect(self.searchDelivery)

    def back(self):
        # 清除输入框的搜索条件，确保每次进来都是空的
        self.lineEdit_parcel.clear()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(12)  # 每次看到都有12个空列
        self.close()

    def searchDelivery(self):
        parcel_id = self.lineEdit_parcel.text()
        statement = f"SELECT * FROM parcel_info WHERE parcel_id = '{parcel_id}'AND post_id='{self.account}'"
        result = self.sql.execute_query(statement=statement)
        if result:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            # 将查询结果填充到表格中
            for row_num, row_data in enumerate(result):
                print(row_data)
                self.tableWidget.insertRow(row_num)

                item1 = QTableWidgetItem(str(row_num))
                self.tableWidget.setItem(row_num, 0, item1)
                item2 = QTableWidgetItem(str(row_data[0]))
                self.tableWidget.setItem(row_num, 1, item2)
                item3 = QTableWidgetItem(str(row_data[7]))
                self.tableWidget.setItem(row_num, 2, item3)
                item4 = QTableWidgetItem(str(row_data[8]))
                self.tableWidget.setItem(row_num, 3, item4)
                item5 = QTableWidgetItem(str(row_data[9]))
                self.tableWidget.setItem(row_num, 4, item5)
                item6 = QTableWidgetItem(str(row_data[15]))
                self.tableWidget.setItem(row_num, 5, item6)
                item7 = QTableWidgetItem(str(row_data[16]))
                self.tableWidget.setItem(row_num, 6, item7)



        else:
            # 处理没有查询结果的情况
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)


class  Window2(QWidget,Ui_postman_code):
    def __init__(self,postmanWindow):
        super().__init__()
        # 查询订单
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()

        self.parcelId =postmanWindow.parcelId
        self.btn_confirm.clicked.connect(self.confirm)
        self.btn_cancel.clicked.connect(self.back)

    def confirm(self):
        result_code = self.lineEdit_code.text()
        statement = f"UPDATE parcel_info SET code = %s WHERE parcel_id= %s"
        value = (result_code,self.parcelId )  # 单个元素加上逗号
        self.sql.execute_update(statement, value)

    def back(self):
        self.close()

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = PostmanMainWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.setWindowOpacity(0.95); 
    window.show()
    
    # 结束QApplication
    app.exec_()
