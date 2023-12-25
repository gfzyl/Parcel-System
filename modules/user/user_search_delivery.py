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

            # 获取表头信息，用于映射数据库字段和表格列
            header_labels = [self.tableWidget.horizontalHeaderItem(col).text() for col in range(self.tableWidget.columnCount())]

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
