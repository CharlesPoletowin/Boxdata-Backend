# author : Charles
# time   ：2019/10/11  11:34 
# file   ：GettingDataFromCloud.PY
# PRODUCT_NAME  ：PyCharm

import pymongo
import pymysql
import threading

import shared

dict1={'水中臭氧浓度':'o3water', '重量数据':'weight', '进气臭氧浓度':'ino3', '湿度':'humidity', '温度':'temperature2', '通道':'channel1', '尾气臭氧浓度':'outo3', 'PRESSURE-0001':'pressure', 'TEMPERATURE-0001':'temperature1', 'PH':'ph'}
config={'host':'localhost','user':'root','password':'111111','database':'monitor','charset':'utf8','port':3306}
address_1 = 'mongodb://shudev2:Etp13A3NROECpQeJ1GjTbkj7OqHfoukak17BwiMgcjw6g2ap5PPZsfraINEVJ1G34UtR2MHUJCTufvhAz2uwLQ==@shudev2.documents.azure.cn:10255/?ssl=true&replicaSet=globaldb'


class GetData:
    def __init__(self,from_address):
        my_client_from = pymongo.MongoClient(from_address)
        my_db_from = my_client_from['iotmanager']
        self.my_col_from = my_db_from['monitordata']

    def update(self):
        if shared.latest_date is None:
            my_query = {"MonitorName":{"$exists":True}}
        else:
            my_query = {"Timestamp": {"$gt": shared.latest_date}}
            # 获得远程数据库中的剩余数据
        number_of_update = self.my_col_from.count_documents(my_query)
        if number_of_update != 0:
            update_data = self.my_col_from.find(my_query)
            temp = update_data.sort("Timestamp", -1).limit (1)
            connection = pymysql.connect(**config)
            cur = connection.cursor()
            for i in temp:
                shared.latest_date=i['Timestamp']
            for x in update_data:
                monitor = dict1.get(x['MonitorName'])
                value = x['Value']
                timestamp = x['Timestamp']
                tempp = (value,timestamp,True)
                if shared.consume.full():
                    shared.consume.get()
                shared.put([monitor,value,timestamp])
                sql = 'insert into ' + str(monitor) + '( v, ts, IsNormal ) values (%s, %s, %s)'
                cur.execute(sql,tempp)
            connection.commit()
            cur.close()


if __name__ == '__main__':
    gd=GetData(address_1)
    timer=threading.Timer(1,gd.update)
    timer.start()