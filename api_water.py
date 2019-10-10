from flask import Flask, request, jsonify
import pymongo
import json
from bson import json_util
import OutputJson1 as JJ
import pandas as pd
import time

app = Flask (__name__)


# 获取water数据库的数据
@app.route ('/data/v1.0/water_data', methods = ['get'])
def getWaterData_fuc():
    try:
        site = request.args.get ('site')
        month = request.args.get ('month')
    except:
        return ('fail')

    elements_json = OJ.elements_json (site, month)

    return jsonify (elements_json)


@app.route ('/data/v1.0/water_data_normalization', methods = ['get'])
def getWaterDataNor_fuc():
    try:
        site = request.args.get ('site')
        month = request.args.get ('month')
    except:
        return ('fail')

    elements_json = OJ.elements_json (site, month, True)

    return jsonify (elements_json)


# 获取water数据最新的一次数据
@app.route ('/data/v1.0/water_recent_data', methods = ['get'])
def getWaterRecentData_fuc():
    recent_json = recent_file
    return jsonify (recent_json)


# 获取water所有站点及月份数据
@app.route ('/data/v1.0/water_site_month', methods = ['get'])
def getWaterSiteAndMonth_fuc():
    recent_json = OJ.siteAndMonth ()
    return jsonify (recent_json)


# 获取water数据abnormal.json
@app.route ('/data/v1.0/water_abnormal_data', methods = ['get'])
def getWaterAbnormalData_fuc():
    abnormal_json = abnormal_file
    return jsonify (abnormal_json)


# 人工标记异常情况
@app.route ('/data/v1.0/abnormal_mark', methods = ['post'])
def abnormalMark_fuc():
    try:
        site = request.form.get ('site')
        time1 = request.form.get ('time1')
        time2 = request.form.get ('time2')
        marker = request.form.get ('marker')
    except:
        return ('fail')

    # 内存中的数据修改
    siteno_re = str (OJ.modify_marker (site, time1, time2, marker))

    time_array_1 = time.strptime (time1, '%Y-%m-%d %H:%M:%S')
    time1 = int (time.mktime (time_array_1)) * 1000
    time_array_2 = time.strptime (time2, '%Y-%m-%d %H:%M:%S')
    time2 = int (time.mktime (time_array_2)) * 1000

    myclient = pymongo.MongoClient ("mongodb://inesa_water:inesa2019@10.200.43.91:27017")
    myclient_name = 'water'
    mydb_name = 'waterAndAD'
    mydb = myclient[myclient_name]
    mycol = mydb[mydb_name]
    siteno_re = str (list (OJ.site_data[OJ.site_data.sitename == site]['siteno'])[0])
    myquery = {"siteno": siteno_re, 'testtime': {"$gte": int (time1), "$lte": int (time2)}}
    newvalues = {"$set": {"marker": marker}}
    x = mycol.update_many (myquery, newvalues)

    return jsonify ({'success': str (x.modified_count) + '个文档已修改'})


def find_all_data_from_Mongodb():
    myclient_name = 'water'
    mydb_name = 'waterAndAD'
    myclient = pymongo.MongoClient ("mongodb://inesa_water:inesa2019@10.200.43.91:27017")
    mydb = myclient[myclient_name]
    mycol = mydb[mydb_name]
    data = mycol.find ({}, {"_id": 0})

    water_df = pd.DataFrame (list (data))

    return water_df


if __name__ == '__main__':
    water_df = find_all_data_from_Mongodb ()
    OJ = JJ.OutputJson (water_df)
    recent_file = OJ.recent_json ()
    abnormal_file = OJ.abnormal_json ()
    # 这里指定了地址和端口号。
    app.run (host = '0.0.0.0', port = 5055)
