largura = float(input('Digite a largura dessa parede em metros: '))
altura = float(input('Digite a altura dessa parede em metros: '))

# Calcula a área
area = largura * altura

# Calcula a quantidade necessária de tinta dado no desáfio, que cada litro de tinta da pra pintar uma área de 2m²
tinta_necessaria = area / 2

# Printa na tela
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
print('A parede tem a dimensão de {} x {}, e sua área é de {}m²'.format(largura, altura, area))
print('A quantidade necessária de tinta para pintar essa parede é de {:.1f} litros'.format(tinta_necessaria))
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
