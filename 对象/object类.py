# 使用人：贾文杰
# 开发时间：2022/1/14 16:43
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0},今年{1}岁'.format(self.name,self.age)

stu=Student('张三','20')
print(dir(stu))
print(stu)
