# 使用人：贾文杰
# 开发时间：2022/1/12 9:43
s='hello world python'
lst = s.split()#返回的是列表类型
print(lst)
s1 ='hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))#劈分次数
#从右侧开始分割
print(s.rsplit())
print(s1.rsplit(sep='|',maxsplit=1))