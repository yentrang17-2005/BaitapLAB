# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:37:58 2024

@author: Admin
"""
print('Câu a.')
a = float(input('\tNhập số bất kì: '))
b = float(input('\tNhập số bất kì: '))
c = float(input('\tNhập số bất kì: '))
if a > b:
    tempt = a
    a = b 
    b = tempt
if a > c:
    tempt = a
    a = c
    c = tempt
if b > c:
    tempt = b
    b = c
    c = tempt
print('\tThứ tự tăng dần:',a,b,c)

print('\nCâu b.')
a1 = int(input("\tNhập vào số nguyên bất kì: "))
a1thanhchuoi= str(a1)
sapxepchuoi = ''.join(sorted(a1thanhchuoi))
print("Thứ tự tăng dần là:", sapxepchuoi)
