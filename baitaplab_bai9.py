# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:57:01 2024

@author: Admin
"""

print('========Menu=============')
print('     1. Hu tieu'          )
print('     2. Chao long'        )
print('     3. Banh canh'        )
print('     4. Bun rieu'         )
print('     5. Pho bo'           )
print('=========================')
a = int(input('Mon nhap lua chon:'))
if a == 1:  
    print('Hu tieu')
elif a == 2:
    print('Chao long')
elif a == 3:
    print('Banh canh')
elif a == 4:
    print('Bun rieu')
elif a == 5:
    print('Pho bo')
else:
    print('khong co trong menu')