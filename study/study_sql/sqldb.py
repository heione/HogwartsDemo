import pymysql


class SQL(object):
    def __init__(self):
        print('连接sql')
        # 地址，用户名，密码，库
        self.db = pymysql.connect('localhost', 'root', '123456', 'user_info')
        self.cursor = self.db.cursor()

    def select_sql(self, sql):
        """
        执行查询语句
        :param sql: 查询语句
        :return: 返回所有值
        """
        # 执行sql语句
        self.cursor.execute(sql)
        # 获取所有记录列表
        data = self.cursor.fetchall()
        return data

    def update_sql(self, sql):
        """
        执行增删改语句
        :param sql:增删改语句
        :return:True or False
        """
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            return True
        except:
            # 发生错误时回滚
            self.db.rollback()
            return False

    @classmethod
    def get_instance(cls):
        # 利用反射,看看这个类有没有_instance属性
        if not hasattr(SQL, '_instance'):
            SQL._instance = SQL()

        return SQL._instance

    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, '_instance'):
    #         cls._instance = super().__new__(cls)
    #
    #     return cls._instance


# single1 = SQL()
# single2 = SQL()
# print(id(single1) == id(single2))
# a = SQL.get_instance()
# b = SQL.get_instance()
# print(id(a) == id(b))
