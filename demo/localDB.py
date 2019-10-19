# author : Charles
# time   ：2019/10/15  13:46 
# file   ：localDB.PY
# PRODUCT_NAME  ：PyCharm

import pymysql
config={'host':'localhost','user':'root','password':'111111','database':'monitor','charset':'utf8','port':3306}




# get new data in order to send to frontend
def select_new_data():
    def get_new(str2, num=1):
        sql = "select * from "+str(str2)+" order by ts desc limit " + str(num)
        cur.execute(sql)
        data = cur.fetchall()
        for row in data:
            result = {"monitor": str2, "value": float(row[0]), "time": row[1], "IsNormal": row[2]}
            data_result_list.append(result)

    data_result_list = []
    connection = pymysql.connect(**config)
    cur = connection.cursor()
    get_new("pressure")
    get_new("temperature1")
    get_new("humidity")
    get_new("locationx",3)
    get_new("locationy",3)

    print(data_result_list[2]['time'])
    cur.close()
    connection.close()
    return data_result_list



# this is used for testing
if __name__ == '__main__':
    select_new_data()