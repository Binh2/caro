import pygame
import constants
import colors

color_palette = colors.color_palettes["freezing"]

class Menu:
    def __init__(self, screen):
        self.screen = screen


    def draw(self):
        self.screen.fill(color_palette[0])
        font = pygame.font.SysFont(None, 36)
        image = font.render("hello", True, color_palette[1])
        self.screen.blit(image, (100, 100))
        pygame.display.flip()


    def main_loop(self):
        fps_limit = 10
        clock = pygame.time.Clock()
        while True:
            clock.tick(fps_limit)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return constants.QUIT
                if event.type == pygame.KEYDOWN:
                    return constants.SCENE_GAME
            self.draw()
        
        
