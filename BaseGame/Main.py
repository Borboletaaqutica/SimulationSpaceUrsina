from ursina import *
from math import sin, cos, radians

app = Ursina()
window.color = color.black

window.fps_counter.enabled = False
window.entity_counter.enabled = False
window.collider_counter.enabled = False
window.exit_button.visible = True
window.fullscreen = True

# Sol
sol = Entity(model='sphere', color=color.yellow, scale=2, position=(0, 0, 0), glow=1)

def desenhar_orbita(raio, cor=color.white, pontos=200):  # Aumentar o número de pontos para suavizar a órbita
    for i in range(pontos):
        angulo = radians(i * (360 / pontos))
        x = cos(angulo) * raio
        z = sin(angulo) * raio
        Entity(
            model='sphere',
            scale=0.05,  # escala
            color=cor.tint(-0.3),  # Ajustar o tom para maior contraste
            position=(x, 0, z)
        )

def criar_planeta(nome, cor, distancia, tamanho, velocidade):
    desenhar_orbita(distancia)
    centro = Entity()
    planeta = Entity(
        model='sphere',
        color=cor,
        scale=tamanho,
        position=(distancia, 0, 0),
        parent=centro
    )


    centro.rot_speed = velocidade
    return centro

# Criar planetas
planetas = [
    criar_planeta('Mercúrio', color.gray, 3, 0.2, 30),
    criar_planeta('Vênus', color.orange, 5, 0.3, 20),
    criar_planeta('Terra', color.blue, 7, 0.4, 10),
    criar_planeta('Marte', color.red, 9, 0.35, 8),
    criar_planeta('Júpiter', color.brown, 12, 1.0, 5),
    criar_planeta('Saturno', color.yellow.tint(-0.2), 15, 0.9, 4),
    criar_planeta('Urano', color.cyan, 18, 0.7, 3),
    criar_planeta('Netuno', color.blue.tint(-0.2), 21, 0.65, 2),
    criar_planeta('Plutão', color.white, 24, 0.1, 1),  # Plutão como planeta anão
]

# Câmera fixa e fundo
camera.position = (0, 20, -40)  # Afastar a câmera para trás
camera.rotation_x = 45
camera.fov = 90  # Aumentar o campo de visão para capturar mais elementos


def update():
    for centro in planetas:
        centro.rotation_y += centro.rot_speed * time.dt

app.run()
