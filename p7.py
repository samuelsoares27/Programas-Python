arq = open('qb.txt')

#for linha in arq: 
#    item= linha.split()
#    print(item[0], item[1], item[-9])

#linha = arq.readline()
#readline => lê uma linha
#readlines => lê todas as linhas de um arquivo

""" while linha:
    linha = linha.split()
    print(linha[0], linha[1] , linha[9])
    linha = arq.readline() """

linhas = arq.readlines()

for linha in linhas: 
    item = linha.split()
    print(item[0], item[1], '\n', item[9])