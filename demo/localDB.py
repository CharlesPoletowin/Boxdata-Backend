# author : Charles
# time   ：2019/10/15  13:46 
# file   ：localDB.PY
# PRODUCT_NAME  ：PyCharm

import numpy as np
import pymysql
import datetime
config={'host':'210.14.69.108','user':'root','password':'1','database':'iot','charset':'utf8','port':3306}


temp =""

# get new data in order to send to frontend
def select_new_data():
    def get_new(str2, num=1):
        sql = "select value, time, isNormal from "+str(str2)+" order by time desc limit " + str(num)
        cur.execute(sql)
        data = cur.fetchall()
        value = []
        time = []
        normal = []
        abnormal = []
        temp = ""
        for row in data:
            if temp == "":
                temp = row[1]
            if str2 == "temperature" or str2 == "humidity" or str2 == "current":
                if row[2] == 0:
                    normal.append([float(row[0]), ((temp-row[1]).seconds+1)])
                else:
                    abnormal.append([float(row[0]), ((temp-row[1]).seconds+1)])
            else:
                if row[2] == 0:
                    normal.append([((temp-row[1]).seconds+1), float(row[0])])
                else:
                    abnormal.append([((temp-row[1]).seconds+1), float(row[0])])
        data1=[normal, abnormal]

        if str2 == "locationx":
            locationx.append(value)
            locationx.append(time)
        elif str2 == "locationy":
            locationy.append(value)
        data_result_list[str2] = data1

    data_result_list = {}
    locationx = []
    locationy = []
    connection = pymysql.connect(**config)
    cur = connection.cursor()
    get_new("temperature",1)
    get_new("humidity")
    get_new("locationx",10)
    get_new("locationy",10)
    get_new("vibration",10)

    # print(data_result_list[2]['time'])
    cur.close()
    connection.close()
    # trail = np.array([locationx[0],locationy[0],locationx[1]]).T.tolist()
    # traildict = {'monitor':"trail",'data':trail}
    # print(traildict)
    # data_result_list.append(traildict)
    return data_result_list



# this is used for testing
if __name__ == '__main__':
    select_new_data()