# 使用人：贾文杰
# 开发时间：2022/1/14 16:27
#python支持多继承，必须在其构造函数中调用父类的构造函数
#一个类没有继承任何类，默认继承object类
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,taechofyear):
        super().__init__(name,age)
        self.teachofyear=taechofyear

stu=Student('张三',20,'20195805')
tea=Teacher('李四',34,10)

stu.info()
tea.info()
#多继承
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    pass