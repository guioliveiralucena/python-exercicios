num = int(input('Digite um ano qualquer: '))

# Se o "num" for divisívil por 4 executa o if
if num % 4 == 0:

    # Se o "num" dividido por 100 for diferente de 0, ou "num" dividido por 400 for igual a 0, mostra que é um ano bissexto!
    if num % 100 != 0 or num % 400 == 0:
        print('Esse ano é um ano Bissexto!')

    # Ao contrário executa essas '4' linhas de códigos abaixo!
    else:
        print('Esse não é um ano Bissexto!')

else: 
    print('Esse não é um ano Bissexto!')