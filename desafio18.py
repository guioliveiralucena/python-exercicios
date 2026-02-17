import math

pergunta = int(input('Digite um ângulo qualquer: '))
angulo = pergunta
# Converte o angulo em radianos
angulo_radianos = math.radians(angulo)

# Calcula o seno, cosseno e tangente do ângulo digitado
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Mostra as respostas
print('O seno do angulo de {}, é {:.2f}'.format(pergunta, seno))
print('O cosseno do angulo de {}, é {:.2f}'.format(pergunta, cosseno))
print('O tangente do angulo de {}, é {:.2f}'.format(pergunta, tangente))


