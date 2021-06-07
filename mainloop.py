import pygame, sys
import caro_board

fps_limit = 10
clock = pygame.time.Clock()

done = False
caro = caro_board.Caro()
caro.draw_board()

while not done:
    clock.tick(fps_limit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = list(event.pos)
            caro.add_move(pos[0], pos[1])
            print(caro.board)
            caro.draw()

    
    pygame.display.flip()

pygame.quit()
sys.exit()
    
