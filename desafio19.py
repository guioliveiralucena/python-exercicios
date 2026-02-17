import random

aluno1 = input('Digite o nome de um aluno qualquer: ')
aluno2 = input('Digite o nome de outro aluno: ')
aluno3 = input('Digite o nome de outro: ')
aluno4 = input('Digite o nome de mais um aluno: ')

# Cria uma lista dos alunos
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteia o nome de um dos alunos
sorteio = random.choice(lista_alunos)

print('O aluno escolhido foi {}'.format(sorteio))