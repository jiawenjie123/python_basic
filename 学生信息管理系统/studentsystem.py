# 使用人：贾文杰
# 开发时间：2022/1/15 11:15
import os.path

filename = 'student.txt'


# 主函数
def main():
    try:
        while True:
            menm()
            choice = int(input('请选择\n'))
            if choice in [1, 2, 3, 4, 5, 6, 7, 8]:
                if choice == 8:
                    answer = input('是否退出系统？y/n\n')
                    if answer == 'y':
                        print('谢谢使用')
                        break
                    else:
                        continue
                elif choice == 1:
                    insert()
                elif choice == 2:
                    search()
                elif choice == 3:
                    delete()
                elif choice == 4:
                    modify()
                elif choice == 5:
                    sort()
                elif choice == 6:
                    total()
                elif choice == 7:
                    show()
            else:
                print('输入有误')
    except BaseException as e:
        print('输入有误')
        print(e)
        main()


# 菜单
def menm():
    print('====================学生信息管理系统====================')
    print('-----------------------功能菜单------------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t8.退出系统')
    print('-----------------------------------------------------')


# 插入学生信息
def insert():
    student_list = []
    while True:
        id = input('请输入ID（如1001）\n')
        if not id:
            print('未输入id')
            continue
        name = input('请输入姓名:\n')
        if not name:
            print('未输入姓名')
            continue
        try:
            while True:
                english = float(input('请输入英语成绩:\n'))
                if english < 0:
                    print('输入有误，请重新输入')
                    continue
                elif english > 100:
                    print('输入有误，请重新输入')
                    continue
                else:
                    break

            while True:
                python = float(input('请输入python成绩:\n'))
                if python < 0:
                    print('输入有误，请重新输入')
                    continue
                elif python > 100:
                    print('输入有误，请重新输入')
                    continue
                else:
                    break

            while True:
                java = float(input('请输入java成绩:\n'))
                if java < 0:
                    print('输入有误，请重新输入')
                    continue
                elif java > 100:
                    print('输入有误，请重新输入')
                    continue
                else:
                    break

        except:
            print('输入无效,请重新输入')
            continue
        # 将学生信息保存到字典
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 学生信息加入列表
        student_list.append(student)
        answer = input('是否继续添加信息？y/n\n')
        if answer == 'y':
            continue
        else:
            break

    # 调用save函数
    save(student_list)
    print('学生信息录入完毕')


# 保存学生信息列表
def save(lst):
    try:
        stu_text = open(filename, 'a', encoding='utf-8')
    except:
        stu_text = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_text.write(str(item) + '\n')
    stu_text.close()


# 查询学生信息
def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = int(input('按id查找输入1,按name查找输入2\n'))
            if mode == 1:
                id = input('输入学生id')
            elif mode == 2:
                name = input('输入学生姓名')
            else:
                print('输入有误,请重新输入')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input('是否继续查询y/n\n')
            if answer == 'y':
                continue
            else:
                print('查询结束')
                break

        else:
            print('暂无学生信息')


# 显示查出的学生数据
def show_student(lst):
    if len(lst) == 0:
        print('未查到学生信息')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
    # 定义内容显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 float(float(item.get('english')) + float(item.get('python')) + float(item.get('java'))
                                       )))


# 删除学生信息
def delete():
    while True:
        student_id = input('请输入要删除学生的id:\n')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = True  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转为字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = False
                    if flag:
                        print(f'没有找到id为{student_id}的学生信息')

                    else:
                        print(f'id为{student_id}的学生信息被删除')
            else:
                print('无学生信息')
                break
            show()  # 删除后显示所有学生信息
            answer = input('是否继续删除y/n\n')
            if answer == 'y':
                continue
            else:
                print('删除操作完成')
                break


# 修改学生信息
def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入修改学生的id:\n')
    with open(filename, 'w', encoding='utf-8') as wfile:

        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以进行修改')
                while True:
                    try:
                        d['name'] = input('输入姓名')
                        d['english'] = input('输入英语成绩')
                        d['python'] = input('输入python成绩')
                        d['java'] = input('输入java成绩')
                    except:
                        print('输入有误')
                    else:
                        break

                wfile.write(str(d) + '\n')
                print('修改成功')
            else:
                wfile.write(str(d) + '\n')
            answer = input('是否继续修改？y/n\n')
            if answer == 'y':
                modify()

#成绩排序
def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students_list = rfile.readlines()
            student_new = []
            for item in students_list:
                d = dict(eval(item))
                student_new.append(d)

    else:
        print('暂未保存数据信息')
    asc_or_desc = input('输入0升序，输入1降序:\n')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('输入有误，请重新输入')
        sort()
    mode = input('输入1按英语排序，2按python排序，3按java排序，4按总成绩排序\n')
    if mode == '1':
        student_new.sort(key=lambda x: float(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: float(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: float(x['java']), reverse=asc_or_desc_bool)
    elif mode == '4':
        student_new.sort(key=lambda x: float(x['english'] + x['python'] + x['java']), reverse=asc_or_desc_bool)
    else:
        print('输入有误，请重新输入')
        sort()

    show_student(student_new)

    answer = input('是否继续排序y/n')
    if answer == 'y':
        sort()
    else:
        print('排序完成')


# 统计人数
def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据信息')


# 显示所有信息
def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)

    else:
        print('暂未保存数据信息')



if __name__ == '__main__':
    main()
