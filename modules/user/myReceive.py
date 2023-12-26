from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PySide6.QtGui import QIcon
from ...controller.sql import Sql
# 导入我们生成的界面
from .myReceive_ui import Ui_myReceive
from qt_material import apply_stylesheet

 # 继承QWidget类，以获取其属性和方法
class MyReceiveWindow(QWidget, Ui_myReceive):
    def __init__(self, user_main_window):
        super().__init__()
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()
        self.account = user_main_window.account
        self.insertData()


        self.tableWidget.cellClicked.connect(self.cellClicked)
        self.confirmBtn.clicked.connect(self.confirmAct)
        self.refuseBtn.clicked.connect(self.refuseAct)
        self.returnBtn.clicked.connect(self.back)


    def insertData(self):
        
        statement = f"SELECT * FROM parcel_info WHERE recipient_tel = '{self.account}'"
        result = self.sql.execute_query(statement)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        # 将查询结果填充到表格中
        for row_num, row_data in enumerate(result):
            self.tableWidget.insertRow(row_num)

            item1 = QTableWidgetItem(str(row_data[0]))
            self.tableWidget.setItem(row_num, 0, item1)
            item2 = QTableWidgetItem(str(row_data[0]))
            self.tableWidget.setItem(row_num, 1, item2)
            item3 = QTableWidgetItem(str(row_data[14]))
            self.tableWidget.setItem(row_num, 2, item3)
            item4 = QTableWidgetItem(str(row_data[15]))
            self.tableWidget.setItem(row_num, 3, item4)

    def confirmAct(self):

        result_id = self.tableWidget.item(self.row,0).text()
        statement = f"UPDATE parcel_info SET status = 2 WHERE parcel_id= %s"
        value = (result_id,)       #单个元素加上逗号
        self.sql.execute_update(statement,value)


    def cellClicked(self,row,column):
        self.row=row
        self.column=column
    def refuseAct(self):
        result_id = self.tableWidget.item(self.row, 0).text()
        statement = f"UPDATE parcel_info SET status = 3 WHERE parcel_id= %s"
        value = (result_id,)  # 单个元素加上逗号
        self.sql.execute_update(statement, value)


    def back(self):
        # 清除输入框的搜索条件，确保每次进来都是空的
        self.close()



# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = MyReceiveWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.show()
    
    # 结束QApplication
    app.exec_()
