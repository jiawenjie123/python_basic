# 使用人：贾文杰
# 开发时间：2021/12/30 12:53
print('hello\nworld')  # \n换行
print('hello\tworld')  # \t制表符
print('helloooo\tworld')  # 4位一个制表位
print('hello\rworld')  # 回车 覆盖了hello
print('hello\bworld')  # 退一格

print('http:\\\\www.baidu.com')
print('老师说’大家好‘')

# 原字符 不希望字符串中的转义字符起作用，就使用原字符，在字符串之前加上r R
print(r"hello\nworld")
# 注意事项 最后一个字符不能是反斜杠 两个可以(奇数不行)
print(r'hello\nworld\\')