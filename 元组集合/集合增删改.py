# 使用人：贾文杰
# 开发时间：2022/1/8 11:40
s = {1, 2, 3, 4, 5}
print(10 in s)

s.add(6)
print(s)
s.update({7, 8, 9})
print(s)

s.remove(1)
print(s)  # 不存在抛异常
s.discard(10)  # 不存在不抛异常

s.pop()  # 随机删除一个 不指定参数

s.clear()  # 清空
