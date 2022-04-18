# 使用人：贾文杰
# 开发时间：2022/1/8 9:28
#remove一次移除一个，只移除第一个
lst=[1,2,3,4,3,2,1]
lst.remove(2)
print(lst)
#根据索引pop不指定参数会删除最后一个
lst.pop(1)
print(lst)
#斜片
new_lst=lst[1:3]
print(new_lst)
lst[1:3]=[]
print(lst)
#清空列表
lst.clear()
print(lst)
#删除列表
del lst