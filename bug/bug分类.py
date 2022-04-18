# 使用人：贾文杰
# 开发时间：2022/1/14 9:51
# 语法错误
# 变量类型错误 ，中文输入法， 判断相等== 而不是=， 漏了：， 缩进错误 ，没有定义变量
# 知识点错误
# 索引越界 ，  方法使用错误
# 思路不清
# 解决方法 1使用print函数 2使用#暂时注释部分代码
lst = [{'rating': [9.7, 2062397], 'id': '1292052', 'type': ['犯罪', '剧情'], 'title': '肖申克的救赎', 'actors': ['蒂姆', '摩根']},
       {'rating': [9.6, 2162397], 'id': '1392052', 'type': ['犯罪', '爱情'], 'title': '霸王别姬', 'actors': ['张国荣', '张丰毅']},
       {'rating': [9.4, 2262397], 'id': '1492052', 'type': ['剧情', '爱情'], 'title': '阿甘正传', 'actors': ['汤姆', '罗宾']}
       ]
name = input('演员名')
for item in lst:  # 遍历列表得到{}
    act_lst = item['actors']
    # print(act_lst)
    for actor in act_lst:
        if name in actor:
            print(name + '出演了' + item['title'])

    '''for movie in item:#遍历字典 得到字典中的键
       print(movie)
        actors=movie['actors']

        if name in actors:
            print(name+'出演了'+movie)'''
# 操作者错误使用
try:
    a = int(input('1:'))
    b = int(input('2:'))
    print(a / b)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('只能输入数字')
except  BaseException as e:
    print(e)
