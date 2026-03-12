import Arma
import pygame

class Planeador(Arma.Arma):
    def __init__(self):
        self.__planeadorOn=pygame.image.load('./PlaneadorOn.png')

    def enciende(self,screen):
        screen.blit(self.__planeadorOn,(0,0))
        pygame.display.flip()

    def grito(self):
        print('¡¡¡¡¡Planeador, abajo!!!!')