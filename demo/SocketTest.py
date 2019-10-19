# author : Charles
# time   ：2019/10/10  15:23 
# file   ：SocketTest.PY
# PRODUCT_NAME  ：PyCharm
from flask import Flask,render_template, session, request
from flask_socketio import SocketIO,emit
import psutil
import time

from threading import Lock
thread = None
thread_lock = Lock()
app=Flask(__name__)
socketio=SocketIO()
socketio.init_app(app)

# 后台线程 产生数据，即刻推送至前端
def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(5)
        count += 1
        t = time.strftime('%M:%S', time.localtime()) # 获取系统时间（只取分:秒）
        cpus = psutil.cpu_percent(interval=None, percpu=True) # 获取系统cpu使用率 non-blocking
        socketio.emit('server_response',
                      {'data': [t, *cpus], 'count': count},
                      namespace='/test')

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


# 与前端建立 socket 连接后，启动后台线程
@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=5101,debug=True)