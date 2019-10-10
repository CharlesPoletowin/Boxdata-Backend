# author : Charles
# time   ：2019/10/10  14:04 
# file   ：Iot_GetData.PY
# PRODUCT_NAME  ：PyCharm

import pymongo
import threading


class get_data:
    def __init__(self, from_address, to_address):
        myclient_from = pymongo.MongoClient (from_address)
        mydb_from = myclient_from['iotmanager']
        self.mycol_from = mydb_from['monitordata']

        myclient_to = pymongo.MongoClient (to_address)
        mydb_to = myclient_to['iotmanager']
        self.mycol_to = mydb_to['data_processed']

    def update_data(self):
        # 获得当前数据库中的最新数据的时间戳
        # self.mycol_to.delete_many({})
        latest_date_data = self.mycol_to.find ().sort ("Timestamp", -1).limit (1)
        latest_date = None
        for i in latest_date_data:
            latest_date = i['Timestamp']
        if not latest_date:
            myquery = {}
        else:
            myquery = {"Timestamp": {"$gt": latest_date}}

        n = 0
        m = 0
        # 获得远程数据库中的剩余数据
        number_of_update = self.mycol_from.count_documents(myquery)

        if number_of_update != 0:
            print ('%s 条数据待更新' % number_of_update)
            update_data = self.mycol_from.find (myquery)
            for data in update_data:
                if 'MonitorName' not in data:
                    continue
                MonitorName = data['MonitorName'].split ('-')[0]
                value = data['Value']
                timestamp = data['Timestamp']
                myquery = {"Timestamp": timestamp}
                findTimeStamp = self.mycol_to.find_one (myquery)
                mydict = {"Timestamp": timestamp,
                          MonitorName: value,
                          'isNormal': True}
                finished = self.mycol_to.insert_one (mydict)
                m +=1
                # print ('成功插入 1 条数据')
            print ('更新 %s 条数据,其中 %s 条新插入，%s 条增加新条目' % (update_data.count(),m,n))
            print(n,m)
        else:
            # 没有更新的数据
            print ('暂无更新数据')


    # 运行这个函数后，每秒钟执行一次
    def update_evevy_second(self):
        self.update_data ()
        timer = threading.Timer (2, getData.update_evevy_second)
        timer.start ()

address_1 = 'mongodb://shudev2:Etp13A3NROECpQeJ1GjTbkj7OqHfoukak17BwiMgcjw6g2ap5PPZsfraINEVJ1G34UtR2MHUJCTufvhAz2uwLQ==@shudev2.documents.azure.cn:10255/?ssl=true&replicaSet=globaldb'
address_2 = 'mongodb://localhost:27017/'
getData = get_data (address_1, address_2)
getData.update_data()
# 定时调度
# timer = threading.Timer (0, getData.update_evevy_second)
# timer.start ()