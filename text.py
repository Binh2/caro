import pygame
import colors


class Text:
    def __init__(self, screen, text, size, color_palette = colors.color_palettes['freezing']):
        self.screen = screen
        self.font = pygame.font.SysFont(None, size)
        self.image = self.font.render(text, True, color_palette[1])
        print(color_palette)
        self.rect = self.image.get_rect()

        
    def draw(self, x, y = None):
        if y == None:
            y = x[1]
            x = x[0]
        self.rect.x = x
        self.rect.y = y
        self.screen.blit(self.image, (x, y))


    def is_clicked(self, x, y = None):
        if y == None:
            y = x[1]
            x = x[0]
        return self.rect.collidepoint(x, y)

                    
                                      