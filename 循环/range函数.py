# 使用人：贾文杰
# 开发时间：2022/1/4 8:18
# 用于生成一个整数序列
r = range(10)
print(r)
print(list(r))  # 查看range对象中的整数序列
# range(stop) 默认从0开始 步长为1 到stop结束（不包含）

s = range(1, 10)
print(list(s))
# range(start,stop)

m = range(0, 10, 2)
print(list(m))
# range(start,stop,step)
print(1 in m)
print(2 not in m)


