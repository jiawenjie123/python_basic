# 使用人：贾文杰
# 开发时间：2022/1/14 9:10
def fun(a, b=10):  # b为默认值参数
    print(a, b)


fun(100)
fun(20, 30)


# 个数可变的位置参数 结果为元组
def fon(*args):  # fon(*args,*args)会报错
    print(args)


fon(10)
fon(10, 20, 30)


# 个数可变的关键字形参 结果为字典
def fan(**args):  # fan(**args,**args)会报错
    print(args)


fan(a=10)
fan(a=10, b=20, c=30)
print()


def fun1(a, b, c):  # 形参
    print('a', a)
    print('b', b)
    print('c', c)


fun1(10, 20, 30)  # 位置传参
lst = [11, 22, 33]  # 将列表的每个元素转为位置实参
fun1(*lst)  #

fun1(a=100, c=10, b=90)  # 关键字实参
dic = {'a': 100, 'b': 90, 'c': 10}
fun1(**dic)  # 将字典中的键值对转换为关键字参数传入


def fun4(a, b, *, c, d):#*号之后只能用关键字实参
    print('a', a)
    print('b', b)
    print('c', c)
    print('d', d)


fun4(10, 20, c=10, d=20)
# c  d 只能采用关键字传递

#变量的作用域
def m(a,b):
    c=a+b
    print(a+b)#a，b，c 局部变量

name=1
def n():
    print(name)#name为全局变量
n()

#global
#在函数内部的局部变量前加global 就变为全局变量