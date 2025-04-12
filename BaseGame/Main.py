from ursina import *
from random import randint
from math import radians, sin, cos, pi

app = Ursina()
window.color = color.black

window.fps_counter.enabled = False
window.entity_counter.enabled = False
window.collider_counter.enabled = False
window.exit_button.visible = True
window.fullscreen = True

# Nave 
class Nave: # Quase nao da pra ver, mas ela existe
    def __init__(self, centro_orbita, raio_orbita, velocidade_orbita):
        self.nave = Entity(
            model='cube',  # Modelo simples da nave
            color=color.white,  # Cor da nave
            scale=(0.06, 0.06, 0.06),  # Escala da nave
            position=(raio_orbita, 0, 0)  # Posição inicial na órbita
        )
        self.centro_orbita = centro_orbita  # Centro da órbita (sol ou planeta)
        self.raio_orbita = raio_orbita  # Raio da órbita
        self.velocidade_orbita = velocidade_orbita  # Velocidade angular da órbita
        self.angulo = 2  # Ângulo inicial da órbita

    def update(self):
        self.angulo += self.velocidade_orbita * time.dt
        self.angulo %= 2 * pi
        self.nave.x = self.centro_orbita.x + cos(self.angulo) * self.raio_orbita
        self.nave.z = self.centro_orbita.z + sin(self.angulo) * self.raio_orbita

# Sol
sol = Entity(model='sphere', color=color.yellow, scale=2, position=(0, 0, 0), glow=1)

# Criar planetas
def desenhar_orbita(raio, cor=color.white, pontos=200):
    for i in range(pontos):
        angulo = radians(i * (360 / pontos))
        x = cos(angulo) * raio
        z = sin(angulo) * raio
        Entity(
            model='sphere',
            scale=0.06,
            color=cor.tint(-0.6),
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

# Instanciar naves fora do update()
naves = [
    Nave(planetas[2], 2, 2),  # Nave orbitando
    Nave(planetas[5], 2, 2),  # Nave orbitando 
]

# Câmera fixa e fundo
camera.position = (0, 20, -40)  # Afastar a câmera para trás
camera.rotation_x = 45
camera.fov = 90  # Aumentar o campo de visão para capturar mais elementos

def update():
    for nave in naves:  # Atualizar cada nave
        nave.update()  # Chama o método update da nave
    for centro in planetas:
        centro.rotation_y += centro.rot_speed * time.dt

app.run()
