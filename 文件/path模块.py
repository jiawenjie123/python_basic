# 使用人：贾文杰
# 开发时间：2022/1/15 10:47
import os.path
print(os.path.abspath('with语句.py'))#获取绝对路径
print(os.path.exists('demo.py'))#判断文件存在
print(os.path.join('C:\\Users\\86130\\Desktop\\python\\python\\文件','with语句.py'))#拼接
print(os.path.split('C:\\Users\\86130\\Desktop\\python\\python\\文件\\with语句.py'))#文件名和扩展名分开
print(os.path.splitext('C:\\Users\\86130\\Desktop\\python\\python\\文件\\with语句.py'))
print(os.path.basename('C:\\Users\\86130\\Desktop\\python\\python\\文件\\with语句.py'))#目录中提取文件名
print(os.path.dirname('C:\\Users\\86130\\Desktop\\python\\python\\文件\\with语句.py'))#提取目录名
print(os.path.isdir('C:\\Users\\86130\\Desktop\\python\\python\\文件\\with语句.py'))#判断是否为路径

#列出指定目录下所有py文件
'''path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)'''

path=os.getcwd()
lst_files=os.walk(path)
for dirpath,dirname,filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('-----')