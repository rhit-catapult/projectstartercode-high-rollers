import pygame


class ChipCounter:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.font1 = pygame.font.SysFont("timesnewroman", size=28)


    def draw(self, value):
        self.value = value
        self.caption1 = self.font1.render(str(self.value), True, (255, 255, 255))
        self.players_chips = pygame.image.load("poker_chip.png")
        self.screen.blit(self.caption1,(self.x, self.y))



    #def update(self, new):
        #self.value = new
        #self.caption1 = self.font1.render(str(self.value), True, (255, 255, 255))






