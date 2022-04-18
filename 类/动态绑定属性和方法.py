# 使用人：贾文杰
# 开发时间：2022/1/14 15:23
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20)
stu2=Student('李四',30)

print('---stu2动态绑定性别属性---')
stu2.gender='女'
print(stu2.name,stu2.age,stu2.gender)

def show():
    print('函数')
stu1.show=show()
stu1.show
