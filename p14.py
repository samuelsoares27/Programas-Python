# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:50:16 2019

@author: Aluno
"""

arq = open('dados.txt')

M = []

for linha in arq:
    valores = [int(x) for x in linha.split()]
    M.append(valores)