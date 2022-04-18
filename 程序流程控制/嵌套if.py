# 使用人：贾文杰
# 开发时间：2022/1/3 15:00
'''会员>=200 8折
      >=100 9折
      不打折
    非会员>200 9.5折
       不打折'''
answer=input('您是会员吗？y/n\n')
m=float(input('输入购物金额\n'))
if answer=='y':
    if m>=200:
        print('付款金额为',0.8*m)
    elif m>=100:
        print('付款金额为',0.9*m)
    else:
        print('付款金额为',m)
else:
    if m>=200:
        print('付款金额为',0.9*m)
    else:
        print('付款金额为',m)
