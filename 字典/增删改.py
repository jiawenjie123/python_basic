# 使用人：贾文杰
# 开发时间：2022/1/8 10:39
scores={'张三':100,'李四':200,'王五':300}
print('张三' in scores)
del scores['张三']#删除指定的key value对
print(scores)
#scores.clear()清空
scores['陈留']=90
print(scores)
scores['陈留']=1
print(scores)
