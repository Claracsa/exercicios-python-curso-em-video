preço = float(input('Qual é o preço do produto? R$'))
desconto = preço - (preço * 0.05)
print('O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f}.'.format(preço, desconto))