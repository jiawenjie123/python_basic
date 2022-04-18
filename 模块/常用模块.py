# 使用人：贾文杰
# 开发时间：2022/1/14 21:53
import  sys#与python解释器及其环境操作相关
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time
print(time.time())
print(time.localtime(time.time()))

import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())

import decimal#用于精度控制，有效位