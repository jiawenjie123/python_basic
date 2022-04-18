# 使用人：贾文杰
# 开发时间：2022/1/10 18:08
import string
s='hello,hello'
print(s.index('lo'))#第一次出现的位置 不存在 报错
print(s.find('lo'))#第一次出现位置 不存在 返回-1
print(s.rindex('lo'))#最后一次出现位置 不存在 报错
print(s.rfind('lo'))#最后一次出现位置 不存在 返回-1