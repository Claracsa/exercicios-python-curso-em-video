import math
ângulo = float(input('Digite o ângulo que você deseja: '))
a = math.radians(ângulo)
print('O ângulo {} tem o SENO de {:.2f}'.format(ângulo, math.sin(a)))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(ângulo, math.cos(a)))
print('O ângulo {} tem o TANGENTE de {:.2f}'.format(ângulo, math.tan(a)))
