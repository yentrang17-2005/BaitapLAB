# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:18:03 2024

@author: Admin
"""
print('Câu a.')
a = int(input('Nhập giờ: '))
b = int(input('Nhập phút: '))
c = int(input('Nhập giây: '))
if a > 23 or b > 60 or c > 60:
    print('Không hợp lệ')
else:
    print('{:02}:{:02}:{:02}'.format(a,b,c))