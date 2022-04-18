# 使用人：贾文杰
# 开发时间：2022/1/8 9:21
#列表末尾加一个元素
lst=[1,2,3]
print(lst,id(lst))
lst.append(4)
print(lst,id(lst))
lst2=[5,6]
lst.append(lst2)
print(lst)
lst.extend(lst2)#增加多个元素
print(lst)
#在任意位置添加元素
lst.insert(1,10)
print(lst)
#在任意位置加多个元素(切完替换)
lst[1:]=lst2
print(lst)