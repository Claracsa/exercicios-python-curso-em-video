distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    valor1 = distancia * 0.5
    print('Você está prestes a começar uma viagem de R${:.2f}'.format(valor1))
else:
    valor2 = distancia * 0.45
    print('Você está prestes a começar uma viagem de R${:.2f}'.format(valor2))
