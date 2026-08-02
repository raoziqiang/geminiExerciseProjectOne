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