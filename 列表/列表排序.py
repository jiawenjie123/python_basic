# 使用人：贾文杰
# 开发时间：2022/1/8 9:37
lst=[1,4,3,10,5]
lst.sort()#默认升序
print(lst)

#指定关键字参数，降序排序
lst.sort(reverse=True)
print(lst)
#sort 不产生新的列表对象

#sorted 产生新的列表对象

new_lst=sorted(lst)
print(lst)
print(new_lst)
lst2=sorted(lst,reverse=True)
print(lst2)