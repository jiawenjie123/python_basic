# 使用人：贾文杰
# 开发时间：2022/1/4 14:13
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            break
        print(j)

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()