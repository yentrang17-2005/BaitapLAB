# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:16:17 2024

@author: Admin
"""
h1 = int(input('Nhập giờ: '))
m1 = int(input('Nhập phút: '))
s1 = int(input('Nhập giây: '))
print('Thời điểm 1: {:02} giờ {:02} phút {:02} giây'.format(h1,m1,s1))


h2 = int(input('Nhập giờ: '))
m2 = int(input('Nhập phút: '))
s2 = int(input('Nhập giây: '))
print('Thời điểm 2: {:02} giờ {:02} phút {:02} giây'.format(h2,m2,s2))

sum_sec = s1 + s2
sum_min = m1 + m2 + sum_sec//60 
sum_hour = h1 + h2 + sum_min//60  
tong_giay = sum_sec%60
tong_phut = sum_min%60
print('Cộng 2 giờ này: {} giờ {} phút {} giây.'.format(sum_hour,tong_phut,tong_giay))


a = h1*3600 + m1*60 + s1
b = h2*3600 + m2*60 + s2
c = abs(a - b)
hieu_giay = c % 60
hieu_phut = (c % 3600)//60
hieu_gio  = c // 3600
print('Trừ 2 giờ này: {} giờ {} phút {} giây.'.format(hieu_gio,hieu_phut,hieu_giay))
