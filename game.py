import pygame
from pygame.locals import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 20)
        self.grid_size = 15
        self.tile_size = 30

        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        self.screen_width, self.screen_height = screen.get_size()

        self.offset_x = (self.screen_width - (self.grid_size * self.tile_size)) // 2
        self.offset_y = (self.screen_height - (self.grid_size * self.tile_size)) // 2

        self.menu_buttons = []
        self.selected_event = None

        self.menu_buttons.append((pygame.Rect(0, 0, 200, 50), "Grano", "grain"))

    def draw_grid(self):
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                rect = pygame.Rect(
                    self.offset_x + x * self.tile_size,
                    self.offset_y + y * self.tile_size,
                    self.tile_size,
                    self.tile_size
                )
                color = (200, 200, 200) if self.grid[y][x] == 0 else (255, 0, 0)
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)  # bordo nero

    def draw_buttons(self):
        for button, text, _ in self.menu_buttons:
            pygame.draw.rect(self.screen, (76, 153, 0), button)
            label = self.font.render(text, True, (255, 255, 255))
            label_rect = label.get_rect(center=button.center)
            self.screen.blit(label, label_rect)

    def handle_click(self, x, y):
        col = x // self.tile_size
        row = y // self.tile_size
        if self.selected_event:
            print(f"Evento {self.selected_event} scatenato su cella ({row}, {col})")
            self.selected_event = None

    def run(self, events):
        self.draw_grid()
        self.draw_buttons()

        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                for button, _, action in self.menu_buttons:
                    if button.collidepoint(x, y):
                        if action == "grain":
                            self.selected_event = "grain"
                            break

                if event.button == 1:  # Click sinistro
                    if x < self.screen.get_width() and y < self.screen.get_height():
                        self.handle_click(x, y)

        return True