# 导入sys
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PySide6.QtGui import QIcon
from ...controller.sql import Sql
# 导入我们生成的界面
from .admin_search_postman_ui import Ui_admin_search_postman
from qt_material import apply_stylesheet

 # 继承QWidget类，以获取其属性和方法
class AdminSearchPostmanWindow(QWidget, Ui_admin_search_postman):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sql=Sql()
        self.sql.connect()
        # 进入界面时先把全部结果列出来
        self.searchPostman()

        # 按键
        self.searchBtn.clicked.connect(self.searchPostman)

    

    def searchPostman(self):
        workId = self.workIdInput.text()
        tel = self.telInput.text()
        # 判断是否输入了工号和电话
        if not workId and not tel:
            # 如果两者都没有输入，则查询所有
            statement = 'SELECT * FROM postman'
        elif workId and not tel:
            # 如果只输入了工号，则按工号查询
            statement = f"SELECT * FROM postman WHERE post_id = '{workId}'"
        elif not workId and tel:
            # 如果只输入了电话，则按电话查询
            statement = f"SELECT * FROM postman WHERE post_phone = '{tel}'"
        else:
            # 如果两者都输入了，则构建一个合适的查询语句（根据你的需求来定）
            statement = f"SELECT * FROM postman WHERE post_id = '{workId}' AND post_phone = '{tel}'"

        result = self.sql.execute_query(statement)
        if result:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            
            # 将查询结果填充到表格中
            for row_num, row_data in enumerate(result):
                self.tableWidget.insertRow(row_num)
                item1 = QTableWidgetItem(str(row_data[0]))
                self.tableWidget.setItem(row_num, 0, item1)
                item2 = QTableWidgetItem(str(row_data[2]))
                self.tableWidget.setItem(row_num, 1, item2)
                item3 = QTableWidgetItem(str(row_data[3]))
                self.tableWidget.setItem(row_num, 2, item3)
                item4 = QTableWidgetItem(str(row_data[5]))
                self.tableWidget.setItem(row_num, 3, item4)
                item5 = QTableWidgetItem(str(row_data[4]))
                self.tableWidget.setItem(row_num, 4, item5)

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
    window = AdminSearchPostmanWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.show()
    
    # 结束QApplication
    app.exec_()
