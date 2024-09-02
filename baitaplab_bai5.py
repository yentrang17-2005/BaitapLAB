# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:29:47 2024

@author: Admin
"""

giờ = int(input('Nhập giờ: '))
phút = int(input('Nhập phút: '))
giây = int(input('Nhập giây: '))
if giờ > 23 or phút > 60 or giây > 60:
    print('Nhập lại giờ, phút, giây.')
else: 
    print('{:02}:{:02}:{:02}'.format(giờ,phút,giây))
    print('Đổi ra giây:',giờ*3600 + phút*60 + giây)
    
