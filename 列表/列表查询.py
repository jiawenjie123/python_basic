# 使用人：贾文杰
# 开发时间：2022/1/8 9:06
lst =['hello','world',98,'hello']
#获取索引，如果有相同元素，只返回第一个
print(lst.index('hello'))
#print(lst.index('hello',1,3))#1到2
#获取列表中单个元素
print(lst[2])#0到n-1
print(lst[-2])#-n到-1
#切片
lst1 =[1,2,3,4,5,6,7,8]
print(lst1[1:6:1])
print(lst1[::-1])#逆序输出
#查询
print('hello' in lst)
#遍历
for i in lst:
    print(i)