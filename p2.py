# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:22:22 2019

@author: Aluno
"""

#i=0
#while i<10:
#    print(i)
#    i+=1
#    
#print('fim')

n = int(input("Entre com um valor inteiro: "))

f=1

while(n > 1):
    f *= n
    n -= 1
    
print("Fatorial = ", f)