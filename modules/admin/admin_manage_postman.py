from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtGui import QIcon
from ...controller.sql import Sql
from .admin_manage_postman_ui import Ui_admin_manage_postman
from qt_material import apply_stylesheet
from ...controller.sql import Sql

 # 继承QWidget类，以获取其属性和方法
class AdminManagePostmanWindow(QWidget, Ui_admin_manage_postman):
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

        # 按键或操作
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
        base_query = 'SELECT * FROM postman WHERE 1=1' # 永真式，如果下面一个也没点的话就是查出所有
        # 根据用户的输入情况构建不同的 SQL 查询语句
        if self.workId:
            base_query += f" AND post_id = '{self.workId}'"

        if self.workPos:
            base_query += f" AND work_pos = '{self.workPos}'"

        query = base_query
        postman = self.sql.execute_query(query)

        if postman:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)       
            # 将查询结果填充到表格中
            for row_num, row_data in enumerate(postman):
                self.tableWidget.insertRow(row_num)
                for col_num in range(6):  
                    item = QTableWidgetItem(str(row_data[col_num]))
                    self.tableWidget.setItem(row_num, col_num, item)

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
        self.workCityInput.setText(self.tableWidget.item(row, 4).text())
        self.ageInput.setText(self.tableWidget.item(row, 5).text())


    def update(self):
        # 更新数据
        if self.row==-1:
            QMessageBox.information(self, "提示", "请选择要修改的数据！", QMessageBox.Ok)
            return
        
        # 不能改ID
        workId = self.workIdInputBottom.text()
        pwd = self.pwdInput.text()
        tel = self.telInput.text()
        workCity = self.workCityInput.text()
        statement = f"UPDATE postman SET post_pwd = %s, post_phone = %s, work_pos = %s WHERE post_id = %s"
        value = (pwd, tel, workCity, workId,)        

        if self.sql.execute_update(statement,value):
            QMessageBox.information(self, "提示", "修改员工记录成功！", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "警告", "修改员工记录失败！", QMessageBox.Ok) 
        # 更新完以后结果直接显示
        self.search()


    def delete(self):
        # 删除数据
        if self.row==-1:
            QMessageBox.warning(self, "警告", "请选择一条员工信息记录！", QMessageBox.Ok)
            return

        workId = self.workIdInputBottom.text()
        statement = f"DELETE FROM postman WHERE post_id = %s"
        value = (workId,)
        if self.sql.execute_update(statement,value):
            QMessageBox.information(self, "提示", "删除员工记录成功！", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "警告", "删除员工记录失败！", QMessageBox.Ok)
              
        self.search()

    
    def insertNew(self):
        # 插入新数据
        workId = self.workIdInputBottom.text()
        name = self.nameInput.text()
        age = self.ageInput.text()
        pwd = self.pwdInput.text()
        tel = self.telInput.text()
        workCity = self.workCityInput.text()
        statement = "INSERT INTO postman (post_id, post_pwd,  post_name, post_phone, work_pos, post_age) VALUES (%(workId)s,%(pwd)s, %(name)s, %(tel)s, %(workCity)s,%(age)s)"
        values = {"workId":workId,"pwd": pwd, "name": name, "tel": tel, "workCity": workCity,"age": age,}        
        # 判重
        requirement = f"SELECT * FROM postman WHERE post_id = {workId}"
        if self.sql.execute_query(requirement):
            QMessageBox.warning(self, "警告", "该员工已存在！", QMessageBox.Ok)
            return
        else:
            if self.sql.execute_insert(statement,values):
                QMessageBox.information(self, "提示", "新增员工记录成功！", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "警告", "新增员工记录失败！", QMessageBox.Ok)
        # 更新完以后结果直接显示
        self.search()      


        
