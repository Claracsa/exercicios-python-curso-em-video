velocidade =  float(input('Qual a velocidade atual? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi MULTADO!')
    print('Você ultrapassou o limite permitido de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia e dirija com segurança!')
    