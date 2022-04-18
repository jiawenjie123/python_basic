# 使用人：贾文杰
# 开发时间：2022/1/12 9:36
s='hello,python'
print(s.center(20,'*'))#居中对齐 不够20的用*填充
print(s.ljust(20,'*'))#左对齐
print(s.rjust(20,'*'))#右对齐
print(s.zfill(20))#右对齐，左边用0
#不够就返回原字符串
