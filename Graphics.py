import pygame
import random
import sys
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption("Poker")
    screen.fill((53, 101, 57))
    clock = pygame.time.Clock()

    image_size = (200,200)
    cowboy = pygame.image.load("cowboy_hat.png")
    fedora = pygame.image.load("fedora.png")
    grad_hat = pygame.image.load("graduation-hat.png")
    tophat = pygame.image.load("tophat.png")
    cowboy = pygame.transform.scale(cowboy, image_size)
    fedora = pygame.transform.scale(fedora, (150,150))
    grad_hat = pygame.transform.scale(grad_hat, (200,120))
    tophat = pygame.transform.scale(tophat, (150, 120))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((53, 101, 57))
        screen.blit(cowboy, (200,-50))
        screen.blit(fedora, (0,590))
        screen.blit(grad_hat, (1000, 650))
        screen.blit(tophat, (1230, 50))


        pygame.display.update()

main()