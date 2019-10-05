arq = open('carros.txt')
arq2 = open('carros2.txt', 'w')

linhas = arq.readlines()

for i in range(len(linhas)):
    arq2.write(str(i+1) + ' - ' + linhas[i])

arq.close()
arq2.close()