# 使用人：贾文杰
# 开发时间：2022/1/14 15:05
class Student:#类名由一个或多个单词构成，每个单词首字母大写。其余小写
    native_place='江苏'#直接写在类里的变量，类属性
    def __init__(self,name,age):
        self.name=name#self.name为实体属性，进行了一个赋值操作，将局部变量的值付给实体属性
        self.age=age
    #实例方法 类外定义的为函数 类内的是方法
    def eat(self):
        print('学生在吃饭')
    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod方法')

    @classmethod
    def cm(cls):
        print('我是类方法')

#创建对象
stu1=Student('张三',20)
stu2=Student('李四',30)
stu1.eat()
print(stu1.name)
print(stu1.age)

Student.eat(stu1)

#类属性调用
print(Student.native_place)
print(stu1.native_place)
Student.native_place='天津'
print(stu1.native_place)
stu1.native_place='上海'
print(Student.native_place)
print(stu2.native_place)

#类方法 使用类名直接访问
print('----------')
Student.cm()

#静态方法 使用类名直接访问
print('----------')
Student.method()
