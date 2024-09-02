# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 00:23:04 2024

@author: Admin
"""

hour = int(input('Nhập giờ: '))
min = int(input('Nhập phút: '))
sec = int(input('Nhập giây: '))
if hour > 23 or min > 60 or sec > 60:
    print('Nhập lại giờ, phút, giây.')
else:
    print('{}h{}p{}s'.format(hour,min,sec))
    print('Đổi ra giây:',hour*3600 + min*60 + sec)
    