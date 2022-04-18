# 使用人：贾文杰
# 开发时间：2022/1/15 10:17
#os 模块与操作系统相关的模块
import os
os.system('notepad.exe')
os.system('calc.exe')
#直接调用可执行文件
os.startfile('C:\Program Files (x86)\Tencent\QQ\Bin\qq.exe')
#返回当前工作目录
print(os.getcwd())
#返回指定目录下的文件和目录信息
lst=os.listdir('../文件')
print(lst)
#创建目录
#os.mkdir('new')
#os.makedirs('A/B/C')
#多级目录
#删除目录
#os.rmdir('new')
#删除多级目录
#os.removedirs('A/B/C')
#将path设为当前工作目录
os.chdir('C:\\Users\\86130\\Desktop\\python\\python\\文件')
print(os.getcwd())
