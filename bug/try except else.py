# 使用人：贾文杰
# 开发时间：2022/1/14 10:35
try:
    a = int(input('1:'))
    b = int(input('2:'))
    result = a / b


except  BaseException as e:
    print('出错了')
    print(e)
else:
    print('结果为,', result)
finally:
    print('无论是否异常，总会被执行的代码')  # 通常用于释放try块中申请的资源 例如数据库连接
