import pygame, sys

res = width, height = 720, 720
fps_limit = 10
color_palette = ["#581b98", "#9c1de7", "#f3558e", "#faee1c"]
for i in  range(len(color_palette)):
    color_palette[i] = pygame.Color(color_palette[i])

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode(res)
screen.fill(color_palette[0])
clock = pygame.time.Clock()

done = False
ite = 0
square_num = 10 # Number of square in the grid
square_width = 40
square_offset = 100
board = [[0 for j in range(square_num)] for i in range(square_num)]

def print_board(board):
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in board]))


for i in range(square_num):
    for j in range(square_num):
        rect = pygame.Rect(i * square_width + square_offset, j * square_width + square_offset, square_width, square_width)
        pygame.draw.rect(screen, color_palette[3], rect, 1, 2) 

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
                print(board_pos[i])
                pos[i] = board_pos[i] * square_width + square_offset # Position readjustment for X and O mark
                
            if ite % 2 == 0:
                print(board_pos)
                board[board_pos[0]][board_pos[1]] = 1
                pygame.draw.line(screen, color_palette[1], pos, (pos[0] + square_width, pos[1] + square_width), 5)
                pygame.draw.line(screen, color_palette[1], (pos[0] + square_width, pos[1]), (pos[0], pos[1] + square_width), 5)
            else:
                board[board_pos[0]][board_pos[1]] = 2
                rect = pygame.Rect(pos, (square_width, square_width))
                pygame.draw.ellipse(screen, color_palette[2], rect, 5)
                                    
            ite += 1
            print_board(board)
            

    pygame.display.flip()

pygame.quit()
sys.exit()
    
