# 使用人：贾文杰
# 开发时间：2021/12/30 12:24
print(520)
print(98.5)
# 可以输出字符串
print('helloworld')
# 含有运算符的表达式
print(3 + 1)
# 数据输入到文件中 注意点 盘符存在 使用file=fp
fp = open('D:/text.text', 'a+')  # 如果文件不存在就创建，存在就在内容后面继续追加
print('helloworld', file=fp)
fp.close()

# 不换行
print('a', 'b', 'c')
