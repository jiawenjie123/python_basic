# 使用人：贾文杰
# 开发时间：2022/1/14 17:35
class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


x = C('jack', 20)
print(x.__dict__)  # 查看实例对象的属性字典
print(C.__dict__)
print(x.__class__)  # 输出了对象所属的类
print(C.__bases__)  # C类的父亲类型的元素
print(C.__base__)
print(C.__mro__)  # 类的层次结构
print(A.__subclasses__())  # 子类的列表

print('---------------')
a = 20
b = 100
d = a.__add__(b)
print(d)


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student('张三')
stu2 = Student('李四')
s = stu1 + stu2
print(s)
s1 = stu1.__add__(stu2)
print(s1)
print('----------------')
lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())
print(len(stu1))
print('----------------')
