n = float(input('Uma distância em metros: '))
print('A medida de {:.1f} corresponde a:')
print('{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(n / 1000, n / 100, n / 10, n * 10, n * 100, n * 1000))