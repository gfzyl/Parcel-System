from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem,QMessageBox
from qt_material import apply_stylesheet

from .deliveryman_main_ui import Ui_deliveryman_main
from ...controller.sql import Sql
from ...controller.routeMap import route

 # 继承QWidget类，以获取其属性和方法
class DeliverymanMainWindow(QWidget,Ui_deliveryman_main):
    logout_signal = Signal()
    def __init__(self,loginWindow):
        super().__init__()
        # 设置界面为我们生成的界面
        self.setupUi(self)
        self.sql = Sql()
        self.sql.connect()
        loginWindow.login_signal.connect(self.receiveAccount)

        self.comboBox_place.currentTextChanged.connect(self.displayText)
        self.btn_return.clicked.connect(self.logoutFun)
        self.btn_confirm.clicked.connect(self.confirm)

    def receiveAccount(self, account):
        self.account = account
        self.insertData()

        statement = f"SELECT sender_prv,recipient_prv FROM parcel_info WHERE delivery_id = '{self.account}'"
        result_prv = self.sql.execute_query(statement)
        routeList = route(result_prv[0][0], result_prv[0][1])
        self.comboBox_place.addItems(routeList)

    def displayText(self):
        result = self.comboBox_place.currentText()
        self.lineEdit_place.setText(result)

    def insertData(self):

        statement = f"SELECT * FROM parcel_info WHERE delivery_id = '{self.account}'"
        result = self.sql.execute_query(statement)
        print(result)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        # 将查询结果填充到表格中
        for row_num, row_data in enumerate(result):
            print(row_data)
            self.tableWidget.insertRow(row_num)

            result =route(row_data[3],row_data[8])
            result_route = '->'.join(result)

            item1 = QTableWidgetItem(str(row_num))
            self.tableWidget.setItem(row_num, 0, item1)
            item2 = QTableWidgetItem(str(row_data[0]))
            self.tableWidget.setItem(row_num, 1, item2)
            item3 = QTableWidgetItem(str(result_route))
            self.tableWidget.setItem(row_num, 2, item3)
            item4 = QTableWidgetItem(str(row_data[14]))
            self.tableWidget.setItem(row_num, 3, item4)
            item5 = QTableWidgetItem(str(row_data[17]))
            self.tableWidget.setItem(row_num, 4, item5)


    def confirm(self):

        result=self.lineEdit_place.text()

        statement = f"UPDATE parcel_info SET cur_place = %s WHERE delivery_id= %s"
        value = (result,self.account)  # 单个元素加上逗号
        self.sql.execute_update(statement, value)

        statement = f"UPDATE deliveryman SET cur_pos = %s WHERE delivery_id= %s"
        value = (result, self.account)  # 单个元素加上逗号
        self.sql.execute_update(statement, value)
        QMessageBox.information(self, "成功", "你已成功修改所有订单当前位置！", QMessageBox.Ok)
        self.insertData()

    def logoutFun(self):
        self.logout_signal.emit()
        self.close()

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue.xml")
 
    # 初始化并展示我们的界面组件
    window = DeliverymanMainWindow()
    # 设置窗口图标
    appIcon = QIcon(r"D:\Project\ParcelSystem\Parcel-System\images\快递.png");
    window.setWindowIcon(appIcon);

    window.show()
    
    # 结束QApplication
    app.exec_()
