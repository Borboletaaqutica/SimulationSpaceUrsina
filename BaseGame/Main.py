import subprocess
import sys

# 30% Inteligência Artificial, 70% Código Humano
# Criado por: [Cass]

def instalar_dependencias():
    try:
        import ursina
    except ImportError:
        print("Instalando dependências...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ursina"])
        print("Dependências instaladas com sucesso! Reinicie o app.")
        sys.exit(0)

instalar_dependencias()

from ursina import *
from random import randint
from math import radians, sin, cos, pi

app = Ursina()
window.color = color.black

window.fps_counter.enabled = False
window.exit_button.visible = True
window.fullscreen = True

# ESFERA CANONICAMENTE GRANDE DE FOGO NO MEIO DO ESPAÇO
sol = Entity(model='sphere', color=color.yellow, scale=2, position=(0, 0, 0), glow=1)

def desenhar_orbita(raio, cor=color.white, pontos=200):
    for i in range(pontos):
        angulo = radians(i * (360 / pontos))
        x = cos(angulo) * raio
        z = sin(angulo) * raio
        Entity(model='sphere', scale=0.06, color=cor.tint(-0.6), position=(x, 0, z))

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

planetas = [
    criar_planeta('Mercúrio', color.gray, 3, 0.2, 30),
    criar_planeta('Vênus', color.orange, 5, 0.3, 20),
    criar_planeta('Terra', color.blue, 7, 0.4, 10),
    criar_planeta('Marte', color.red, 9, 0.35, 8),
    criar_planeta('Júpiter', color.brown, 12, 1.0, 5),
    criar_planeta('Saturno', color.yellow.tint(-0.2), 15, 0.9, 4),
    criar_planeta('Urano', color.cyan, 18, 0.7, 3),
    criar_planeta('Netuno', color.blue.tint(-0.2), 21, 0.65, 2),
    criar_planeta('Plutão', color.white, 24, 0.1, 1),
]

camera.position = (0, 20, -40) 
camera.rotation_x = 45
camera.fov = 90

# Velocidade
velocidade_fator = 1.0

def input(key):
    global velocidade_fator
    if key == 'up arrow':
        velocidade_fator += 0.1
        print(f"Velocidade aumentada: {velocidade_fator:.1f}")
    elif key == 'down arrow':
        velocidade_fator = max(0.1, velocidade_fator - 0.1)
        print(f"Velocidade reduzida: {velocidade_fator:.1f}")

def update():
    for centro in planetas:
        centro.rotation_y += centro.rot_speed * velocidade_fator * time.dt

app.run()
