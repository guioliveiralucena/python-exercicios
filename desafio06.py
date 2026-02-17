metros = float(input('Digite um valor em metros: '))

# Cria váriaveis para os centimetros e milimetros, e pega a variavel metros e multiplica pelos devidos números
centimetros = metros * 100
milimetros = metros * 1000

# Exibe na tela o valor
print('\nEsse velor equivale a {:.0f} centímetros'.format(centimetros))
print('\nE esse valor equivale a {:.0f} milímetros '.format(milimetros))
