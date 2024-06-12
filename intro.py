import pygame
import sys
import button_module
import project

def main():
    pygame.init()
    pygame.display.set_caption("Poker")
    screen = pygame.display.set_mode((1400,800))

    play_button = button_module.TextButton(screen, screen.get_width() / 2, 705, "Click here to play")
    title_font = pygame.font.SysFont("timesnewroman", 40)
    instruction_font = pygame.font.SysFont("timesnewroman", 26)
    title_caption = title_font.render("Poker: Texas Hold'em edition", True, pygame.Color("WHITE"))
    instruction_caption = instruction_font.render("Left click to check, spacebar to bet, F to fold. ", True, pygame.Color("WHITE"))

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button.is_clicked_by(event.pos):
                    print("You clicked the play button.")
                    project.main()
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((53, 101, 57))
        play_button.draw()

        screen.blit(title_caption, (445, screen.get_height()/5))
        screen.blit(instruction_caption, (445, screen.get_height()/3))

        pygame.display.update()
main()