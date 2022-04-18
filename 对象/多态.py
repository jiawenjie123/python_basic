# 使用人：贾文杰
# 开发时间：2022/1/14 16:50
class Animal:
    def eat(self):
        print('动物会吃')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person:
    def eat(self):
        print('人吃五谷杂粮')


def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())
print('-----------')
fun(Person())
