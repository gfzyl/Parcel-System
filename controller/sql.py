import pymssql

class Sql:
    def __init__(self):
        self.server = '127.0.0.1'
        self.user = 'sa'
        self.password = 'gfyl999'
        self.database = 'parcel'
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pymssql.connect(
                self.server,
                self.user,
                self.password,
                self.database,
                charset='utf8'
                )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"连接数据库错误: {e}")
            return None

    def execute_query(self, statement):
        try:
            self.cursor.execute(statement)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"查询操作错误: {e}")
            return None

    def execute_update(self, statement, values=None):
        try:
            self.cursor.execute(statement,values)
            self.conn.commit()
            print("操作成功")
            return True
        except Exception as e:
            return False

    def execute_insert(self, statement, value=None):
            return self.execute_update(statement, value)


    def execute_delete(self, statement, value=None):
            return self.execute_update(statement, value)


    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()



