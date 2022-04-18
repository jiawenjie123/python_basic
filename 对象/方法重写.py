# 使用人：贾文杰
# 开发时间：2022/1/14 16:39
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def info(self):
        super().info()
        print(self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, taechofyear):
        super().__init__(name, age)
        self.teachofyear = taechofyear

    def info(self):
        super().info()
        print(self.teachofyear)


stu = Student('张三', 20, '20195805')
tea = Teacher('李四', 34, 10)
stu.info()
tea.info()
