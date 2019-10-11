from flask import Flask,render_template, session, request
from flask_socketio import SocketIO,emit
import psutil
import time
import shared
from threading import Lock
thread = None
thread_lock = Lock()
app=Flask(__name__)
socketio=SocketIO()
socketio.init_app(app)


# 后台线程 产生数据，即刻推送至前端
def background_thread():
    while True:
        socketio.sleep(5)
        if shared.consume.empty():
            continue
        send_message=shared.consume.get()
        if len(send_message)==2:
            send_message.append(True)
        socketio.emit('message',
                      {'monitor':send_message[0],'value':send_message[1],'IsNormal':send_message[2]},
                      namespace='/test')



# 与前端建立 socket 连接后，启动后台线程
@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=5101)