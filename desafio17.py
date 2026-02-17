import math

cateto_adjacente = int(input('Digite o cateto adjacente do triângulo retângulo: '))
cateto_oposto = int(input('Digite o cateto oposto do triângulo retângulo: '))

# Faz o cálculo pra saber a hipotenusa
hipotenusa = math.sqrt((cateto_adjacente ** 2) + (cateto_oposto ** 2))

  # Dois jeitos de fazer a hipotenusa
#  Jeito manual
print('A Hipotenusa é {:.2f}'.format(hipotenusa))

# jeito automático, que já vem importado na biblioteca math
print('A Hipotenusa é {:.2f}'.format(math.hypot(cateto_adjacente, cateto_oposto)))

