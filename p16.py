# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 19:12:00 2018

@author: Aluno
"""

#arq = open("dados.txt","r")

def lermat(arquivo,multiplicador):
    arq = open(arquivo,"r")
    master=[]
    for linha in arq:
        linhastr = linha.split();
        valores=[]
        for valor in linhastr:
            valores.append(int(valor)*multiplicador)
        master.append(valores)
    return master


def mulmat(matriz, escalar):
    for l,linha in enumerate(matriz):
        for c, valor in enumerate(linha):
            matriz[l][c] *= escalar
            

def gravamat(matriz,NOME_ARQUIVO):
    arq = open(NOME_ARQUIVO,"w")
    for linha in matriz:
        for valor in linha:
            arq.write((str(valor)+' '))
        arq.write('\n')
    arq.close()