#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author:raoziqiang
# time:2026-7-30
# description: This script is written by raoziqiang on 2026-7-30
# usage: python3 script.py
# notes: Add any additional notes or comments about the script here
# aim study using python programming develop skills and agent development
#print("Hello, world!")
#print('are you ok?')
#print('i\'m your "father"')
#print(r"we' 'are' 'the' 'champions'")
#print(r'''hello,\n
#world''')
#print(
#'''line1
#    line2
#        line3     ''')

5 > 3 and 3 > 1
print(5 > 3 and 3 > 1)
# int age ; 动态变量不需要先定义类型
age = input ("Please enter your age: ")
age = int(age)
if age >= 18&age < 100:
    print('adult')
else:
    print('teenager')

n = 123
f = 456.789
s1 = "hello, world"
s2 = 'hello, \'adam\''
s3 = r'hello, "world"'
s4 = '''hello,
Bob!'''
# print(?)


# List:有序,可变的集合
fruit = ['apple', 'banana', 'cherry','orange']
print("Original List:", fruit) #{'apple', 'banana', 'cherry', 'orange'}
# 索引访问(从0开始,负数表示从末尾开始计数)
print("last element:", fruit[-1]) #orange
print("first element:", fruit[0]) #apple

# 切片[起始:结束:步长]，不包含结束位置-左闭右开
print("slice:", fruit[1:3]) #['banana', 'cherry']
print("slice with step:", fruit[::2]) #['apple', 'cherry']
print("slice with negative step:", fruit[::-2]) #['orange',  'banana']
print("slice last two:", fruit[-2:]) #['cherry', 'orange']

#增删改查
fruit.append('pear') #增加元素-末尾添加
fruit.insert(1, 'grape') #增加元素-指定位置添加
fruit.remove('banana') #删除元素-按值删除
#待我抽支烟,有点困
popped_fruit = fruit.pop() #弹出末尾元素
print("操作后:", fruit) #['apple', 'grape', 'cherry']
print("弹出的元素:", popped_fruit) #pear


# 常用操作
print("长度:", len(fruit)) #输出list长度: 3
print("是否存在:", 'apple' in fruit) #判断元素是否存在: True
fruit.sort() #排序
print("排序后:", fruit) #['apple', 'cherry', 'grape', 'orange']

# 列表推导式(Python特色)
squares = [x**2 for x in range(1,6)] #生成1-5的平方数列表
print("平方数列表:",)


even_squares = [x for x in range(10) if x % 2 == 0] #生成1-10的偶数平方数列表
print("偶数平方数列表:", even_squares) #输出: [0, 2, 4, 6, 8]
evens = [x for x in range(10) if x % 2 == 0] #生成0-9的偶数列表
print("0~9的偶数:", evens) #输出: [0, 2, 4, 6, 8]


# ---------- 2. 元组 (tuple) ----------
#元组:有序,不可变的集合,用()表示,元素之间用逗号分隔
point = (3,5)   #二维坐标
rgb = (255,128,0) #RGB颜色值
print("\n坐标:", point,"颜色:", rgb) #输出: 坐标: (3, 5) 颜色: (255, 128, 0)
# 解包(unpacking)
x, y = point
r, g, b = rgb
print(f"x={x}, y={y}, r={r}, g={g}, b={b}") #输出: x=3, y=5, r=255, g=128, b=0


# 元组不可修改,但可以"重新赋值"
# point[0] = 10 #会报错,因为元组不可变
point = (10, 5) #重新赋值,定义整个元组

#单元素元组注意逗号!
single = (42,)  #这是元组
not_tuple = (42)  #这是整数,不是元组
print("单元素元组:", single, type(single))
print("不是元组:", not_tuple, type(not_tuple))

# ---------- 3. 字典 (dict) ----------
#字典:无序,可变的集合,用{}表示,键值对{Key: Value}表示,键必须是不可变类型(如字符串,数字,元组),值可以是任意类型
student = {'name': 'Alice', 
           'age': 20, 
           'score': [85,92,78],
           'major': 'Computer Science',
           'is passed': True
           }

print("\n学生信息:", student) #输出: 学生信息: {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}

#访问字典元素
print("姓名:", student['name']) #输出: 姓名: Alice
print("年龄:", student.get('age')) #输出: 年龄: 20
print("成绩:", student['score']) #输出: 成绩: [85, 92, 78]
print("专业:", student['major']) #输出: 专业: Computer Science
print("是否及格:", student['is passed']) #输出: 是否及格: True
print("电话:", student.get('phone', '无')) #输出: 电话: N/A,使用get方法获取键值,如果键不存在则返回默认值

#增删改查
student['phone'] = '123-456-7890' #增加键值对
student['age'] = 21 #修改键值对
removed_value = student.pop('score') #删除键值对,返回被删除的值
print("操作后:", student) #输出: 操作后: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'is passed': True, 'phone': '123-456-7890'}
print("被删除的成绩:", removed_value) #输出: 被删除的成绩: [85, 92, 78]


# 遍历
print("遍历键", list(student.keys())) #输出: 遍历键 ['name', 'age', 'major', 'is passed', 'phone']
print("遍历值", list(student.values())) #输出: 遍历值 ['Alice', 21, 'Computer Science', True, '123-456-7890']
for key, value in student.items():
    print(f" {key} -> {value}") #输出: name: Alice, age: 21, major: Computer Science, is passed: True, phone: 123-456-7890


#字典推导式(Python特色)
word_lengths = {word: len(word) for word in ['hello', 'world', 'python']}
print("单词长度映射:", word_lengths) #输出: 单词长度字典: {'hello': 5, 'world': 5, 'python': 6}

# ---------- 4. 集合 (set) ----------
#集合:无序,可变的集合,用{}或者set()表示,元素唯一且不可变,适合用于去重和集合运算
