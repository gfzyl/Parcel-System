import pymssql

class Sql:
    def __init__(self):
        self.server = '127.0.0.1'
        self.user = 'sa'
        self.password = 'sa'
        self.database = '123'
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pymssql.connect(self.server, self.user, self.password, self.database)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"连接数据库错误: {e}")

    def execute_query(self, statement):
        try:
            self.cursor.execute(statement)
            result = self.cursor.fetchall()
            print("查询成功")
            return result

        except Exception as e:
            print(f"查询操作错误: {e}")
            return None

    def execute_update(self, statement, values=None):
        try:
            self.cursor.execute(statement,values)
            self.conn.commit()
            print("更新成功")
        except Exception as e:
            print(f"更新操作错误: {e}")

    def execute_insert(self, statement, value=None):
            self.execute_update(statement, value)


    def execute_delete(self, statement, value=None):
            self.execute_update(statement, value)

    def sql1(self):
        # print(sql)
        serverName = '127.0.0.1'  # sql服务器名，这里(127.0.0.1)是本地数据库IP
        userName = 'sa'  # 登陆用户名和密码
        passWord = 'sa'  # 建立连接并获取cursor
        conn = pymssql.connect(serverName, userName, passWord, "kd")  # 连接数据库
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        cur = conn.cursor()  # 创建游标 提交sql语句
        cur.execute(self)  # 提交sql命令
        fanhui = cur.fetchall()  # 获取查询结果 在fanhui列表中以[( ,),( ,)]保存
        cur.close()  # 关闭游标
        conn.close()
        if fanhui == []:
            fanhui = [('',), ]
        return fanhui


    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()



