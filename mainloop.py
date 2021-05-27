import pygame, sys

res = width, height = 720, 720

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode(res)

done = False
ite = 0
caro_size = 40, 40

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
##            global ite
            pos = event.pos
            if ite % 2 == 0:
                image = pygame.image.load(r"xMark.gif")
                image = pygame.transform.scale(image, caro_size)
                screen.blit(image, pos)
            else:
                image = pygame.image.load(r"oMark.gif")
                image = pygame.transform.scale(image, caro_size)
                screen.blit(image, pos)
            ite += 1
            

    pygame.display.flip()

pygame.quit()
sys.exit()
    
