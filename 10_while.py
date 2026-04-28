#求平均值的计算器
total = 0
count = 0
n = input("请输入数字：")
while n != "q":
    num = float(n)
    total += num
    count += 1
    n = input("请输入数字：")
if count == 0 :
    result = 0
else:
    result = total/count
print(f"你输入的数字平均值为:{result}")