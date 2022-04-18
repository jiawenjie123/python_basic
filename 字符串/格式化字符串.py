# 使用人：贾文杰
# 开发时间：2022/1/12 10:36
#%号做占位符
name='张三'
age=20
print('我叫%s,今年%d岁'%(name,age))
#{}
print('我叫{0},今年{1}岁'.format(name,age))
#f-string
print(f'我叫{name},今年{age}岁')

print('%10d'%99)#10为宽度
print('%10.3f'%3.1415926)#.3为小数点后三位

print('{0:.3}'.format(3.1415926))#.3是总共三位
print('{0:10.3f}'.format(3.1415926))