from ursina import *

# Chama pro app funcinar
app = Ursina()

# Cria uma 'Entidade' que é um cubo, com os valores dados abaixo
cubo = Entity(parent=scene, model='cube', color= color.green, scale= (2, 2, 2),position= (-3, 1, 0), texture='brick', collider='mesh')
cubo2 = Entity(parent=scene, model='cube', color= color.white, scale= (2, 2, 2),position= (3, 1, 0), collider='mesh', texture='grass')

# Atualiza o jogo a cada frame
def update():

    # Se a tecla 'd' estiver pressionada meche o cubo para direita
    if held_keys['d']:
        cubo.x += 4 * time.dt

    # Se a tecla 'a' estiver pressionada meche o cubo para esquerda
    if held_keys['a']:
        cubo.x -= 4 * time.dt

    # Se a tecla 'w' estiver pressionada meche o cubo para cima
    if held_keys['w']:
        cubo.y += 4 * time.dt

    # Se a tecla 's' estiver pressionada meche o cubo para baixo
    if held_keys['s']:
        cubo.y -= 4 * time.dt

    # Mesma lógica, só que pro outro cubo movendo com as setas do teclado
    if held_keys['left arrow']:
        cubo2.x -= 4 * time.dt

    if held_keys['right arrow']:
        cubo2.x += 4 * time.dt
        
    if held_keys['up arrow']:
        cubo2.y += 4 * time.dt

    if held_keys['down arrow']:
        cubo2.y -= 4 * time.dt

# Roda o jogo/app
app.run()