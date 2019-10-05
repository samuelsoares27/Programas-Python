L = []

L.append('Polo\n')
L.append('Fusion\n')
L.append('Uno\n')
L.append('Camaro')

arq = open('carros.txt', 'w')
arq.writelines(L)
arq.close()