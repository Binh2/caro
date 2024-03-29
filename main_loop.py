import pygame, sys, json
import caro_board, menu
import constants
scene = constants.SCENE_MENU

res = width, height = constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode(res, pygame.RESIZABLE)
fps_limit = 10
clock = pygame.time.Clock()

done = False
caro = caro_board.Caro(constants.CARO_OBJECT)
caro.draw_board(screen)

menu_instance = menu.Menu(constants.MENU_OBJECT)

while not done:
    clock.tick(fps_limit)

    if scene == constants.SCENE_MENU:
        scene = menu_instance.loop(screen, fps_limit)
    elif scene == constants.SCENE_GAME:
        scene = caro.loop(screen, fps_limit)
    elif scene == constants.QUIT:
        done = True

    pygame.display.flip()

pygame.quit()
sys.exit()
