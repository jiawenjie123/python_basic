# 使用人：贾文杰
# 开发时间：2022/1/8 10:34
scores={'张三':100,'李四':200,'王五':300}

print(scores['张三'])
#print(scores['陈三'])
print(scores.get('张三'))
print(scores.get('陈三'))
print(scores.get('钱七',99))
