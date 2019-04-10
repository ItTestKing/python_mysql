from mysql import connector
import logging
import csv
from time import sleep

class search():
    mydb = connector.connect(
        host='192.168.0.195',
        user='root',
        passwd='root',
        database='mirror',
        charset='utf8'
    )

    i = 150
    # sql = "INSERT INTO mr_host (ck, name, mac, is_auth) VALUES (' +  str(i), str(i), str(i), 1 + ')"

    for i in range(160, 200):
        sqlpre = "INSERT INTO mr_host (ck, name, mac, is_auth) VALUES ("
        sqlend = ")"
        sqlsplit = ","
        sqlck = "\'" + str(i) + "\'"
        sqlname = "\'" + str(i) + "\'"
        sqlmac = "\'" + str(i) + "\'"
        sqlisauth = str(1)
        sql = sqlpre + sqlck + sqlsplit + sqlname + sqlsplit + sqlmac + sqlsplit + sqlisauth + sqlend
        print(sql)
        logging.info(sql)
        # sql = "INSERT INTO mr_host (ck, name, mac, is_auth) VALUES ('zx11','zx11','zx11', 1)"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()

    # mycursor.close()
    # mydb.close()



