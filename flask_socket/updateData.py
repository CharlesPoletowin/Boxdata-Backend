import pymongo
import pymysql
import threading
import datetime
#import time
from bson.objectid import ObjectId

class get_data:
    def __init__(self,from_address):
        myclient_from = pymongo.MongoClient (from_address)
        mydb_from = myclient_from['iotmanager']
        self.mycol_from = mydb_from['monitordata']

        self.db_mysql = pymysql.connect ("210.14.69.108", "root", "1", "iot")
        self.cursor = self.db_mysql.cursor ()



    def update_data(self):


        pastday = datetime.datetime.now()+datetime.timedelta(days=-10)
        # print("pastday:",pastday)
        try:
            # 获得当前数据库中的最大id
            max_id_sql = "SELECT _id FROM last_id ORDER BY id DESC LIMIT 1"
            self.cursor.execute (max_id_sql)
            max_id = self.cursor.fetchall ()[0][0]

            try:
                # 存到本地数据库中
                myquery = {"_id": {"$gt": ObjectId(max_id)},"Timestamp": {"$gt": pastday}}
                # print('***********', myquery)
                saved_data_count = self.insert_many(myquery)
                print ('更新 %s 条数据' % saved_data_count)

            except:
                # 没有更新的数据
                print('无更新数据')
                pass
        except:
            # 当前数据库中无数据，获取所有数据，并写入
            myquery = {"Timestamp": {"$gt": pastday}}
            print('当前数据库无数据')
            saved_data_count = self.insert_many(myquery)
            print ('更新 %s 条数据_1' % saved_data_count)

    def insert_many(self, myquery):
        # 获得远程数据库中的剩余数据
        MonitorName_list = ['temp','noise','Humidity','X轴速度','Y轴速度','X轴位移','Y轴位移','Vibration']
        dbName_list = ['temperature', 'noise', 'humidity', 'speedx', 'speedy', 'locationx', 'locationy','vibration']
        update_data = self.mycol_from.find (myquery)
        print('myquery:',myquery)
        print('#############',update_data)
        count = 0
        for item in update_data:
            print('*****************',item['MonitorName'])
            if 'MonitorName' not in item or item['MonitorName'] not in MonitorName_list or 'Value' not in item or type( item['Value']) not in  [type(1),type(1.1)]:
				
                continue
            MonitorName = dbName_list[MonitorName_list.index(item['MonitorName'])]
            

            value = item['Value']
            timestamp = item['Timestamp'].strftime ("%Y-%m-%d %H:%M:%S")
            # print(timestamp)
            sql = "INSERT INTO {0} (time,value) VALUES ('{1}',{2}) ".format(MonitorName,timestamp,value)
            a = self.cursor.execute(sql)
            count += 1
            self.db_mysql.commit()

            if MonitorName == 'locationy':
                sql = "UPDATE location set y = {0} WHERE time = '{1}' ".format(value, timestamp)
                a = self.cursor.execute (sql)
                if a == 0:
                    sql = "INSERT INTO location (time,y) VALUES ('{0}',{1}) ".format (timestamp, value)
                    a = self.cursor.execute (sql)
                self.db_mysql.commit()
            elif MonitorName == 'locationx':
                sql = "UPDATE location set x = {0} WHERE time = '{1}' ".format(value, timestamp)
                a = self.cursor.execute (sql)
                if a == 0:
                    sql = "INSERT INTO location (time,x) VALUES ('{0}',{1}) ".format (timestamp, value)
                    a = self.cursor.execute (sql)
                self.db_mysql.commit()
        if not update_data:
            return 0
        # 更新所保存的最大_id
        update_id_sql = "INSERT INTO last_id (_id) VALUES ('{0}') ".format (str(item['_id']))
        self.cursor.execute (update_id_sql)
        self.db_mysql.commit ()
        return count

    def clean_data(self):
        dbName_list_2 = ['temperature', 'noise', 'humidity', 'speedx', 'speedy', 'locationx', 'locationy','last_id','vibration','location']
        for i in dbName_list_2:
            sql_delete  = 'DELETE FROM {0}'.format(i)
            self.cursor.execute (sql_delete)
            self.db_mysql.commit ()


    # 运行这个函数后，每秒钟执行一次
    def update_evevy_second(self):
        self.update_data ()
        timer = threading.Timer (1, getData.update_evevy_second)
        timer.start ()


if __name__ == '__main__':
    
    address_1  = 'mongodb://shudev2:Etp13A3NROECpQeJ1GjTbkj7OqHfoukak17BwiMgcjw6g2ap5PPZsfraINEVJ1G34UtR2MHUJCTufvhAz2uwLQ==@shudev2.documents.azure.cn:10255/?ssl=true&replicaSet=globaldb'
    address_2 = 'mongodb://localhost:27017/'
    getData = get_data(address_1)

    # getData.clean_data()
    getData.update_evevy_second()

