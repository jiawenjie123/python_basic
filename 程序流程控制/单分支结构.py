# 使用人：贾文杰
# 开发时间：2022/1/3 14:45
money=1000
s=int(input('输入取款金额'))
#判断
if money>=s:
    money=money-s
    print('取款成功，余额为',money)
