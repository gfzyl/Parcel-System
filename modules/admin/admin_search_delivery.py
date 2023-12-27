from PySide6.QtWidgets import QApplication, QWidget,QTableWidgetItem
from PySide6.QtGui import QIcon
from ...controller.sql import Sql
from ...controller.routeMap import route

from .admin_search_delivery_ui import Ui_admin_search_delivery
from qt_material import apply_stylesheet


class AdminSearchDeliveryWindow(QWidget, Ui_admin_search_delivery):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()
        self.tableWidget.setColumnWidth(18, 400)  # 完整路线列

        
        # 把省表查出来放进sendCityBox和reCityBox
        statement = 'SELECT prv_name FROM province'
        province = self.sql.execute_query(statement)
        provinceList = [item[0] for item in province]
        self.sendPrvBox.addItems(provinceList)
        self.rePrvBox.addItems(provinceList) 
        self.sendPrvBox.currentTextChanged.connect(self.change_1)
        self.rePrvBox.currentTextChanged.connect(self.change_2)

        # 按键
        self.search() # 先把记录显示
        self.returnBtn.clicked.connect(self.back)
        self.searchBtn.clicked.connect(self.search)

    # 下拉选框选项的绑定
    def change_1(self):
            result = self.sendPrvBox.currentText()
            statement = f"SELECT city_name FROM city, province WHERE city.prv_id = province.prv_id AND province.prv_name ='{result}'"
            result_comboBox = self.sql.execute_query(statement)
            result_list = [item[0] for item in result_comboBox]
            self.sendCityBox.clear()
            self.sendCityBox.addItems(result_list)

    def change_2(self):
            result = self.rePrvBox.currentText()
            statement = f"SELECT city_name FROM city, province WHERE city.prv_id = province.prv_id AND province.prv_name ='{result}'"
            result_comboBox = self.sql.execute_query(statement)
            result_list = [item[0] for item in result_comboBox]
            self.reCityBox.clear()
            self.reCityBox.addItems(result_list)

    
    def back(self):
        self.close()


    def search(self):
        # 获取当前选择的下拉框元素
        self.sendPrv = self.sendPrvBox.currentText()
        self.sendCity = self.sendCityBox.currentText()
        self.receivePrv = self.rePrvBox.currentText()
        self.receiveCity = self.reCityBox.currentText()
        # 获取输入的快递单号，电话号码，配送员工号，快递员工号
        self.parcelId = self.parcelIdInput.text()
        self.tel = self.telInput.text()
        self.deliverymanId = self.deliveryIdInput.text()
        self.postmanId = self.postIdInput.text()
        # 用户可以任意输入或选择（可以叠加信息）
        # print( self.sendPrv,self.sendCity, self.receivePrv,self.receiveCity,self.parcelId, self.tel, self.deliverymanId, self.postmanId)
        
        base_query = 'SELECT * FROM parcel_info WHERE 1=1' # 永真式，如果下面一个也没点的话就是查出所有
        # 根据用户的输入情况构建不同的 SQL 查询语句
        if self.sendPrv:
            base_query += f" AND sender_prv = '{self.sendPrv}'"

        if self.sendCity:
            base_query += f" AND sender_city = '{self.sendCity}'"
        
        if self.receivePrv:
            base_query += f" AND recipient_prv = '{self.receivePrv}'"


        if self.receiveCity:
            base_query += f" AND recipient_city = '{self.receiveCity}'"

        if self.parcelId:
            base_query += f" AND parcel_id = '{self.parcelId}'"

        if self.tel:
            base_query += f" AND recipient_tel = '{self.tel}'"

        if self.deliverymanId:
            base_query += f" AND delivery_id = '{self.deliverymanId}'"

        if self.postmanId:
            base_query += f" AND post_id = '{self.postmanId}'"
        # 最终构建的 SQL 查询语句
        query = base_query
        # print(query)
        parcelInfo = self.sql.execute_query(query)
        # print(parcelInfo)
        
        if parcelInfo:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)       
            # 将查询结果填充到表格中
            for row_num, row_data in enumerate(parcelInfo):
                self.tableWidget.insertRow(row_num)
                for col_num in range(18):  
                    item = QTableWidgetItem(str(row_data[col_num]))
                    self.tableWidget.setItem(row_num, col_num, item)

                
                # 路线
                result = route(row_data[3], row_data[8])
                result_route = '->'.join(result)
                result_route = result_route + '->' + row_data[9] + '->' + row_data[10]

                item = QTableWidgetItem(str(result_route))
                self.tableWidget.setItem(row_num, 18, item)

        else:
            # 处理没有查询结果的情况
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

    

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = AdminSearchDeliveryWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.show()
    
    # 结束QApplication
    app.exec_()
    
