import decimal

from flask import Flask,render_template
from flask_socketio import SocketIO
import json
import datetime
import localDB
from threading import Lock
thread = None
thread_lock = Lock()
app = Flask(__name__)
# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
app.after_request(after_request)
socketio = SocketIO(app,cors_allowed_origins='*')
# socketio.init_app(app)

class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime.datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, datetime.date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj) 

# 后台线程 产生数据，即刻推送至前端
def background_thread():
    while True:
        socketio.sleep(5)
        get_new = localDB.select_new_data()
        socketio.emit('message', json.dumps(get_new,cls=DateEncoder))

@app.route('/')
def index():
    return 'yes'


@app.route('/test22')
def index2():
    return render_template('index.html', async_mode=socketio.async_mode)

# 与前端建立 socket 连接后，启动后台线程
@socketio.on('connect')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=5101,debug=True)