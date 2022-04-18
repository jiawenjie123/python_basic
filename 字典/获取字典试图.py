# 使用人：贾文杰
# 开发时间：2022/1/8 10:43
scores={'张三':100,'李四':200,'王五':300}
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))

values=scores.values()
print(values)
print(type(values))
print(list(values))

items=scores.items()
print(items)
print(list(items))#转换后为元组

#遍历
for s  in  scores:
    print(s)