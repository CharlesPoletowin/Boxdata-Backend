# author : Charles
# time   ：2019/12/5  14:48 
# file   ：test.PY
# PRODUCT_NAME  ：PyCharm
import pymongo

def demo() :
    address_1 = 'mongodb://shudev2:Etp13A3NROECpQeJ1GjTbkj7OqHfoukak17BwiMgcjw6g2ap5PPZsfraINEVJ1G34UtR2MHUJCTufvhAz2uwLQ==@shudev2.documents.azure.cn:10255/?ssl=true&replicaSet=globaldb'
    myclient_from = pymongo.MongoClient(address_1)
    mydb_from = myclient_from['iotmanager']
    mycol_from = mydb_from['monitordata']
    result = mycol_from.find().count()
    print(result)
    pass


if __name__ == '__main__':
    demo()