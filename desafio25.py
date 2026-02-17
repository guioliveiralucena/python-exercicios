pergunta = input('Digite alguma palavra: ').strip().upper()

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\nA letra "a" aparece {} vezes nessa palavra!'.format(pergunta.count('A')))
# O comando 'find' procura a letra da esquerda pra direita e mostra a posição dela 
print('A letra "a" apareceu pela primeira vez na posição {}!'.format(pergunta.find('A') + 1))
# O comando 'rfind' procura a letra da direita pra esquerda 
print('A letra "a" apareceu pela última vez na posição {}!\n'.format(pergunta.rfind('A') + 1))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')