import pygame
import json
import constants

class Button:
    def __init__(self, fileName):
        with open(fileName, "r") as file:
            self.obj = json.load(file)
        self.x = self.obj['x']
        self.y = self.obj['y']
        self.width = self.obj['width']
        self.height = self.obj['height']
        self.border_radius = self.obj['border_radius']
        self.text = self.obj['text']
        self.text_size = self.obj['text_size']
        self.color_palette = self.obj['color'] # color_palette had to have background and text key
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        font = pygame.font.SysFont(None, self.text_size)
        text = font.render(self.text, True, self.color_palette["text"])
        text_rect = text.get_rect(center = (self.x + self.width / 2, self.y + self.height / 2))

        pygame.draw.rect(screen, self.color_palette["background"], self.rect, 0, self.border_radius)

        screen.blit(text, text_rect)

    def after_clicked(self):
        print("hello")

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return self.after_clicked()

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
    screen = pygame.display.set_mode([720, 720])

    button = Button('button.txt')

    button.loop(screen)
