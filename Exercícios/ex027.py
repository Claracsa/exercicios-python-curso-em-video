nome = str(input('Digite seu nome completo: ')).upper().strip()
print('Prazer em te conhecer!')
s = nome.split()
print('Seu primeiro nome é {}.'.format(s[0]))
print('Seu último nome é {}.'.format(s[len(s) - 1]))