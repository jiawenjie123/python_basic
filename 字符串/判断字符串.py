# 使用人：贾文杰
# 开发时间：2022/1/12 9:49
s='hello,python'
#判断是否合法字符串
print('1',s.isidentifier())#F 合法的是字符数字下划线
#判断是否由空字符组成 回车 换行 水平制表符
print('2','\t'.isspace())
#字母
print('3','abc'.isalpha())
print('4','张三'.isalpha())
#十进制
print('5','123'.isdecimal())
#数字
print('6','123'.isnumeric())
print('7','123四'.isnumeric())
#字母和数字
print('8','张三abc1'.isalnum())

