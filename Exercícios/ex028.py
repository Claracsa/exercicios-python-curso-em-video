import random
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
randomnum = random.randint(0, 5)
num = int(input('Em que número eu pensei? '))
print('Processando...')
if num != randomnum:
    print('Ganhei, eu pensei no {} e não no {}.'.format(randomnum, num))
else:
    print('Parabéns, você conseguiu me vencer, pensamos no mesmo número, o {}.'.format(randomnum))
