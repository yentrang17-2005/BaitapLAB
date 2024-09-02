# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 00:06:14 2024

@author: Admin
"""

day = int(input('Nhập ngày sinh: '))
month = int(input('Nhập tháng sinh: '))
year = int(input('Nhập năm sinh: '))
print('a. {:02}/{:01}/{:04}'.format(day,month,year))
year_short = year % 100
print('b. {:02}/{:01}/{:02}'.format(day,month,year_short))
print('c. {:04}/{:01}/{:02}'.format(year,month,day))
