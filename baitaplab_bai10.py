# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:06:20 2024

@author: Admin
"""

a = str(input('Nhập số xe của bạn (gồm 4 chữ số): '))
b = int(a)
so_nut = b//1000 + (b%1000)//100 + (b%100)//10 + b%10
if len(a) == 4:
    print('Số xe của bạn được',so_nut%10,'nút.')
else:
    print('Nhập lại số xe của bạn.')
    
    
    