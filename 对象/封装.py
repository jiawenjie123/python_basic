# 使用人：贾文杰
# 开发时间：2022/1/14 16:15
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已经启动')

car=Car('宝马想x5')
car.start()
print(car.brand)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #不希望在外部被使用
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()

print(stu.name)
##print(stu.__age)

print(dir(stu))
print(stu._Student__age)#在类的外部可以通过_Student__age来实现