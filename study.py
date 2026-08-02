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