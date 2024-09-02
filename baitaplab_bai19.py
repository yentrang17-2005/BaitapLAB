# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:22:15 2024

@author: Admin
"""

a = int(input('Nhập số nguyên thứ nhất: '))
b = int(input('Nhập số nguyên thứ hai: '))
c = int(input('Nhập số nguyên thứ ba: '))
d = int(input('Nhập số nguyên thứ tư: '))

if a < b and a < c and a < d:
    print('Giá trị nhỏ nhất là: ',a)
elif b < a and b < c and b < d:
    print('Giá trị nhỏ nhất là: ',b)
elif c < a and c < b and c < d:
    print('Giá trị nhỏ nhất là: ',c)
else:
    print('Giá trị nhỏ nhất là: ',d)
    
    
