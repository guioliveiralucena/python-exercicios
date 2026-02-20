pergunta = int(input('Digite qual a distância da viagem que você vai fazer em km: '))

# Cria váriaveis que, se a viagem for abaixo de 200 km, cada km vale 0,50 reais e, se for mais longa 0,45.
viagem_abaixo_200km = pergunta * 0.50
viagem_longa = pergunta * 0.45

# Se a var. "pergunta" for menor ou igual a 200 executa o código abaixo.
if pergunta <= 200:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-=--=-=-=-=-==-=--=')
    print('\nPara esta viagem você terá que pagar {} reais.\n'.format(viagem_abaixo_200km))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-=--=-=-=-=-==-=--=')
# Ao contrário executa isso.
else:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-=--=-=-=-=-==-=--=')
    print('\nPara esta viagem você terá que pagar {} reais.\n'.format(viagem_longa))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-=--=-=-=-=-==-=--=')