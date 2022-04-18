# 使用人：贾文杰
# 开发时间：2022/1/15 10:04
print(type(open('a.txt','r')))

with open('a.txt','r') as file:
    print(file.read())

with open('0B4SZPK3XORFZP69.jpg','rb') as scr_file:
    with open('copy2.jpg','wb') as  taget_file:
        taget_file.write(scr_file.read())