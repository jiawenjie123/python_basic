# 使用人：贾文杰
# 开发时间：2022/1/15 9:44
file=open('a.txt','r')
#print(file.read())
#print(file.readline())
print(file.readlines())
file.close()

file1=open('b.txt','w')
#file1.write('hello')
lst=['java','go']
file1.writelines(lst)
file1.close()