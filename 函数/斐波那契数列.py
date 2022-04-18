# 使用人：贾文杰
# 开发时间：2022/1/14 9:42
#1 1 2 3 5
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(20))

for i in range(1,7):
    print(fib(i))
