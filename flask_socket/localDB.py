# author : Charles
# time   ：2019/10/15  13:46 
# file   ：localDB.PY
# PRODUCT_NAME  ：PyCharm

import numpy as np
import pymysql

config = {'host': '10.200.43.149', 'user': 'root', 'password': '1', 'database': 'iot', 'charset': 'utf8', 'port': 3306}


temp = ""


# get new data in order to send to frontend
def select_new_data():
    def demo():
        sql22 = "select x, y, time, isNormal from location where x is not null and y is not null and x >= 0 and x < 310 and y >= 0 and y < 310 order by time desc limit 100"
        cur.execute(sql22)
        data = cur.fetchall()
        normal = []
        abnormal = []
        global temp
        temp = ""
        for row in data:
            if temp == "":
                temp = row[2]
            if row[3] == 0:
                normal.append([row[0], row[1], ((temp - row[2] ).seconds + 1)])
            else:
                abnormal.append([row[0], row[1], ((temp - row[2]).seconds + 1)])
        if len(normal) >= 1:
            t1 = np.array(normal)
            t1[:, 2] = 101 - t1[:, 2]
            normal = t1.tolist()
        if len(abnormal) >= 1:
            t2 = np.array(abnormal)
            t2[:, 2] = 101 - t2[:, 2]
            abnormal = t2.tolist()
        data1 = [normal, abnormal]
        data_result_list["location"] = data1

    def get_new(str2, num=1):
        sql = "select value, time, isNormal from "+str(str2)+" order by time desc limit " + str(num)
        cur.execute(sql)
        data = cur.fetchall()
        normal = []
        abnormal = []
        global temp
        temp = ""
        for row in data:
            if temp == "":
                temp = row[1]
            if num == 1:
                if row[2] == 0:
                    normal.append([float(row[0]), ((temp-row[1]).seconds+1)])
                else:
                    abnormal.append([float(row[0]), ((temp-row[1]).seconds+1)])
            else:
                if row[2] == 0:
                    normal.append([((temp-row[1]).seconds+1), float(row[0])])
                else:
                    abnormal.append([((temp-row[1]).seconds+1), float(row[0])])
        if num > 1:
            if len(normal) >= 1:
                t1 = np.array(normal)
                t1[:, 0] = 1+num-t1[:, 0]
                normal = t1.tolist()
            if len(abnormal) >= 1:
                t2 = np.array(abnormal)
                t2[:, 0] = 1+num-t2[:, 0]
                abnormal = t2.tolist()
        data1 = [normal, abnormal]
        data_result_list[str2] = data1

    def get_new2(str2, num=1):
        sql = "select value, time, isNormal from "+str(str2)+" where value >= 0 and value <= 310 order by time desc limit " + str(num)
        cur.execute(sql)
        data = cur.fetchall()
        normal = []
        abnormal = []
        global temp
        temp = ""
        for row in data:
            if temp == "":
                temp = row[1]
            if num == 1:
                if row[2] == 0:
                    normal.append([float(row[0]), ((temp-row[1]).seconds+1)])
                else:
                    abnormal.append([float(row[0]), ((temp-row[1]).seconds+1)])
            else:
                if row[2] == 0:
                    normal.append([((temp-row[1]).seconds+1), float(row[0])])
                else:
                    abnormal.append([((temp-row[1]).seconds+1), float(row[0])])
        if num > 1:
            if len(normal) >= 1:
                t1 = np.array(normal)
                t1[:, 0] = 1+num-t1[:, 0]
                normal = t1.tolist()
            if len(abnormal) >= 1:
                t2 = np.array(abnormal)
                t2[:, 0] = 1+num-t2[:, 0]
                abnormal = t2.tolist()
        data1 = [normal, abnormal]
        data_result_list[str2] = data1

    data_result_list = {}
    connection = pymysql.connect(**config)
    cur = connection.cursor()
    get_new("temperature")
    get_new("noise")
    get_new("speedx",20)
    get_new("speedy",20)
    get_new2("locationx",40)
    get_new2("locationy",40)
    demo()
    get_new("vibration",20)

    cur.close()
    connection.close()
    print(data_result_list)
    return data_result_list


# this is used for testing
if __name__ == '__main__':
    select_new_data()