# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:40:29 2019

@author: Aluno
"""

arq = open('dados.txt')

M = []

dim = arq.readline().split()

for i in range(int(dim[0])):
    linha  = [int(x) for x in arq.readline().split()]
    M.append(linha)     