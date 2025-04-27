import pygame
from game import Game
from button import Button

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PyFarm")

    clock = pygame.time.Clock()

    # Schermata iniziale
    start_menu = True
    game = None

    start_button = Button(300, 200, 200, 50, "Start Game", lambda: None)
    quit_button = Button(300, 300, 200, 50, "Quit", lambda: exit())

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if start_menu:
                start_button.handle_event(event)
                quit_button.handle_event(event)
                if start_button.hovered and event.type == pygame.MOUSEBUTTONDOWN:
                    start_menu = False
                    game = Game(screen)

        screen.fill((255, 255, 255))

        if start_menu:
            font = pygame.font.SysFont(None, 64)
            title = font.render("PyFarm", True, (0, 100, 0))
            screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 100))

            start_button.draw(screen)
            quit_button.draw(screen)
        else:
            if game:
                game.run(events)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
