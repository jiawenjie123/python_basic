# 使用人：贾文杰
# 开发时间：2022/1/13 16:58
def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

lst=[10,29,34,23,44,53,55]
print(fun(lst))
#函数如果没有返回值，return可以不写
#函数返回值如果是一个，则返回原来的值，如果是多个，返回值则为元组
#函数在定义时是否需要返回值，视情况而定

