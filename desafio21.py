primeiro_nome = input('Digite seu primeiro nome: ')
nome_completo = input('Digite seu nome completo: ')
letras_do_primeiro_nome = len(primeiro_nome)
sem_espaços = nome_completo.replace(" ", " ")
total_sem_espaços = len(sem_espaços)


# Printa na tela o nome com essas caractéres
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=--===--==-=-=--=-=-=-=-==-==')
print('\n Seu nome completo com todas as letras minúsculas: {}'.format(nome_completo.lower()))
print('\n Seu nome completo com todas as letras maiúsculas: {}'.format(nome_completo.upper()))
print('\n Quantas letras ao todo tem seu nome completo (sem considerar os espaços): {}'.format(total_sem_espaços))
print('\n Quantas letras tem só seu primeiro nome: {}'.format(letras_do_primeiro_nome))
print('\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=--===--==-=-=--=-=-=-=-==')
