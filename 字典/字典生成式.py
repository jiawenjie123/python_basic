# 使用人：贾文杰
# 开发时间：2022/1/8 10:51
item=['fruit','books','others']
prices=[100,200,300,400,500]

d={item.upper():prices  for item,prices in zip(item,prices)}
print(d)