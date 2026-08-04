# day = "Monday" 3


# for循环遍历列表中的每个元素


from ast import While


colors = ["red", "green", "blue", "yellow", "purple", "orange",
          "pink", "brown", "black", "white"]  # 初始化一个包含若干颜色的列表
for color in colors:  # 遍历列表中的每个颜色
    print(f"{color}")  # 打印当前颜色
# 第二种输出方式
    print('color: ', color)
    # 两者的差别是什么


# 生成数字序列
print(list(range(5)))  # 生成从0到4的数字序列
print(list(range(2, 7)))  # 生成从2到6的数字序列
print(list(range(1, 10, 2)))  # 生成从1到9的奇数序列

for i in range(1, 10):  # 遍历从1到9的数字
    print(f"5 x {i} = {5*i}")  # 输出5*列表里面的每个数字

# 遍历字典
person = {"name": "Alice", "age": 30, "city": "New York"}  # 初始化一个包含个人信息的字典
for key, value in person.items():
    print(f"{key}: {value}")

#enumerate()函数可以同时获取索引和值
animals = ["cat", "dog", "rabbit", "hamster"]  # 初始化一个包含若干动物的列表
for index, animal in enumerate(animals):  # 遍历列表中的每个动物及其索引
    print(f"{index}: {animal}")  # 打印当前动物的索引和值   


#ZIP()函数可以将两个或多个可迭代对象打包成一个元组列表
names = ["Alice", "Bob", "Charlie"]  # 初始化一个包含若干名字的列表
scores = [85, 92, 78]  # 初始化一个包含若干分数的列表
names.append("david")  # 在原列表末尾添加一个元素
for name, score in zip(names, scores):  # 使用zip()函数将两个列表打包成元组列表
    print(f"{name}: {score}")  # 打印每个名字及其对应的分数
# 打包之后，生成的元组列表只包含对应索引位置的元素,且不可更改,不能增删改查

#  while循环
count = 1
while count <=5:
    print(f"第{count}次循环")
    count += 1#别忘了递增,否则死循环!

# while True + break 的用法

n=1
while True:
    print(f"n = {n}")
    n += 1
    if n>6:
        break

# break语句用于终止循环,当满足条件时跳出循环,否则会一直执行下去,造成死循环

# break 和coutinue的区别:
# break: 终止整个循环,跳出循环体,不再执行循环体内的代码,直接跳出循环
# continue: 终止本次循环,跳过循环体内剩余的代码,继续执行下一次循环,不会跳出循环
#break:提前结束整个循环
for i in range(1, 11):
    if i == 6:
        continue  # 如果是6,跳过本次循环,继续下一次循环
    print(f"{i}")  # 输出奇数
 #continue:跳过本次循环,继续下一次循环
for i in range(1, 11):
    if i % 3 == 0:
        continue  #如果是3的倍数,跳过本次循环,继续下一次循环    
    print(i)  

# for...else  else语句在for循环中使用,当for循环正常结束时(没有被break终止),会执行else语句块中的代码,如果for循环被break终止,则不会执行else语句块中的代码 
for i in range(3):
    print(i)
else:
    print("循环正常结束")  # 输出: 循环正常结束

#嵌套循环-九九乘法表
for i in range(1, 10):
    row = ""
    for j in range(1, i + 1):
        row += f"{j} x {i} ={i*j:2d}   "#格式化输出,每个乘积占2个字符宽度,右对齐,每个算式之间加两个空格
    print(row)  # 每一行结束后换行


for i in range(1, 10):
    formulas = []

    for j in range(1, i + 1):
        formulas.append(f"{j} x {i} = {i * j:2d}")

    print("    ".join(formulas))


#1.fizzbuzz问题:打印1-30之间的数字,如果是3的倍数打印fizz,如果是5的倍数打印buzz,如果是3和5的倍数打印fizzbuzz,否则打印数字本身
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)


#2.求和问题:计算1-100之间所有整数的和
s=0
for i in range(1, 101):
    s += i
print(f"100内整数和: {s}")


#3.斐波那契数列:前两项为1,后面的每一项都是前两项之和 用while循环实现前20个(完全不懂)
a, b = 0, 1# 初始化斐波那契数列的前两项
count = 0# 用于记录已经生成的斐波那契数列的项数
total = 0# 用于存储斐波那契数列的和
n = 20  # 要计算的斐波那契数列的项数
while count < n:
    total += a# 累加当前项到总和
    a, b = b, a + b# 更新斐波那契数列的下一项
    count += 1# 计数器加1,表示已经生成了一项
print(f"前{n}个斐波那契数列的和: {total}")


#4.猜数字游戏
import random#导入random模块,用于生成随机数
random.randint(1, 20)# 生成一个1-20之间的随机整数
while True:
    guess = int(input("请输入一个1-20之间的数字: "))# 获取用户输入的数字,并将其转换为整数
    if guess == random.randint(1, 20):
        print("恭喜你,猜对了!")
        break
    else:
        print("猜错了,请再试一次.")