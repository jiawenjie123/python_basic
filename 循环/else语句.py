# 使用人：贾文杰
# 开发时间：2022/1/4 13:49
for i in range(3):
    pwd=input('输入密码\n')
    if pwd=='888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('三次密码均错误')


a=0
while a<3:
    p=input('输入密码\n')
    if p=='000000':
        print('密码正确')
        break
    else:
        print('密码错误')
    a+=1
else:
    print('三次均错误')