import pygame
import constants
import button


class Board:
    __instance = None
    def __init__(self, object):
        if Board.__instance != None:
            raise Exception("Board is a singleton class")
        Board.__instance = self
        self.object = object
        self.square_width = object["square_width"]
        self.x_offset = object["x_offset"]
        self.y_offset = object["y_offset"]
        self.row = object["row"]
        self.col = object["col"]
        self.is_aspect_ratio_rescale = object["is_aspect_ratio_rescale"]
        self.color = {"square_border": object["color"]["square_border"]}
        self.board = [['.' for j in range(self.col)] for i in range(self.row)]


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


    def rescale(self, scaleX, scaleY):
        scale = min(scaleX, scaleY)
        if self.is_aspect_ratio_rescale:
            scaleX = scaleY = scale
        self.square_width = int(self.object["square_width"] * scale)
        self.x_offset = int(self.object["x_offset"] * scaleX)
        self.y_offset = int(self.object["y_offset"] * scaleY)


    def draw(self, screen):
        for i in range(self.row):
            for j in range(self.col):
                rect = pygame.Rect(i * self.square_width + self.x_offset, j * self.square_width + self.y_offset, self.square_width, self.square_width)
                pygame.draw.rect(screen, self.color["square_border"], rect, 1, 2)


class MoveLog():
    def __init__(self):
        self.move_log = []
        self.move_log_trash = []


    def draw(self, screen):
        for markObject in self.move_log:
            markObject.draw(screen)


    def add(self, markObject):
        if self.move_log_trash != []:
            self.move_log_trash = []
        self.move_log.append(markObject)


    def move_backward(self):
        if self.move_log == []:
            return
        self.move_log_trash.append(self.move_log.pop())


    def move_forward(self):
        if self.move_log_trash == []:
            return
        self.move_log.append(self.move_log_trash.pop())


    def __getitem__(self, i):
        return self.move_log[i]


    def __len__(self):
        return len(self.move_log)


