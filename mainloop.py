import pygame, sys
##import pygame_menu 
import caro_board


res = width, height = 720, 720
fps_limit = 10
color_palettes = {
    "mysterious": ["#581b98", "#9c1de7", "#f3558e", "#faee1c", "#8cff75"],
    "freezing": ['#7d8aff', '#6db3de', '#84f5e4', '#6dde8e', '#cdfab6']
}
color_palette = color_palettes["mysterious"]
for i in  range(len(color_palette)):
    color_palette[i] = pygame.Color(color_palette[i])

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode(res)
screen.fill(color_palette[1])
clock = pygame.time.Clock()

done = False
ite = 0
board_row = 10
board_col = 10
square_width = 40
square_offset = 100
board = caro_board.Board(board_row, board_col)


for i in range(board_row):
    for j in range(board_col):
        rect = pygame.Rect(i * square_width + square_offset, j * square_width + square_offset, square_width, square_width)
        pygame.draw.rect(screen, color_palette[2], rect, 1, 2) 

while not done:
    clock.tick(fps_limit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = list(event.pos)
            board_pos = [0, 0]
            for i in range(2):
                board_pos[i] = (pos[i] - square_offset) // square_width
                pos[i] = board_pos[i] * square_width + square_offset # Position readjustment for X and O mark
            
            if ite % 2 == 0:
                if board.xPlayer.play([board_pos[0], board_pos[1]]):
                    pygame.draw.line(screen, color_palette[3], pos, (pos[0] + square_width, pos[1] + square_width), 5)
                    pygame.draw.line(screen, color_palette[3], (pos[0] + square_width, pos[1]), (pos[0], pos[1] + square_width), 5)
                    consecutive_points = board.xPlayer.is_winning()
                    if len(consecutive_points) == 5:
                        for i in range(2):            
                            consecutive_points[0][i] = consecutive_points[0][i] * square_width + square_offset + square_width / 2
                            consecutive_points[4][i] = consecutive_points[4][i] * square_width + square_offset + square_width / 2
                        pygame.draw.line(screen, color_palette[4], consecutive_points[0], consecutive_points[4], 20)
            
                    ite += 1
            else:
                if board.oPlayer.play([board_pos[0], board_pos[1]]):
                    rect = pygame.Rect(pos, (square_width, square_width))
                    pygame.draw.ellipse(screen, color_palette[0], rect, 5)
                    consecutive_points = board.oPlayer.is_winning()
                    if len(consecutive_points) == 5:
                        for i in range(2):            
                            consecutive_points[0][i] = consecutive_points[0][i] * square_width + square_offset + square_width / 2
                            consecutive_points[4][i] = consecutive_points[4][i] * square_width + square_offset + square_width / 2
                        pygame.draw.line(screen, color_palette[4], consecutive_points[0], consecutive_points[4], 20)
            
                    ite += 1
            print(board)
            
            

    pygame.display.flip()

pygame.quit()
sys.exit()
    
