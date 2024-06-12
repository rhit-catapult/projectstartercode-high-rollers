import pygame


class ChipCounter:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.value = 10
        self.font1 = pygame.font.SysFont("comicsansms", size=28)
        self.caption1 = self.font1.render(str(self.value), True, (255,255,255))

    def draw(self):
        self.screen.blit(self.caption1,(self.x, self.y))

    def update(self, delta):
        self.value = delta + self.value
        self.caption1 = self.font1.render(str(self.value), True, (255, 255, 255))






