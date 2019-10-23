# author : Charles
# time   ：2019/10/15  13:46 
# file   ：localDB.PY
# PRODUCT_NAME  ：PyCharm

import numpy as np
import pymysql
import datetime
config={'host':'10.200.43.40','user':'root','password':'1','database':'monitor','charset':'utf8','port':3306}




# get new data in order to send to frontend
def select_new_data():
    def get_new(str2, num=1):
        sql = "select * from "+str(str2)+" order by ts desc limit " + str(num)
        cur.execute(sql)
        data = cur.fetchall()
        result = {"monitor": str2,}
        value = []
        time = []
        IsNormal = []
        for row in data:
            value.append(float(row[0]))
            time.append((datetime.datetime(2019,10,23,10,29,5)-row[1]).seconds+1)
            # time.append((datetime.datetime.now()-row[1]).seconds+1)
            IsNormal.append(row[2])
        value.reverse()
        time.reverse()
        IsNormal.reverse()
        result['value'] = value
        result['time'] = time
        result['IsNormal'] = IsNormal
        # print(result)
        if str2 == "locationx":
            locationx.append(value)
            locationx.append(time)
        elif str2 == "locationy":
            locationy.append(value)
        data_result_list.append(result)

    data_result_list = []
    locationx = []
    locationy = []
    connection = pymysql.connect(**config)
    cur = connection.cursor()
    get_new("pressure")
    get_new("temperature1")
    get_new("humidity")
    get_new("locationx",3)
    get_new("locationy",3)

    # print(data_result_list[2]['time'])
    cur.close()
    connection.close()
    trail = np.array([locationx[0],locationy[0],locationx[1]]).T.tolist()
    traildict = {'monitor':"trail",'value':trail}
    # print(traildict)
    data_result_list.append(traildict)
    return data_result_list



# this is used for testing
if __name__ == '__main__':
    select_new_data()