# Example file showing a circle moving on screen
import pygame
import time
import Mazinger

# Añadir aquí las importaciones del armamento.
import Planeador
import PuñosFuera
import RayosFotónicos
import FuegoPecho


# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 800))
running = True

maz=Mazinger.Mazinger(screen)

# Incorporar aquí el armamento con pares de líneas como éstos.
Puños= PuñosFuera.PuñosFuera()
maz.incorpora(Puños)
Rayos= RayosFotónicos.RayosFotónicos()
maz.incorpora(Rayos)
Pecho= FuegoPecho.FuegoPecho()
maz.incorpora(Pecho)
Plano= Planeador.Planeador()
maz.incorpora(Plano)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    maz.arm(screen)
    time.sleep(0.5)
    maz.desactiva(screen)
    time.sleep(0.5)
    maz.sigArm()
