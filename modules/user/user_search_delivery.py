# 导入sys
import sys

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget,QTableWidgetItem
from PySide6.QtGui import QIcon
from ...controller.sql import Sql
# 导入我们生成的界面
from .user_search_delivery_ui import Ui_user_search_delivery
from qt_material import apply_stylesheet

 # 继承QWidget类，以获取其属性和方法
class UserSearchDeliveryWindow(QWidget,Ui_user_search_delivery):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sql=Sql()
        self.sql.connect()
        
        # 按键
        self.returnBtn.clicked.connect(self.back)
        self.searchBtn.clicked.connect(self.searchDelivery)

    def back(self):
        # 清除输入框的搜索条件，确保每次进来都是空的
        self.parcelIdInput.clear()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(12) # 每次看到都有12个空列
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


# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = UserSearchDeliveryWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.setWindowOpacity(0.95); 
    window.show()
    
    # 结束QApplication
    app.exec_()
