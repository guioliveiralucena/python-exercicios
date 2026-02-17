a = int(input('Digite um número 0 à 9999: '))

# Faz o cálculo de Unidade, Dezena, Centena e milhar
s1 = a // 1 % 10
s2 = a // 10 % 10
s3 = a // 100 % 10
s4 = a // 1000 % 10 

# Printa na tela o resultado

print('=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\nUnidade: {}'.format(s4))
print('Dezena: {}'.format(s3))
print('Centena: {}'.format(s2))
print('Milhar: {}\n'.format(s1))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-')