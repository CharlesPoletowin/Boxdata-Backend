1. 这个项目是boxdata的后端部分
2. 该项目主要利用websocket连接传输数据，对于所有连接上的前端页面，采用广播机制分发信息。
3. localDB.py是取mysql数据库的操作
4. app.py是唯一主文件
5. DataEncoder是处理时间格式在json交互中错误的bug。
6. 其它文件无实际意义。
7. README 写于实习结束前，项目进行交接。