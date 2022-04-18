# 使用人：贾文杰
# 开发时间：2022/1/15 9:52
file=open('b.txt','r')
file.seek(2)
print(file.read())
print(file.tell())
file.close()

file1=open('c.txt','a')#先刷新后关闭
file1.write('hello')
file1.flush()
file1.write('world')
file1.close()
