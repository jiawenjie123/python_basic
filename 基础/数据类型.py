# 使用人：贾文杰
# 开发时间：2021/12/30 15:34
# 整数 integer 正数 负数 0
# 可表示为二，十，八，十六进制
n1=1
n2=-1
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
print(0b10101111)# 2
print(0o176)# 8
print(0x1EAF)# 16
# 浮点
a=3.14159
print(a,type(a))
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))#浮点数运算
# 布尔 True=1 False=0
f1=True
f2=False
print(f1,type(f1))
print(f1+f2)

# 字符串 三引号可以分行
str1='qwe'
str2="qwe"
str3="""qw
e"""
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
# 数据类型转换 str int float
name='张三'
age=20
print(type(name),type(age))
print('我叫'+name+'，今年'+str(age)+'岁')
s1='128'
print(type(int(s1)))#整数字符串可转，浮点型不行
s2=True
print(int(s2))
s3='128.98'
print(float(s3))
print(float(s2))