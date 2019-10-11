# author : Charles
# time   ：2019/10/11  11:28 
# file   ：shared.PY
# PRODUCT_NAME  ：PyCharm
# This file is used for sharing variables
from queue import Queue
latest_date = None
consume = Queue(maxsize=1000)
pressure = []
temperature = []