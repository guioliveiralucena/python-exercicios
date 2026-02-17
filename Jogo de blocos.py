from ursina import *
# Importa a ursina pra conseguir rodar em primeira pessoa e os controles do jogo
from ursina.prefabs.first_person_controller import FirstPersonController

# Váriavel pra ursina
app = Ursina()

# Váriavel 'player' em primeira pessoa e o 'Sky' é o céu
player = FirstPersonController()
Sky()

# Cria o chão e os blocos
boxes = []
for i in range (20):
    for j in range (20):
        box = Button(color=color.white, model='cube', position=(j, 0, i),
                    texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)  

# Verifica se os botões esquerdos e direitos do mouse foram apertados, e de acordo com o que apertado executa os códigos
def input(key):
    # Verifica se o mouse está sobre um objeto
    if mouse.hovered_entity:
        # Faz a lógica do click do mouse esquerda pra destruir um bloco
        if key == 'right mouse down':
            new = Button(color=color.white, model='cube', position=mouse.hovered_entity.position + mouse.normal,
                             texture='grass.png', parent = scene, origin_y=0.5 )
            boxes.append(new)
        # Faz a lógica do click do mouse direito pra construir um bloco
        if key == 'left mouse down':
            target = mouse.hovered_entity
            if target in boxes:
                    boxes.remove(target)
                    destroy(target)

# Roda o jogo
app.run()