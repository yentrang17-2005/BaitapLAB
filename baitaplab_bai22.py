# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:20:33 2024

@author: Admin
"""

a = float(input("Nhập giá trị của a:"))
b = float(input("Nhập giá trị của b:"))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    if b != 0: 
        print("Phương trình vô nghiệm")
if a!= 0:
    x = -b/a
    print("Nghiệm phương trình là:",x)
