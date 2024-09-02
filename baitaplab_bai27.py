# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:53:58 2024

@author: Admin
"""
import math
print('hình vuông = v')
print('hình tròn = t')
print('hình chữ nhật = n')
B = str(input('\nChọn một hình (v, t, n): '))
if B == "n":
    print('Tính P và S của hình chữ nhật')
    a = float(input('Nhập chiều dài: '))
    b = float(input('Nhập chiều rộng: '))
    print('Kết quả là: P = ',(a+b)*2,'\tS =', a*b)

if B == "t":
    print('Tính P và S của hình tròn')
    c = float(input('Nhập bán kính hình tròn: '))
    print('Kết quả là: \nP = ',2*c*math.pi,'\nS =', c*c*math.pi) 

if B == "v":
    print('Tính P và S của hình vuông')
    d = float(input('Nhập cạnh hình vuông: '))
    print('Kết quả là: P = ',d*4,'\tS =', d*d)
    


          