# 使用人：贾文杰
# 开发时间：2022/1/3 15:24

a = int(input('输入第一个整数\n'))
b = int(input('请输入第二个整数\n'))
if a >= b:
    print(a, '大于等于', b)
else:
    print(a, '小于等于', b)

# 用条件表达式
#条件判断为true 则执行左边

print(str(a) + '大于等于' + str(b) if a >= b else str(a) + '小于' + str(b))
