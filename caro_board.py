import pygame
import constants
import colors
import text

color_palette = colors.color_palettes["mysterious"]
for i in  range(len(color_palette)):
    color_palette[i] = pygame.Color(color_palette[i])


class Board:
    __instance = None
    def __init__(self, screen, row = 10, col = 10):
        if Board.__instance != None:
            raise Exception("Board is a singleton class")
        Board.__instance = self
        self.square_width = 40
        self.x_offset = 100
        self.y_offset = 100
        self.row = row
        self.col = col
        self.board = [['.' for j in range(self.col)] for i in range(self.row)]
        self.screen = screen


    def add(self, x, y, mark):
        self.board[x][y] = mark


    def remove(self, x, y):
        self.board[x][y] = '.'


    def __getitem__(self, i):
        return self.board[i]


    def get_inst():
        return Board.__instance


    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.board])


    def __repr__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.board])


    def draw(self):
        for i in range(self.row):
            for j in range(self.col):
                rect = pygame.Rect(i * self.square_width + self.x_offset, j * self.square_width + self.y_offset, self.square_width, self.square_width)
                pygame.draw.rect(self.screen, color_palette[2], rect, 1, 2)


class MoveLog():
    def __init__(self):
        self.moveLog = []
        self.moveLogTrash = []


    def draw(self):
        for markObject in self.moveLog:
            markObject.draw()


    def add(self, markObject):
        if self.moveLogTrash != []:
            self.moveLogTrash = []
        self.moveLog.append(markObject)


    def move_backward(self):
        if self.moveLog == []:
            return
        self.moveLogTrash.append(self.moveLog.pop())


    def move_forward(self):
        if self.moveLogTrash == []:
            return
        self.moveLog.append(self.moveLogTrash.pop())


    def __getitem__(self, i):
        return self.moveLog[i]


    def __len__(self):
        return len(self.moveLog)


