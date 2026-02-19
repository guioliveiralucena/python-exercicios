pergunta = int(input('Digite um número: '))

# Se a váriavel "pergunta" dividido por 2 for igual a 0, mostra que o número é par
if pergunta % 2 == 0:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('\nO número {} é par\n'.format(pergunta))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
# Ao contrário mostra que é impar
else:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('\nO número {} é impar\n'.format(pergunta))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')