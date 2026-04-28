students = []
dictionary = {"name":"张三",
              "score":85}
students.append(dictionary)
students.append({"name":"李四",
                "score":92})
students.append({"name":"王五",
                "score":78})
# for s in students:
#     print(s["name"],s["score"])
#     print("学生：" + s["name"]+"  成绩: "+str(s["score"]))
#     print(f"学生：{s["name"]},成绩:{str(s["score"])}")
while True:
    print("\n===== 学生管理系统 =====")
    print("1.显示所有学生")
    print("2.增加学生")
    print("3.退出")
    print("4.删除学生")
    choice = input("请选择：")
    if choice == "1":
        for s in students:
            print(f"学生:{s["name"]},成绩：{s["score"]}")
    elif choice == "2":
        x = input("请输入添加的学生：")
        y = float(input("请输入该学生成绩："))
        students.append({"name":x,"score":y})
    elif choice == "3":
        print("感谢使用，再见")
        break
    elif choice == "4":
        name = input("请输入删除学生姓名：")
        # score = float(input("请输入删除学生成绩："))
        # students.remove({"name":name,"score":score})
        # print("已删除")
        for s in students:
           if s["name"] == name:
            students.remove(s)
            print("已删除")
            break
        else:
            print("没有此同学")
    else:
        print("错误选项")
        break