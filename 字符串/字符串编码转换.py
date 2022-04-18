# 使用人：贾文杰
# 开发时间：2022/1/12 10:49
#编码
s = '天涯共此时'
print(s.encode(encoding='GBK'))#一个中文占两个字节
print(s.encode(encoding='UTF-8'))#三个字节

#解码
byte =s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))