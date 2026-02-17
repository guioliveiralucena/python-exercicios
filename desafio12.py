preço = float(input('Digite o preço de um produto: '))
percentagem = int(input('Digite uma percentagem de desconto de 0 a 100: '))

# Faz a porcentagem que é 0.95 que equivale a 5%
desconto = preço * ((100 - percentagem) / 100)

print('Esse produto está com um desconto de {}%, então você terá que pagar {:.1f}'.format(percentagem, desconto))
