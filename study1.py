#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author:raoziqiang
# time:2026-7-30
# description: This script is written by raoziqiang on 2026-7-30
# usage: python3 script.py
# notes: Add any additional notes or comments about the script here
# aim study using python programming develop skills and agent development
# print("Hello, world!")
# print('are you ok?')
# print('i\'m your "father"')
# print(r"we' 'are' 'the' 'champions'")
# print(r'''hello,\n
# world''')
# print(
# '''line1
#    line2
#        line3     ''')
# 集合 ,列表, 元组, 字典的相关知识
5 > 3 and 3 > 1
print(5 > 3 and 3 > 1)
# int age ; 动态变量不需要先定义类型
age = input("Please enter your age: ")
age = int(age)
if age >= 18 & age < 100:
    print('adult')
else:
    print('teenager')

n = 123
f = 456.789  # F-string格式化字符串
s1 = "hello, world"
s2 = 'hello, \'adam\''
s3 = r'hello, "world"'
s4 = '''hello,
Bob!'''
# print(?)


# List:有序,可变的集合
fruit = ['apple', 'banana', 'cherry', 'orange']
print("Original List:", fruit)  # {'apple', 'banana', 'cherry', 'orange'}
# 索引访问(从0开始,负数表示从末尾开始计数)
print("last element:", fruit[-1])  # orange
print("first element:", fruit[0])  # apple

# 切片[起始:结束:步长]，不包含结束位置-左闭右开
print("slice:", fruit[1:3])  # ['banana', 'cherry']
print("slice with step:", fruit[::2])  # ['apple', 'cherry']
print("slice with negative step:", fruit[::-2])  # ['orange',  'banana']
print("slice last two:", fruit[-2:])  # ['cherry', 'orange']

# 增删改查
fruit.append('pear')  # 增加元素-末尾添加
fruit.insert(1, 'grape')  # 增加元素-指定位置添加
fruit.remove('banana')  # 删除元素-按值删除
# 待我抽支烟,有点困
popped_fruit = fruit.pop()  # 弹出末尾元素
print("操作后:", fruit)  # ['apple', 'grape', 'cherry']
print("弹出的元素:", popped_fruit)  # pear


# 常用操作
print("长度:", len(fruit))  # 输出list长度: 3
print("是否存在:", 'apple' in fruit)  # 判断元素是否存在: True
fruit.sort()  # 排序
print("排序后:", fruit)  # ['apple', 'cherry', 'grape', 'orange']

# 列表推导式(Python特色)
squares = [x**2 for x in range(1, 6)]  # 生成1-5的平方数列表
print("平方数列表:",)


even_squares = [x for x in range(10) if x % 2 == 0]  # 生成1-10的偶数平方数列表
print("偶数平方数列表:", even_squares)  # 输出: [0, 2, 4, 6, 8]
evens = [x for x in range(10) if x % 2 == 0]  # 生成0-9的偶数列表
print("0~9的偶数:", evens)  # 输出: [0, 2, 4, 6, 8]


# ---------- 2. 元组 (tuple) ----------
# 元组:有序,不可变的集合,用()表示,元素之间用逗号分隔
point = (3, 5)  # 二维坐标
rgb = (255, 128, 0)  # RGB颜色值
print("\n坐标:", point, "颜色:", rgb)  # 输出: 坐标: (3, 5) 颜色: (255, 128, 0)
# 解包(unpacking)
x, y = point
r, g, b = rgb
print(f"x={x}, y={y}, r={r}, g={g}, b={b}")  # 输出: x=3, y=5, r=255, g=128, b=0


# 元组不可修改,但可以"重新赋值"
# point[0] = 10 #会报错,因为元组不可变
point = (10, 5)  # 重新赋值,定义整个元组

# 单元素元组注意逗号!
single = (42,)  # 这是元组
not_tuple = (42)  # 这是整数,不是元组
print("单元素元组:", single, type(single))
print("不是元组:", not_tuple, type(not_tuple))

# ---------- 3. 字典 (dict) ----------
# 字典:无序,可变的集合,用{}表示,键值对{Key: Value}表示,键必须是不可变类型(如字符串,数字,元组),值可以是任意类型
student = {'name': 'Alice',
           'age': 20,
           'score': [85, 92, 78],
           'major': 'Computer Science',
           'is passed': True
           }

# 输出: 学生信息: {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}
print("\n学生信息:", student)

# 访问字典元素
print("姓名:", student['name'])  # 输出: 姓名: Alice
print("年龄:", student.get('age'))  # 输出: 年龄: 20
print("成绩:", student['score'])  # 输出: 成绩: [85, 92, 78]
print("专业:", student['major'])  # 输出: 专业: Computer Science
print("是否及格:", student['is passed'])  # 输出: 是否及格: True
print("电话:", student.get('phone', '无'))  # 输出: 电话: N/A,使用get方法获取键值,如果键不存在则返回默认值

# 增删改查
student['phone'] = '123-456-7890'  # 增加键值对
student['age'] = 21  # 修改键值对
removed_value = student.pop('score')  # 删除键值对,返回被删除的值
# 输出: 操作后: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'is passed': True, 'phone': '123-456-7890'}
print("操作后:", student)
print("被删除的成绩:", removed_value)  # 输出: 被删除的成绩: [85, 92, 78]


