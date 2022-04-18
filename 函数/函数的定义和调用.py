# 使用人：贾文杰
# 开发时间：2022/1/13 16:29
def calc(a,b):#a,b 形式参数，形式参数是在函数定义处
    c=a+b
    return c

result=calc(10,20)# 10,20是实参
print(result)
#参数传递 位置实参，
# 关键字实参

res=calc(b=10,a=20)
print(res)