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
            #print("查询成功")
            # if result == []:
            #     result   = [('',), ]
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


    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()



