import pygame

class Button:
    def __init__(self, x, y, width, height, border_radius, background_color, text, text_color, text_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_radius = border_radius
        self.background_color = background_color
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        font = pygame.font.SysFont(None, self.text_size)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center = (self.x + self.width / 2, self.y + self.height / 2))

        pygame.draw.rect(screen, self.background_color, self.rect, 0, self.border_radius)

        screen.blit(text, text_rect)


    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("hello")

    def loop(self):
        pass


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([720, 720])

    button = Button(50, 100, 100, 50, 5, (0,255,0), "hello", (255,0,0), 24)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            button.event_handler(event)

        screen.fill((255,255,255))
        button.draw(screen)
        pygame.display.flip()
