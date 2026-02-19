# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True

x0=120
y0=120
nombres=['torre','caballo','arfil','reina','rey','peon']
orden=[0,1,2,3,4,2,1,0]
piezas=[[],[]]
for equip in range(2):
    for piez in range(len(nombres)):
        piezas[0].append(pygame.image.load('./img/'+nombres[piez]+'B.png'))
        piezas[1].append(pygame.image.load('./img/'+nombres[piez]+'N.png'))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray95")
    pygame.draw.rect(screen, "green3", (x0,y0, 240,240))
    for fil in range(8):
        for col in range(8):
            if fil%2==0 and col%2==0 or fil%2 != 0 and col%2 != 0:
                pygame.draw.rect(screen, "white", (x0+col*30,y0+fil*30,30,30))
    pygame.draw.rect(screen,"black",(x0,y0,240,240),1)
    pygame.draw.rect(screen,"black",(x0-3,y0-3,246,246),1)

    for inx in range(8):
        screen.blit(piezas[0][orden[inx]],(x0+inx*30,y0))
        screen.blit(piezas[0][5],(x0+inx*30,y0+30))
        screen.blit(piezas[1][5],(x0+inx*30,y0+180))
        screen.blit(piezas[1][orden[inx]],(x0+inx*30,y0+210))

 
    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()