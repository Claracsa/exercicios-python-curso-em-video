dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
d = dias * 60
k = km * 0.15
print('O total a pagar é de R${:.2f}'.format(d + k))