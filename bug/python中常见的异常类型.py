# 使用人：贾文杰
# 开发时间：2022/1/14 10:51
#数学运算异常
#print(10/0) ZeroDivisionError

#索引异常
#lst=[11,22,33,44]
#print(lst[4]) IndexError

#映射中没有这个键
#dic={'name':'张三','age':'2'}
#print(dic['gender']) KeyError

#没有申明
#NameError

#语法错误
#SyntaxError

#传入无效参数
#ValueError
import traceback
#traceback模块打印异常信息
try:
    print('----------')
    print(1/0)
except:
    traceback.print_exc()