pergunta = float(input('Quantos km(quilômetros) você está dirigindo? '))
limite_de_velocidade = 80
valor_por_km = 7.0

if pergunta >= limite_de_velocidade:
    km_acima = pergunta - limite_de_velocidade
    multa = km_acima * valor_por_km
    print('\n=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=')
    print('\nVocê ultrapassou {} km acima do limite de velocidade!'.format(km_acima))
    print('\nVocê terá que pagar uma multa de R$:{}!'.format(multa))
    print('\n=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=')

else:
    print('\n=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=')
    print('\nMuito bem! Você não ultrapassou o limite de velocidade!')
    print('\n=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=')