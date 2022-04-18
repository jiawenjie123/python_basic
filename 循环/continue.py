# 使用人：贾文杰
# 开发时间：2022/1/4 13:43
#输出1到50间所有5的倍数

for i in range(1,51):
    if i%5==0:
        print(i)

for j in range(1,50):
    if j%5!=0:
        continue
    print(j)