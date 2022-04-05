import pygame
import constants
import button


class Menu:
    def __init__(self, object):
        self.object = object
        self.color = {
            "background": self.object["color"]["background"]
        }
        self.buttons = []
        for buttonObject in object["buttons"]:
            self.buttons.append(button.Button(buttonObject))


    def draw(self, screen):
        screen.fill(self.color["background"])
        for button in self.buttons:
            button.draw(screen)

        pygame.display.flip()


    def rescale(self, scaleX, scaleY):
        for button in self.buttons:
            button.rescale(scaleX, scaleY)


    def event_handler(self, event):
        if event.type == pygame.VIDEORESIZE:
            self.rescale(event.w / constants.SCREEN_WIDTH, event.h / constants.SCREEN_HEIGHT)


    def loop(self, screen, fps_limit = 10):
        clock = pygame.time.Clock()
        while True:
            clock.tick(fps_limit)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return constants.QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return constants.QUIT
                    return constants.SCENE_GAME
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.is_clicked():
                            return constants.SCENE_GAME
                    # for window in self.windows:
                    #     if window.is_clicked(event.pos):
                    #         return constants.SCENE_GAME
                self.event_handler(event)
            self.draw(screen)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.RESIZABLE)
    menu = Menu(constants.MENU_OBJECT)
    menu.loop(screen, constants.FPS_LIMIT)
