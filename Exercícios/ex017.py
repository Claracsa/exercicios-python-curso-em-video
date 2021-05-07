import math
catoposto = float(input('Comprimento do cateto oposto: '))
catadjacente = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(catoposto, catadjacente)))