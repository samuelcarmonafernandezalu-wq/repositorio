# Example file showing a circle moving on screen
import pygame

class Mazinger:
    def __init__(self,screen):
        self.__cuerpo=pygame.image.load('./Mazinger.png')
        screen.blit(self.__cuerpo,(0,0))
        self.__armamento=[]
        self.__inxArm=0
        pygame.display.flip()

    def incorpora(self,arma):
        self.__armamento.append(arma)
        

    def arm(self,screen):
        if len(self.__armamento)==0:
            return
        self.__armamento[self.__inxArm].enciende(screen)
        self.__armamento[self.__inxArm].grito()
    
    def sigArm(self):
        if len(self.__armamento)==0:
            return
        self.__inxArm=(self.__inxArm+1)%len(self.__armamento)

    def desactiva(self,screen):
        screen.blit(self.__cuerpo,(0,0))
        pygame.display.flip()