class Mark():
    def __init__(self, screen, x, y, mark):
        self.mark = mark
        if (self.mark == 'x'):
            corner_offset = Board.get_inst().square_width // 7
            self.color = color_palette[0]
            self.image = pygame.Surface((Board.get_inst().square_width, Board.get_inst().square_width))
            pygame.draw.line(self.image, self.color, (corner_offset, corner_offset),
                             (Board.get_inst().square_width - corner_offset, Board.get_inst().square_width - corner_offset), 5)
            pygame.draw.line(self.image, self.color, (Board.get_inst().square_width - corner_offset, corner_offset),
                             (corner_offset, Board.get_inst().square_width - corner_offset), 5)
        else:
            self.image = pygame.Surface((Board.get_inst().square_width, Board.get_inst().square_width))
            pygame.draw.circle(self.image, color_palette[2], (Board.get_inst().square_width // 2, Board.get_inst().square_width // 2), Board.get_inst().square_width // 2, 5)
        self.image = pygame.transform.scale(self.image, (Board.get_inst().square_width, Board.get_inst().square_width))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.y = (x - Board.get_inst().x_offset) // Board.get_inst().square_width
        self.x = (y - Board.get_inst().y_offset) // Board.get_inst().square_width
        self.rect.x = self.y * Board.get_inst().square_width + Board.get_inst().x_offset
        self.rect.y = self.x * Board.get_inst().square_width + Board.get_inst().y_offset
        self.screen = screen


    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


class Caro:
    def __init__(self, screen, board_row = 10, board_col = 10):
        self.screen = screen
        self.board = Board(self.screen, board_row, board_col)
        self.moveLog = MoveLog()
        self.moveLogTrash = self.moveLog.moveLogTrash
        self.consecutive_num = 5
        self.moveBackwardButton = text.Text(self.screen, "Move back", 50)
        self.moveForwardButton = text.Text(self.screen, "Move forward", 50)


    def add_move(self, x, y):
        board_y = (x - self.board.x_offset) // self.board.square_width
        if 0 <= board_y < self.board.row:
            board_x = (y - self.board.y_offset) // self.board.square_width
            if 0 <= board_x < self.board.col:
                if self.board[board_x][board_y] == '.':
                    mark = None
                    if len(self.moveLog) % 2 == 0:
                        mark = 'x'
                    else:
                        mark = 'o'
                    self.board[board_x][board_y] = mark
                    markObject = Mark(self.screen, x, y, mark)
                    self.moveLog.add(markObject)


    def move_backward(self):
        if len(self.moveLog) == 0:
            return
        self.board.remove(self.moveLog[-1].x, self.moveLog[-1].y)
        self.moveLog.move_backward()


    def move_forward(self):
        if self.moveLogTrash == []:
            return
        self.board.add(self.moveLogTrash[-1].x, self.moveLogTrash[-1].y, self.moveLogTrash[-1].mark)
        self.moveLog.move_forward()


    def draw_move(self):
        self.moveLog.draw()


    def draw_board(self):
        self.board.draw()


    def draw_buttons(self):
        self.moveBackwardButton.draw(100, 50)
        self.moveForwardButton.draw(300, 50)


    def draw(self):
        self.screen.fill(color_palette[1])
        self.draw_move()
        self.draw_board()
        self.draw_buttons()
        mark = None
        if len(self.moveLog) % 2 == 0:
            mark = 'o'
        else:
            mark = 'x'
        if winning_board_points := self.find_consecutive_marks(mark):
            self.draw_winning_line(winning_board_points)
        pygame.display.flip()


    def loop(self, fps_limit = 10):
        clock = pygame.time.Clock()
        while True:
            clock.tick(fps_limit)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return constants.QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return constants.SCENE_MENU
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.move_backward()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.move_forward()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = list(event.pos)
                    self.add_move(pos[0], pos[1])
                    if self.moveBackwardButton.is_clicked(event.pos):
                        self.move_backward()
                    if self.moveForwardButton.is_clicked(event.pos):
                        self.move_forward()
                    print(self.board, '\n')

            self.draw()


    def find_vertical_consecutive_marks(self, mark):
        result = []
        for j in range(self.board.col):
            for i in range(self.board.row - 4):
                for k in range(self.consecutive_num):
                    if (self.board[i+k][j] == mark):
                        result.append([i+k,j])
                    else:
                        result = []
                        break
                if len(result) == self.consecutive_num:
                    return result
        return result


    def find_horizontal_consecutive_marks(self, mark):
        result = []
        for i in range(self.board.row):
            for j in range(self.board.col - 4):
                for k in range(self.consecutive_num):
                    if (self.board[i][j+k] == mark):
                        result.append([i, j+k])
                    else:
                        result = []
                        break
                if len(result) == self.consecutive_num:
                    return result
        return result


    def find_diagonal_consecutive_marks(self, mark):
        result = []
        for i in range(self.board.row - 4):
            for j in range(self.board.col - 4):
                for k in range(self.consecutive_num):
                    if (self.board[i+k][j+k] == mark):
                        result.append([i+k, j+k])
                    else:
                        result = []
                        break
                if len(result) == self.consecutive_num:
                    return result
        return result


    def find_secondary_diagonal_consecutive_marks(self, mark):
        result = []
        for i in range(self.board.row - 4):
            for j in range(self.consecutive_num - 1, self.board.col):
                for k in range(self.consecutive_num):
                    if (self.board[i+k][j-k] == mark):
                        result.append([i+k, j-k])
                    else:
                        result = []
                        break
                if len(result) == self.consecutive_num:
                    return result
        return result



    def find_consecutive_marks(self, mark):
        if result := self.find_vertical_consecutive_marks(mark):
            return result
        if result := self.find_horizontal_consecutive_marks(mark):
            return result
        if result := self.find_diagonal_consecutive_marks(mark):
            return result
        if result := self.find_secondary_diagonal_consecutive_marks(mark):
            return result
        return []


    def draw_winning_line(self, winning_board_points):
        if len(winning_board_points) == self.consecutive_num:
            pygame.draw.line(self.screen, color_palette[4],
                             (winning_board_points[0][1] * self.board.square_width + self.board.x_offset + self.board.square_width // 2,
                              winning_board_points[0][0] * self.board.square_width + self.board.y_offset + self.board.square_width // 2),
                             (winning_board_points[self.consecutive_num - 1][1] * self.board.square_width + self.board.x_offset + self.board.square_width // 2,
                              winning_board_points[self.consecutive_num - 1][0] * self.board.square_width + self.board.y_offset + self.board.square_width // 2), 5)
