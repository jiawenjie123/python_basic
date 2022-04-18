# 使用人：贾文杰
# 开发时间：2022/1/15 9:30
file=open('a.txt','r')
print(file.readlines())
file.close()
#readlines结果是列表

#常用文件打开模式
file1=open('b.txt','w')
file1.write('python')
file1.close()

file1=open('b.txt','a')#追加
file1.write('python')
file1.close()
#b以二进制的方式打开文件，不能单独使用
scr_file=open('0B4SZPK3XORFZP69.jpg','rb')
target_file=open('copy.jpg','wb')

target_file.write(scr_file.read())
scr_file.close()

