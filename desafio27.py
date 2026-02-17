import random
print('O computador irá escolher um número aleatório de 1 a 10!')
pergunta = int(input('Tente descobrir que número é esse, digite aqui: '))
# Faz o pc escolher um número aleatório com o "random.randint" de 1 a 10
escolha_do_pc = random.randint(1, 10)

# Faz a lógica se a pergunta foi igual a escolha_do_pc, se for executa oque foi digitado, ao contrário digita aquilo
if pergunta == escolha_do_pc:
    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('\nParabéns você acertou!')
    print('O número ecolhido pelo pc foi {}'.format(escolha_do_pc))
    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=')
else:
    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('\nQue pena você errou :c')
    print('O número ecolhido pelo pc foi {}'.format(escolha_do_pc))
    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=')