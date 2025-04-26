import pygame

from game import Game
from menu import Menu

pygame.init()

# ====== Dimensioni della finestra ====== #
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Py Farm")


def main():
    menu = Menu(screen)
    game = Game(screen)

    running = True
    in_game = False

    while running:
        screen.fill((64, 64, 64))

        events = pygame.event.get()  # <-- Prima raccogli gli eventi

        if not in_game:
            in_game = menu.run(events)
        else:
            in_game = game.run(events)

        pygame.display.flip()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()