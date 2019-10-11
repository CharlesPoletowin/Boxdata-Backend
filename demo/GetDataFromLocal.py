# author : Charles
# time   ：2019/10/10  14:27 
# file   ：GetDataFromLocal.PY
# PRODUCT_NAME  ：PyCharm
import pymongo
addr='mongodb://localhost:27017/'
# myclient=pymongo.MongoClient(addr)
# mydb=myclient["iotmanager"]
# mycol=mydb["data_processed"]
# myquery={"TEMPERATURE":{"$exists":True}}
# mydoc=mycol.find(myquery)
# for x in mydoc:
#     print(x['Timestamp'],end="  ")
#     print(x["TEMPERATURE"])
# print(type(mydoc))

address_1 = 'mongodb://shudev2:Etp13A3NROECpQeJ1GjTbkj7OqHfoukak17BwiMgcjw6g2ap5PPZsfraINEVJ1G34UtR2MHUJCTufvhAz2uwLQ==@shudev2.documents.azure.cn:10255/?ssl=true&replicaSet=globaldb'
myclient=pymongo.MongoClient(address_1)
mydb=myclient['iotmanager']
mycol=mydb['monitordata']
# myquery={"MonitorName":{"$exists":True}}
# {'水中臭氧浓度', '重量数据', '进气臭氧浓度', '湿度', '温度', '通道', '尾气臭氧浓度', 'PRESSURE-0001', 'TEMPERATURE-0001', 'PH'}

myquery={"MonitorName":{"$exists":False}}
mydoc=mycol.find(myquery)
b=set()
c=0
for x in mydoc:
    print(x)
    c=c+1
    # b.add(x["MonitorName"])
print(c)
print(b)
