# 导入sys
from ...controller.sql import Sql
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PySide6.QtGui import QIcon

from .admin_manage_deliveryman_ui import Ui_admin_manage_deliveryman
from qt_material import apply_stylesheet

class AdminManageDeliverymanWindow(QWidget, Ui_admin_manage_deliveryman):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()
        
        # 把市表查出来放进sendCityBox和reCityBox
        statement = 'SELECT city_name FROM city'
        citys = self.sql.execute_query(statement)
        cityList = [item[0] for item in citys]
        self.workCityBox.addItems(cityList)




        # 按键
        self.returnBtn.clicked.connect(self.back)
        self.searchBtn.clicked.connect(self.search)
    

    def search(self):
        # 记录当前输入或选择的内容
        self.workId = self.workIdInputTop.text()
        self.workPos = self.workCityBox.currentText()
        base_query = 'SELECT * FROM deliveryman WHERE 1=1' # 永真式，如果下面一个也没点的话就是查出所有
        # 根据用户的输入情况构建不同的 SQL 查询语句
        if self.workId:
            base_query += f" AND delivery_id = '{self.workId}'"

        if self.workPos:
            base_query += f" AND  (work_pos1 = '{self.workPos}' OR work_pos2 = '{self.workPos}')'"

        query = base_query
        deliverymen = self.sql.execute_query(query)
        print(deliverymen)

        if deliverymen:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)       
            # 将查询结果填充到表格中
            for row_num, row_data in enumerate(deliverymen):
                self.tableWidget.insertRow(row_num)
                for col_num in range(8):  
                    item = QTableWidgetItem(str(row_data[col_num]))
                    self.tableWidget.setItem(row_num, col_num, item)

        else:
            # 处理没有查询结果的情况
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)



    
    def back(self):
        self.close()


if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
    window = AdminManageDeliverymanWindow()
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);
    window.show()
    app.exec_()
