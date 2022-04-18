# 使用人：贾文杰
# 开发时间：2022/1/15 10:07
#该类实现了 ---特殊方法 ，称该类遵守了上下文管理器协议
#该类的实例对象就称为上下文管理器
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__被执行了')

    def show(self):
        print('show方法被执行了')

with MyContentMgr() as file:
    file.show()