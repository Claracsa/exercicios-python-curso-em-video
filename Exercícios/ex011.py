largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura
litros = área / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, altura, área))
print('Para pintar essa parede você precisará de {:.2f}l de tinta.'.format(litros))