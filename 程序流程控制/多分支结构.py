# 使用人：贾文杰
# 开发时间：2022/1/3 14:52
point = float(input('请输入成绩'))
if 90 < point <= 100:
    print('成绩为A')
elif 80 < point <= 90:
    print('成绩为B')
elif 70 < point <= 80:
    print('成绩为C')
elif 60 < point <= 70:
    print('成绩为D')
elif 0 < point <= 60:
    print('成绩为E')
else:
    print('成绩有误')
