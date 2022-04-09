import pygame
import time
import json
import constants

class TextBox:
    def __init__(self, object):
        self.object = object
        self.x = self.object['x']
        self.y = self.object['y']
        self.width = self.object['width']
        self.height = self.object['height']
        self.border_radius = self.object['border_radius']
        self.text = self.object['text']
        self.text_size = self.object['text_size']
        self.color = self.object['color'] # color te had to have background and text key
        self.name = self.object['name']
        self.is_center = self.object['is_center']
        self.padding_left = self.object['padding_left']
        self.padding_right = self.object['padding_right']
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_focus = True
        self.cursor_pos = 0


    def draw(self, screen):
        font = pygame.font.SysFont(None, int(self.text_size))
        text_surface = font.render(self.text, True, self.color["text"])
        fake_text_surface = font.render(self.text[:self.cursor_pos], True, self.color["text"])
        if self.is_center:
            text_rect = text_surface.get_rect(center = (self.x, self.y))
        else:
            text_rect = text_surface.get_rect(topleft = (self.x, self.y + (self.height - text_surface.get_height())/2))

        padded_width = text_surface.get_width() + self.padding_left + self.padding_right
        self.rect = pygame.Rect(self.x - self.padding_left, self.y,
                                self.width if self.width > padded_width else padded_width, self.height)
        if self.is_center:
            x = self.x + ((self.padding_left + self.padding_right)/2 - self.padding_left)
            self.rect.center = (x, self.y)
        pygame.draw.rect(screen, self.color["background"], self.rect, 0, self.border_radius)

        if (self.is_focus):
            if (time.time() % 1 > 0.5):
                cursor_surface = pygame.Surface((int(0.08 * self.text_size), int(0.7 * self.text_size)))
                cursor_surface.fill(self.color["cursor"])
                cursor_rect = cursor_surface.get_rect(top = text_rect.top, left = text_rect.left + fake_text_surface.get_width())
                screen.blit(cursor_surface, cursor_rect)

        screen.blit(text_surface, text_rect)


    def rescale(self, xScalar, yScalar):
        self.x = self.object["x"] * xScalar
        self.y = self.object['y'] * yScalar
        self.width = self.object['width'] * xScalar
        self.height = self.object['height'] * yScalar
        # self.border_radius = self.object['border_radius']
        self.text_size = self.object['text_size'] * yScalar


    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())


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

        if event.type == pygame.VIDEORESIZE:
            self.rescale(event.w / constants.SCREEN_WIDTH, event.h / constants.SCREEN_HEIGHT)

        if event.type == pygame.KEYDOWN:
            if self.is_focus:
                if event.key == pygame.K_BACKSPACE:
                    if self.cursor_pos:
                        self.text = self.delete_string_at(self.text, self.cursor_pos, 1)
                    self.cursor_pos -= 1
                elif event.key == pygame.K_TAB:
                    string = "  "
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
                    self.text = self.insert_string_at(self.text, event.unicode, self.cursor_pos)
                    self.cursor_pos += 1
                if self.cursor_pos <= -1:
                    self.cursor_pos = 0
                if self.cursor_pos > len(self.text):
                    self.cursor_pos = len(self.text)


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

    text_box = TextBox(constants.TEXT_BOX_OBJECT)

    text_box.loop(screen)
