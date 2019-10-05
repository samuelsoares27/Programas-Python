# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:03:55 2019

@author: Aluno
"""

texto = 'Marcos Alberto de Carvalho'

dicionario = {}

for letra in texto.lower():
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1