# 遍历
# 输出: 遍历键 ['name', 'age', 'major', 'is passed', 'phone']
print("遍历键", list(student.keys()))
# 输出: 遍历值 ['Alice', 21, 'Computer Science', True, '123-456-7890']
print("遍历值", list(student.values()))
for key, value in student.items():
    # 输出: name: Alice, age: 21, major: Computer Science, is passed: True, phone: 123-456-7890
    print(f" {key} -> {value}")


# 字典推导式(Python特色)
word_lengths = {word: len(word) for word in ['hello', 'world', 'python']}
# 输出: 单词长度字典: {'hello': 5, 'world': 5, 'python': 6}
print("单词长度映射:", word_lengths)

# ---------- 4. 集合 (set) ----------
# 集合:无序,可变的集合,用{}或者set()表示,Set()创建的集合是空集合,元素唯一且不可变,适合用于去重和集合运算
# set()方法
# set() = {1, 2, 3, 4, 5}错误示范
# set() = {4, 5, 6, 7, 8} 错误示范
# a = set()创建空集合
# b = set()创建空集合
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("集合a:", a, "集合b:", b)  # 输出: 集合a: {1, 2, 3, 4, 5} 集合b: {4, 5, 6, 7, 8}
# 集合运算
print("交集AnB输出:", a & b)  # 输出: 交集: {4, 5}
print("并集AUB输出:", a | b)  # 输出: 并集: {1, 2, 3, 4, 5, 6, 7, 8}
print("差集A-B输出:", a - b)  # 输出: 差集: {1, 2, 3}
print("对称差 A▲B输出:", a ^ b)  # 输出: 对称差: {1, 2, 3, 6, 7, 8}#对称差就是指并集减去交集的集合

# 去重--集合的一个重要特性就是元素唯一,可以用来去重,集合的经典用法就是去重,比如有一个列表,里面有重复的元素,我们可以用集合来去重
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
unique = list(set(numbers))
print("去重后的列表:", unique)  # 输出: 去重后的列表: [1, 2, 3, 4, 5]

# 添加和删除
a.add(99)  # 添加元素
a.discard(1)  # 安全删除元素,如果元素不存在不会报错
# a.remove(2)  # 删除元素,如果元素不存在会报错
print("操作后的A:", a)  # 输出: 操作后的A: {2, 3, 4, 5, 99}


# 综合练习
print("\n综合练习:"+"="*40)
print("综合练习: 统计文本中的词频")
print("="*40)

text = "apple banana apple orange banana apple grape orange orange"
words = text.split()  # 按空格分割成列表
# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
# print("词频统计结果:", word_count)
print("单词列表:", words)


# 用字典统计词频
word_count = {}  # 初始化一个空字典用于存储词频统计结果
for word in words:  # 遍历单词列表
    # 使用字典的get方法获取当前单词的计数，如果不存在则返回0，然后加1
    word_count[word] = word_count.get(word, 0) + 1
# 输出: 词频统计结果: {'apple': 3, 'banana': 2, 'orange': 3, 'grape': 1}
print("词频统计结果:", word_count)


# 找出出现最多的词
most_common = max(word_count, key=word_count.get)
# 输出: 出现最多的词: 'apple'(3次)
print(f"出现最多的词: '{most_common}'({word_count[most_common]}次)")

# example1: 找出最大值和最小值
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 11]  # 初始化一个包含若干整数的列表
for num in numbers:  # 遍历列表中的每个数字
    if num > num:  # 如果当前数字大于当前最大值
        num = num
        print(num)  # 更新最大值为当前数字
    else:
        print(num)  # 否则保持当前最大值不变
    if num < num:  # 如果当前数字小于当前最小值
        num = num
        print(num)  # 更新最小值为当前数字
    else:
        print('0')  # 否则保持当前最小值不变
num = [num > num for num in numbers]  # 使用列表推导式生成一个布尔列表，表示每个数字是否大于当前最大值
print(num)  # 输出布尔列表
num = [num < num for num in numbers]  # 使用列表推导式生成一个布尔列表，表示每个数字是否小于当前最小值
print(num)  # 输出布尔列表


# example2:使用字典存储你一周的课程表
class_list = {
    'Monday': ['Math', 'English', 'Physics'],
    'Tuesday': ['Chemistry', 'Biology', 'History'],
    'Wednesday': ['Math', 'Computer Science', 'Physical Education'],
    'Thursday': ['English', 'Geography', 'Art'],
    'Friday': ['Math', 'English', 'Music'],
    'Saturday': ['Optional Class'],
    'Sunday': []
}
# 输出: 课程表: {'Monday': ['Math', 'English', 'Physics'], 'Tuesday': ['Chemistry', 'Biology', 'History'], 'Wednesday': ['Math', 'Computer Science', 'Physical Education'], 'Thursday': ['English', 'Geography', 'Art'], 'Friday': ['Math', 'English', 'Music'], 'Saturday': ['Optional Class'], 'Sunday': []}
print("课程表:", class_list)


# example3:有两个列表,用集合找出只在第一个列表中出现的值
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
unique_to_list1 = list(set(list1) - set(list2))  # 使用了差集用列表1减去列表2,得到只在列表1中出现的值
print("只在第一个列表中出现的值:", unique_to_list1)  # 输出: 只在第一个列表中出现的值: [1, 2, 3]
