from ...controller.sql import Sql
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
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
        self.search()

        # 按键
        self.tableWidget.cellClicked.connect(self.cellClicked)
        self.returnBtn.clicked.connect(self.back)
        self.searchBtn.clicked.connect(self.search)
        self.updBtn.clicked.connect(self.update)
        self.createBtn.clicked.connect(self.insertNew)
        self.delBtn.clicked.connect(self.delete)
    

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

        if deliverymen:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)       
            # 将查询结果填充到表格中
            for row_num, row_data in enumerate(deliverymen):
                self.tableWidget.insertRow(row_num)
                for col_num in range(8):  
                    item = QTableWidgetItem(str(row_data[col_num]))
                    self.tableWidget.setItem(row_num, col_num, item)
                # 加入状态
                status = ''
                if row_data[6] == row_data[5] or row_data[6 == row_data[4]]:
                    status = '空闲'
                else:
                    status = '忙碌'
                status = QTableWidgetItem(status)
                self.tableWidget.setItem(row_num, 8, status)
                
        else:
            # 处理没有查询结果的情况
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)


    def back(self):
        self.close()


    def cellClicked(self,row,column):
        # 表中选择到的数据展示到下面的文本输入区域中
        self.row=row
        self.column=column
        self.workIdInputBottom.setText(self.tableWidget.item(row, 0).text())
        self.pwdInput.setText(self.tableWidget.item(row, 1).text())
        self.nameInput.setText(self.tableWidget.item(row, 2).text())
        self.telInput.setText(self.tableWidget.item(row, 3).text())
        self.workCityInput1.setText(self.tableWidget.item(row, 4).text())
        self.workCityInput2.setText(self.tableWidget.item(row, 5).text())
        self.ageInput.setText(self.tableWidget.item(row, 7).text())

    
    def update(self):
        # 更新数据
        if self.row==-1:
            QMessageBox.information(self, "提示", "请选择要修改的数据！", QMessageBox.Ok)
            return
        
        # 不能改ID
        workId = self.workIdInputBottom.text()
        pwd = self.pwdInput.text()
        tel = self.telInput.text()
        workCity1 = self.workCityInput1.text()
        workCity2 = self.workCityInput2.text()
        statement = f"UPDATE deliveryman SET delivery_pwd = %s, delivery_phone = %s, work_pos1 = %s, work_pos2 = %s WHERE delivery_id = %s"
        value = (pwd, tel, workCity1, workCity2, workId,)        
        try:
            self.sql.execute_update(statement,value)
        except Exception as e:
            QMessageBox.warning(self, "警告", "修改员工记录失败！", QMessageBox.Ok)
        QMessageBox.information(self, "提示", "修改成功！", QMessageBox.Ok)    
        # 更新完以后结果直接显示
        self.search()


    def delete(self):
        # 删除数据
        if self.row==-1:
            QMessageBox.warning(self, "警告", "请选择一条员工信息记录！", QMessageBox.Ok)
            return

        workId = self.workIdInputBottom.text()
        statement = f"DELETE FROM deliveryman WHERE delivery_id = %s"
        value = (workId,)
        try:
            self.sql.execute_update(statement,value)
        except Exception as e:
            QMessageBox.warning(self, "警告", "删除员工记录失败！", QMessageBox.Ok)
        QMessageBox.information(self, "提示", "删除员工记录成功！", QMessageBox.Ok)
        # 更新完以后结果直接显示
        self.search()

    
    def insertNew(self):
        # 插入新数据
        workId = self.workIdInputBottom.text()
        name = self.nameInput.text()
        age = self.ageInput.text()
        pwd = self.pwdInput.text()
        tel = self.telInput.text()
        workCity1 = self.workCityInput1.text()
        workCity2 = self.workCityInput2.text()
        statement = "INSERT INTO deliveryman (delivery_id, delivery_pwd,  delivery_name, delivery_phone, work_pos1, work_pos2,  delivery_age) VALUES (%(workId)s,%(pwd)s, %(name)s, %(tel)s, %(workCity1)s, %(workCity2)s, %(age)s)"
        values = {"workId":workId,"pwd": pwd, "name": name, "tel": tel, "workCity1": workCity1, "workCity2": workCity2 ,"age": age,}
        try:
            self.sql.execute_insert(statement,values)
        except Exception as e:
            QMessageBox.warning(self, "警告", "新增员工记录失败！", QMessageBox.Ok)
        QMessageBox.information(self, "提示", "新增员工记录成功！", QMessageBox.Ok)
        # 更新完以后结果直接显示
        self.search()      
