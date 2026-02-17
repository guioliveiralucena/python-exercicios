n = input('Digite algo: ')

print('\n Analizando o valor: {}'.format(n))
print("-" * 30)

# Descobre o tipo primitivo da frase ou número.
print('\n O tipo primitivo: {}'.format(type(n)))

# Descobre todas as informações dos tipos primitivos.
print(' É tudo maiúsculo? {}'.format(n.isupper()))
print(' É tudo minúsculo? {}'.format(n.islower()))
print(' É um número? {}'.format(n.isnumeric()))
print(' É um texto? {}'.format(n.istitle()))
print(' É um número? {}'.format(n.isalnum()))


