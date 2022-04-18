# 使用人：贾文杰
# 开发时间：2022/1/10 18:15
s='hello,python'
a=s.upper()#转为大写，会产生一个新的字符串对象
print(s)
print(id(a),id(s))
b=s.lower()#转为小写，会产生新的字符串对象
print(b)
print(id(b))
s2='hello,Python'
print(s2.swapcase())#大变小，小变大
print(s2.capitalize())#第一个变大，其余变小
print(s2.title())#每个单词第一个变大，其余变小
