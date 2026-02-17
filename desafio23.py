g = input('Escreva o nome de uma cidade: ').strip()

# Se a palavra Santo não estiver(not in) na váriavel 'g', executa o if, essa função é boa porque se a pessoa digitar Santo em qualquer lugar,
# e em qualquer ordem mostra!
if 'Santo' not in g:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('\nSua cidade não tem Santo no nome.\n')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

else:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('\nO nome da cidade que você digitou tem Santo!\n')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


