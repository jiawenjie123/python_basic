# 使用人：贾文杰
# 开发时间：2022/1/12 9:58
s='hello,python'
print(s.replace('python','java'))
s1='hello,python,python,python'
print(s1.replace('python','java',2))

lst=['hello','java','python']
print('|'.join(lst))

t=('hello','java','python')
print(''.join(t))

print('*'.join('python'))