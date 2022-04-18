# 使用人：贾文杰
# 开发时间：2022/1/3 14:37

# False 0 none ’ ‘  “” 布尔值都是false
print(bool([]))  # 空列表
print(bool(list()))  # 空列表
print(bool(()))  # 空元组
print(bool(tuple()))
print(bool({}))  # 空字典
print(bool(dict()))
print(bool(set()))  # 空集合

# 除以上的其他的布尔值均为true

age=int(input('输入年龄'))
if age:
    print(age)
else:
    print('年龄为',age)