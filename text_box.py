import pygame
import time
import json
import constants

class TextBox:
    def __init__(self, object):
        self.object = object
        if self.object['is_center'] == True:
            self.center_x = self.object['center_x']
            self.center_y = self.object['center_y']
            # self.x = self.object['center_x']
            # self.y = self.object['center_y']
        else:
            self.x = self.object['x']
            self.y = self.object['y']
        self.width = self.object['width']
        self.height = self.object['height']
        self.border_radius = self.object['border_radius']
        self.text = self.object['text']
        self.text_font = self.object['text_font']
        self.text_limit = self.object['text_limit']
        self.text_size = self.object['text_size']
        self.color = self.object['color'] # color te had to have background and text key
        self.name = self.object['name']
        self.is_center = self.object['is_center']
        self.padding_left = self.object['padding_left']
        self.padding_right = self.object['padding_right']
        self.is_focus = True
        self.cursor_pos = 0
        self.char_widths = {}
        self.text_surface = None
        self.font = None
        self.rect = None

    def get_text_surface(self):
        if not self.text_surface:
            font = self.get_font()
            self.text_surface = font.render(self.text, True, self.color["text"])
        return self.text_surface

    def get_text_rect_width(self):
        return self.get_text_surface().get_width()

    def get_text_rect_height(self):
        return self.get_text_surface().get_height()

    def get_rect_width(self):
        padded_width = self.get_text_rect_width() + self.padding_left + self.padding_right
        return max(padded_width, self.width)

    def get_rect_height(self):
        return self.height

    def get_rect_x(self):
        return self.center_x - self.get_rect_width() / 2 if self.is_center else self.x

    def get_rect_y(self):
        return self.center_y - self.get_rect_height() / 2 if self.is_center else self.y

    def get_rect_xy(self):
        return (self.get_rect_x(), self.get_rect_y())

    def get_text_rect_x(self):
        return self.center_x - self.get_text_rect_width() / 2 if self.is_center else self.x + self.get_rect_width()/2 - self.get_text_rect_width()/2

    def get_text_rect_y(self):
        return self.center_y - self.get_text_rect_height() / 2 if self.is_center else self.y + self.get_rect_height()/2 - self.get_text_rect_height()/2

    def get_text_rect_xy(self):
        return (self.get_text_rect_x(), self.get_text_rect_y())

    def get_rect(self):
        if not self.rect:
            self.rect = pygame.Rect(self.get_rect_x(), self.get_rect_y(), self.get_rect_width(), self.get_rect_height())
        return self.rect

    def get_char_width(self, char):
        font = self.get_font()
        if not char in self.char_widths:
            self.char_widths[char] = font.render(char, True, self.color["text"]).get_width()
        return self.char_widths[char]

    def get_cursor_pos_of_mouse_pos(self, mouse_pos):
        if self.get_rect_y() <= mouse_pos[1] < self.get_rect_y() + self.get_rect_height():
            prev_char_widths_sum = self.get_text_rect_x()
            if self.get_rect_x() <= mouse_pos[0] < prev_char_widths_sum:
                return 0
            for i in range(len(self.text)):
                char_widths_sum = prev_char_widths_sum + self.get_char_width(self.text[i])
                # print(prev_char_widths_sum, mouse_pos[0], char_widths_sum, (prev_char_widths_sum + char_widths_sum)/2)
                if prev_char_widths_sum <= mouse_pos[0] < char_widths_sum:
                    if mouse_pos[0] < (prev_char_widths_sum + char_widths_sum)/2:
                        return i
                    else:
                        return i + 1
                prev_char_widths_sum = char_widths_sum
            if char_widths_sum <= mouse_pos[0] < self.get_rect_x() + self.get_rect_width():
                return len(self.text) + 1
        return -1

    def get_font(self):
        return self.font if self.font else pygame.font.SysFont(self.text_font, int(self.text_size))

    def draw(self, screen):
        font = self.get_font()
        text_surface = self.get_text_surface()
        fake_text_surface = font.render(self.text[:self.cursor_pos], True, self.color["text"])
        text_rect = text_surface.get_rect(topleft = self.get_text_rect_xy())

        self.rect = self.get_rect()
        pygame.draw.rect(screen, self.color["background"], self.rect, 0, self.border_radius)

        if (self.is_focus):
            if (time.time() % 1 > 0.5):
                cursor_surface = pygame.Surface((int(0.08 * self.text_size), int(0.7 * self.text_size)))
                cursor_surface.fill(self.color["cursor"])
                cursor_rect = cursor_surface.get_rect(top = text_rect.top, left = text_rect.left + fake_text_surface.get_width())
                screen.blit(cursor_surface, cursor_rect)

        screen.blit(text_surface, text_rect)


    def rescale(self, x_scalar, y_scalar):
        if self.is_center:
            self.center_x = self.object['center_x'] * x_scalar
            self.center_y = self.object['center_y'] * y_scalar
        else:
            self.x = self.object['x'] * x_scalar
            self.y = self.object['y'] * y_scalar
        self.width = self.object['width'] * x_scalar
        self.height = self.object['height'] * y_scalar
        self.padding_left = self.object['padding_left'] * x_scalar
        self.padding_right = self.object['padding_right'] * x_scalar
        self.text_surface = None
        self.rect = None
        # self.border_radius = self.object['border_radius']
        self.text_size = self.object['text_size'] * y_scalar


    def is_hovered(self):
        return self.get_rect().collidepoint(pygame.mouse.get_pos())


    def insert_string_at(self, string, string_to_add, pos = 0):
        return string[:pos] + string_to_add + string[pos:]


    def delete_string_at(self, string, pos = 0, len_to_delete = 1):
        return string[:pos - len_to_delete] + string[pos:]


    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered():
                self.is_focus = True
            else:
                self.is_focus = False
            self.cursor_pos = self.get_cursor_pos_of_mouse_pos(event.pos)

        if event.type == pygame.VIDEORESIZE:
            self.rescale(event.w / constants.SCREEN_WIDTH, event.h / constants.SCREEN_HEIGHT)

        if event.type == pygame.KEYDOWN:
            if self.is_focus:
                if event.key == pygame.K_BACKSPACE:
                    if self.cursor_pos:
                        self.text = self.delete_string_at(self.text, self.cursor_pos, 1)
                    self.cursor_pos -= 1
                elif event.key == pygame.K_TAB:
                    string = "  " if self.text_limit - 1 > len(self.text) else " " if self.text_limit > len(self.text) else ""
                    self.text = self.insert_string_at(self.text, string, self.cursor_pos)
                    self.cursor_pos += len(string)
                elif event.key == pygame.K_CLEAR:
                    self.text = ""
                elif event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_PAUSE:
                    pass
                elif event.key == pygame.K_ESCAPE:
                    self.is_focus = False
                elif event.key == pygame.K_DELETE:
                    self.text = self.delete_string_at(self.text, self.cursor_pos + 1, 1)
                elif event.key == pygame.K_LEFT:
                    self.cursor_pos -= 1
                elif event.key == pygame.K_RIGHT:
                    self.cursor_pos += 1
                elif event.key == pygame.K_HOME:
                    self.cursor_pos = 0
                elif event.key == pygame.K_END:
                    self.cursor_pos = len(self.text)
                else:
                    if self.text_limit > len(self.text):
                        self.text = self.insert_string_at(self.text, event.unicode, self.cursor_pos)
                        self.cursor_pos += 1
                if self.cursor_pos <= -1:
                    self.cursor_pos = 0
                if self.cursor_pos > len(self.text):
                    self.cursor_pos = len(self.text)
                # if len(self.text) > self.text_limit:
                #     self.text = self.text[:self.text_limit]


    def loop(self, screen, fps_limit = 10):
        done = False
        clock = pygame.time.Clock()
        result = constants.QUIT
        while not done:
            clock.tick(fps_limit)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                result = self.event_handler(event)
            screen.fill((255,255,255))
            self.draw(screen)
            pygame.display.flip()
        return result

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT], pygame.RESIZABLE)

    text_box = TextBox(constants.TEXT_BOX_OBJECT[1])

    text_box.loop(screen)
