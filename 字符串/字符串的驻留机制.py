# 使用人：贾文杰
# 开发时间：2022/1/8 12:46
a='python'
b="python"
c='''python'''
print(id(a),id(b),id(c))
#字符串长度为0或1
#符合标识符的字符串
#字符串只在编译时驻留，而非运行时
#-5到256的整数数字是驻留的
import sys
a='abc%'
b='abc%'
print(a is b)
a=sys.intern(b)
print(a is b)
#在交互式上运行  pcharm 进行了优化