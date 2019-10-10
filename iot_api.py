from flask import Flask, request, jsonify
import pymongo
app = Flask (__name__)


# 获取water数据库的数据
@app.route ('/iot/v1.0/data_get', methods = ['get'])
def getIotData_fuc():
    try:
        last_time = request.args.get ('time')

    except:
        return ('fail')

    myquery = {"Timestamp": {"$gt": last_time}}
    elements_json = mycol_to.find (myquery)

    return jsonify (elements_json)



if __name__ == '__main__':
    to_address = 'mongodb://localhost:27017/'
    myclient_to = pymongo.MongoClient (to_address)
    mydb_to = myclient_to['iotmanager']
    mycol_to = mydb_to['data_processed']

    # 这里指定了地址和端口号。
    app.run (host = '0.0.0.0', port = 5055)
