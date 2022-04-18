# 使用人：贾文杰
# 开发时间：2022/1/8 11:46
s1={1,2,3,4,5}
s2={1,3,2,4,5}
print(s1==s2)
s3={1,2,3}
print(s3.issubset(s1))#子集

print(s1.issuperset(s3))#超集

print(s1.isdisjoint(s3))#无交集

