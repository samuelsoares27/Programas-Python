# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:11:48 2019

@author: Aluno
"""

import sys 

texto = sys.argv[1]

print(texto)

tab = {}

for letra in texto.lower():
    if letra in tab:
        tab[letra] += 1
    else:
        tab[letra] = 1
        
for chave in sorted(tab):
    print(chave, ' - ', tab[chave])