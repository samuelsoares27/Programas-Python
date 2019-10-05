# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:36:29 2019

@author: Aluno
"""
import random

n=random.randint(1,50)

x=int(input("Entre com um número entre 0 e 50: "))

while x!=n:
    if n < x:
        print('É menor!')
    else:
        print('É maior!')    
    x=int(input("Entre com um número entre 0 e 50: "))

print("Acertou!")