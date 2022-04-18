# 使用人：贾文杰
# 开发时间：2022/1/4 13:17

for i in 'python':
    print(i)

for r in range(10):
    print(r)

for _ in range(5):  # 循环次数
    print('q')

# 使用for循环求1到100的偶数和
sum = 0
for n in range(1, 101):
    if n % 2 == 0:
        sum = sum + n
print(sum)
# 输出100到999之间的水仙花数  个位三次方+十位三次方+百位三次方=数本身


for q in range(100, 1000):
    j = q % 10
    k =  q //10% 10
    l = q//100

    if j**3+k**3 +l**3 == q:
        print(q)
