# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:53:20 2019

@author: Aluno
"""

#for i in range(10,0,-1):
#    print(i)


L=["Maros", 10, "João", 8, "Ana", 7.3]

for i in range(0,len(L),2):
    print("%s nota igual a %.2f" %(L[i], L[i + 1]))