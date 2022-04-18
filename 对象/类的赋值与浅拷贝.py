# 使用人：贾文杰
# 开发时间：2022/1/14 20:32
class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu1 = Cpu()
cpu2 = cpu1
print(cpu1)
print(cpu2)

# 类的浅拷贝
print('---------------')
disk = Disk()
computer = Computer(cpu1, disk)
# 开始浅拷贝
import copy

computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

#深拷贝
computer3=copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)


