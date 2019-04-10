from mysql import connector
import csv
from time import sleep


class search():
    mydb = connector.connect(
        host='192.168.0.172',
        user='root',
        passwd='root',
        database='mirror',
        charset='utf8'
    )
    sql = "INSERT INTO mr_host (ck,name) VALUES ('11111111111111111111111111', 'wwww')"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()










    def DeletTable(self,table, number):
        sql = "DELETE FROM" + " " + table + " " + "WHERE id REGEXP"
        num = "^" + "[0-" + number + "]"
        mycursor = self.mydb.cursor()
        mycursor.execute(sql + ' ''\'' + num + '\'')
        sleep(50)
        self.mydb.commit()

    # 清空表
    def DeletAll(self,table):
        sql = "truncate" + " " + table
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)

    # 读取csv文件
    def read(self):
        with open("E:\\table.csv", "r", encoding="utf-8") as csvfile:
            read = csv.reader(csvfile)
            for i in read:
                return i[0]

    def cretestring(self):
        x = 0
        for i in range(2000):
            x += 1
            s = str(x)

    #填充数据库
    def create(self):
        sql = "INSERT INTO mr_host (ck, name) VALUES ('111', 'wwww')"
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)

