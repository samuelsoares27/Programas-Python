arq = open('carros.txt')
arq2 = open('carros2.txt', 'w')

linhas = arq.readlines()
linhas.reverse()

arq2.writelines(linhas)

arq.close()
arq2.close()