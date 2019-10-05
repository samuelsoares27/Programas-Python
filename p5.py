# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:04:16 2019

@author: Aluno
"""

def igual(a, b):
    if abs(a)==abs(b):
        print("São iguais")
    else:
        print("São diferentes")
        
def fib(n):
    a,b = 0,1
    seq = [] 
    
    while a<=n:
        seq.append(a)
        a,b = b,a+b
        
    return seq