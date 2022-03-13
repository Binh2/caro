import pygame, sys
import caro_board, main_menu
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

menu = main_menu.Menu(screen)

while not done:
    clock.tick(fps_limit)

    if scene == constants.SCENE_MENU:
        scene = menu.loop(fps_limit)
    elif scene == constants.SCENE_GAME:
        scene = caro.loop(fps_limit)
    elif scene == constants.QUIT:
        done = True

    pygame.display.flip()

pygame.quit()
sys.exit()
