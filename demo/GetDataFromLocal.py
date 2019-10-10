# author : Charles
# time   ：2019/10/10  14:27 
# file   ：GetDataFromLocal.PY
# PRODUCT_NAME  ：PyCharm
import pymongo
addr='mongodb://localhost:27017/'
myclient=pymongo.MongoClient(addr)
mydb=myclient["iotmanager"]
mycol=mydb["data_processed"]
myquery={"TEMPERATURE":{"$exists":True}}
mydoc=mycol.find(myquery)
for x in mydoc:
    print(x['Timestamp'],end="  ")
    print(x["TEMPERATURE"])
