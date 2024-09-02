# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:02:30 2024

@author: Admin
"""

a=float(input('Cho a là so bat ki:'))
b=float(input('Cho b là so bat ki:'))
A = pow(a,1/3)
B = pow(b,1/3)
C = pow((a*b),1/3)
D = pow((A - B),2)
E = ((a+b)/(A + B) - (C))/((D))
print('Gia tri bieu thuc:',E)


