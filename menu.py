import pygame
from pygame.locals import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 40)
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        self.create_button("Start", 300, 200, "start", (76, 153, 0))
        self.create_button("Quit", 300, 300, "quit", (153, 0, 0))

    def create_button(self, text, x, y, action, color):
        self.buttons.append((pygame.Rect(x, y, 200, 50), text, action, color))

    def draw_buttons(self):
        for button, text, _, color in self.buttons:
            pygame.draw.rect(self.screen, color, button)
            label = self.font.render(text, True, (255, 255, 255))
            label_rect = label.get_rect(center=button.center)
            self.screen.blit(label, label_rect)

    def run(self, events):
        self.draw_buttons()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for button, _, action, color in self.buttons:
                    if button.collidepoint(x, y):
                        if action == "start":
                            return True
                        elif action == "quit":
                            pygame.quit()
                            exit()
        return False