class Mark():
    def __init__(self, object):
        self.object = object
        self.mark = object["mark"]
        self.board_x = object["board_x"]
        self.board_y = object["board_y"]
        self.color = self.object["color"]["x"] if self.mark == 'x' else self.object["color"]["y"]
        self.image = self.get_image()
        self.rect = self.get_image_rect()
        self.is_aspect_ratio_rescale = object["is_aspect_ratio_rescale"]
        # self.object["image"] = self.image
        # screen_width, screen_height = pygame.display.get_surface().get_size()
        # rect_width, rect_height = self.rect.size
        # self.object["image"] = pygame.transform.scale(self.image, (rect_width * constants.SCREEN_WIDTH / screen_width, rect_height * constants.SCREEN_HEIGHT / screen_width))
        # self.object["rect"] = {"x": self.rect.x * constants.SCREEN_WIDTH / screen_width, "y": self.rect.y * constants.SCREEN_HEIGHT // screen_width}


    def get_image_rect(self):
        rect = self.image.get_rect()
        # y = (self.object["x"] - Board.get_inst().x_offset) // Board.get_inst().square_width
        # x = (self.object["y"] - Board.get_inst().y_offset) // Board.get_inst().square_width
        rect.x = self.board_y * Board.get_inst().square_width + Board.get_inst().x_offset
        rect.y = self.board_x * Board.get_inst().square_width + Board.get_inst().y_offset
        return rect


    def get_image(self):
        return self.get_x_image() if self.mark == 'x' else self.get_o_image()


    def get_x_image(self):
        # corner_offset = Board.get_inst().square_width // 7
        corner_offset = 0
        image = pygame.Surface((Board.get_inst().square_width, Board.get_inst().square_width))
        pygame.draw.line(image, self.color, (corner_offset, corner_offset),
                         (Board.get_inst().square_width - corner_offset, Board.get_inst().square_width - corner_offset), 5)
        pygame.draw.line(image, self.color, (Board.get_inst().square_width - corner_offset, corner_offset),
                         (corner_offset, Board.get_inst().square_width - corner_offset), 5)
        image.set_colorkey((0,0,0))
        return image


    def get_o_image(self):
        image = pygame.Surface((Board.get_inst().square_width, Board.get_inst().square_width))
        pygame.draw.circle(image, self.color, (Board.get_inst().square_width // 2, Board.get_inst().square_width // 2), Board.get_inst().square_width // 2, 5)
        image.set_colorkey((0,0,0))
        return image


    def rescale(self, scaleX, scaleY):
        scale = min(scaleX, scaleY)
        if self.is_aspect_ratio_rescale:
            scaleX = scaleY = scale
        # self.rect.x = int(self.object["rect"]["x"] * scaleX)
        # self.rect.y = int(self.object["rect"]["y"] * scaleY)
        # width = self.object["image"].get_image_rect().width
        # height = self.object["image"].get_image_rect().height
        # self.image = pygame.transform.scale(self.object["image"], (scaleX * width, scaleY * height))
        self.image = self.get_image()
        self.rect = self.get_image_rect()


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Caro:
    def __init__(self, object):
        self.board = Board(constants.BOARD_OBJECT)
        self.move_log = MoveLog()
        self.consecutive_num = 5
        self.color = {
            "background": object["color"]["background"],
            "winning_line": object["color"]["winning_line"]
        }
        self.buttons = []
        for buttonObject in object["buttons"]:
            self.buttons.append(button.Button(buttonObject))


    def rescale(self, scaleX, scaleY):
        self.board.rescale(scaleX, scaleY)
        for markObject in self.move_log:
            markObject.rescale(scaleX, scaleY)
        for button in self.buttons:
            button.rescale(scaleX, scaleY)


    def add_move(self, x, y):
        board_y = int((x - self.board.x_offset) // self.board.square_width)
        if 0 <= board_y < self.board.row:
            board_x = int((y - self.board.y_offset) // self.board.square_width)
            if 0 <= board_x < self.board.col:
                if self.board[board_x][board_y] == '.':
                    mark = None
                    if len(self.move_log) % 2 == 0:
                        mark = 'x'
                    else:
                        mark = 'o'
                    self.board[board_x][board_y] = mark
                    markObject = Mark({"board_x": board_x, "board_y": board_y, "mark": mark, **constants.MARK_OBJECT})
                    self.move_log.add(markObject)


    def event_handler(self, event):
        if event.type == pygame.VIDEORESIZE:
            self.rescale(event.w / constants. SCREEN_WIDTH, event.h / constants.SCREEN_HEIGHT)


    def move_backward(self):
        if len(self.move_log) == 0:
            return
        self.board.remove(self.move_log[-1].board_x, self.move_log[-1].board_y)
        self.move_log.move_backward()


    def move_forward(self):
        if self.move_log.move_log_trash == []:
            return
        self.board.add(self.move_log.move_log_trash[-1].board_x, self.move_log.move_log_trash[-1].board_y, self.move_log.move_log_trash[-1].mark)
        self.move_log.move_forward()


    def draw_move(self, screen):
        self.move_log.draw(screen)


    def draw_board(self, screen):
        self.board.draw(screen)


    def draw_buttons(self, screen):
        for button in self.buttons:
            button.draw(screen)


    def draw(self, screen):
        screen.fill(self.color["background"])
        self.draw_move(screen)
        self.draw_board(screen)
        self.draw_buttons(screen)
        mark = None
        if len(self.move_log) % 2 == 0:
            mark = 'o'
        else:
            mark = 'x'
        if winning_board_points := self.find_consecutive_marks(mark):
            self.draw_winning_line(screen, winning_board_points)
        pygame.display.flip()


    def loop(self, screen, fps_limit = 10):
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
                    for button in self.buttons:
                        if button.is_clicked() and button.name == "move_backward":
                            self.move_backward()
                        if button.is_clicked() and button.name == "move_forward":
                            self.move_forward()
                    print(self.board, '\n')
                self.event_handler(event)

            self.draw(screen)


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


    def draw_winning_line(self, screen, winning_board_points):
        if len(winning_board_points) == self.consecutive_num:
            pygame.draw.line(screen, self.color["winning_line"],
                             (winning_board_points[0][1] * self.board.square_width + self.board.x_offset + self.board.square_width // 2,
                              winning_board_points[0][0] * self.board.square_width + self.board.y_offset + self.board.square_width // 2),
                             (winning_board_points[self.consecutive_num - 1][1] * self.board.square_width + self.board.x_offset + self.board.square_width // 2,
                              winning_board_points[self.consecutive_num - 1][0] * self.board.square_width + self.board.y_offset + self.board.square_width // 2), 5)
