import pygame, sys
import caro_board, my_menu
import constants
scene = constants.SCENE_MENU

res = width, height = 720, 720
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode(res)
fps_limit = 10
clock = pygame.time.Clock()

done = False
caro = caro_board.Caro(screen)
caro.draw_board()

menu = my_menu.Menu(screen)

while not done:
    clock.tick(fps_limit)
    
    if scene == constants.SCENE_MENU:
        scene = menu.main_loop()
    elif scene == constants.SCENE_GAME:
        scene = caro.main_loop()
    elif scene == constants.QUIT:
        done = True
    
    pygame.display.flip()

pygame.quit()
sys.exit()
    
