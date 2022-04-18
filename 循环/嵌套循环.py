# 使用人：贾文杰
# 开发时间：2022/1/4 13:53
from idlelib.multicall import s

for i in  range(3):
    for j in range(4):
        print('*',end='\t')
    print()

for m in  range(1,10):
    for n in range(1,m+1):
        print(m,'*',n,'=',m*n,end='\t')
    print()
