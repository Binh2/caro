import pygame
import json
import constants

class Button:
    def __init__(self, object):
        self.object = object
        self.x = self.object['x']
        self.y = self.object['y']
        self.width = self.object['width']
        self.height = self.object['height']
        self.border_radius = self.object['border_radius']
        self.text = self.object['text']
        self.text_size = self.object['text_size']
        self.color_palette = self.object['color'] # color_palette had to have background and text key
        self.name = self.object['name']
        self.is_center = self.object['is_center']


    def draw(self, screen):
        font = pygame.font.SysFont(None, int(self.text_size))
        text = font.render(self.text, True, self.color_palette["text"])
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if not self.is_center:
            text_rect = text.get_rect(center = (self.x + self.width / 2, self.y + self.height / 2))

        else:
            text_rect = text.get_rect(center = (self.x, self.y))
            self.rect.center = (self.x, self.y);

        pygame.draw.rect(screen, self.color_palette["background"], self.rect, 0, self.border_radius)
        screen.blit(text, text_rect)


    def rescale(self, xScalar, yScalar):
        self.x = self.object["x"] * xScalar
        self.y = self.object['y'] * yScalar
        self.width = self.object['width'] * xScalar
        self.height = self.object['height'] * yScalar
        # self.border_radius = self.object['border_radius']
        self.text_size = self.object['text_size'] * yScalar


    def is_clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())


    def event_handler(self, event):
        if event.type == pygame.VIDEORESIZE:
            self.rescale(event.w / constants.SCREEN_WIDTH, event.h / constants.SCREEN_HEIGHT)

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

    button = Button(constants.MENU_OBJECT["buttons"][0])

    button.loop(screen)
