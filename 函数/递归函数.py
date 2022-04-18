# 使用人：贾文杰
# 开发时间：2022/1/14 9:38
#函数的函数体内调用了自己本身
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(6))