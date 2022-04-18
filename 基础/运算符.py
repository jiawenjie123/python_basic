# 使用人：贾文杰
# 开发时间：2022/1/3 9:51

# 标准运算符 + - * /
# //整除运算
# % 取余运算
# ** 幂运算
print(-9 // 4)  # -3
print(9 // -4)  # 向下取整
print(9 % -4)  # 余数=被除数-除数*商 -3
print(-9 % 4)  # 3
# 赋值运算符 从右到左
# 支持链式赋值
a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))
# 支持参数赋值
a = 20
a += 30
# 支持系列解包赋值 左右变量格式与值的个数相同
a, b, c = 10, 20, 30
print(a, b, c)
# 交换
a, b = 1, 2
a, b = b, a
print(a, b)

# 比较运算符
print(a > b)
# 结果为bool型
print(a == b)  # 比较运算符 比较值
m = 10
n = 10
print(m is n)  # 比较表示
list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)
print(list1 is list2)
print(list1 is not list2)

# 布尔运算符
# and 与 or 或  not 取反
# in  not in
a = 'hello'
print('h' in a)

# 位运算符 转为二进制
# & 对应数都为1 结果为1 否则为0 |  对应数都为0 结果为0 否则为1
print(4 & 8)
print((4 | 8))
# << 左移位 高位溢出舍弃，低位补0
# >> 右移位低位溢出舍弃，高位补0

#运算符优先级
#先算数运算符，后位运算 <<>> & |,然后比较运算 ，再 布尔运算 ，最后 赋值运算
