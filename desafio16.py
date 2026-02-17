import math

num = float(input('Digite um número em vírgula (ponto): '))

# O math.floor arredonda o número digitado na váriavel num
resultado = math.floor(num)

# Printa na tela
print('O número {} tem a porção inteira {}'.format(num, resultado))