nome = input('Digite seu nome completo: ').strip()
# A função "split()" divide os espaços em brancos e separa 
nome_separado = nome.split()

# Se "nome" estiver na variável "nome_separado, executa"
for nome in nome_separado:
    print(nome)


