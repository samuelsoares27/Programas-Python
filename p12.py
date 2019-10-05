# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:16:42 2019

@author: Aluno
"""

def media(notas): 
    if len(notas) > 0:
        return sum(notas)/len(notas)
    else:
        return 0
    
arq = open('notas.txt')
notas = []

for linha in arq:
    item = linha.split()
    notas = [int(x) for x in item[1:]]
    print(item[0], ' Media = %.2f' %(media(notas)))