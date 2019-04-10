from mysql import connector
import csv
from time import sleep


class mub():
    mydb = connector.connect(
        host='192.168.0.172',
        user='root',
        passwd='root',
        database='mirror',
    )

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
    DeletTable(read())