# 使用人：贾文杰
# 开发时间：2022/1/12 10:16
#字符串不可变类型 不能增删改
#切片将产生新的对象
s='hello,python'
s1=s[:5]
s2=s[6:]
s3='!'
s4=s1+s2+s3
print(s4)
#切片[start,end,step]
print(s[-6::1])