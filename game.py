import pygame
import time
from tile import Tile


'''
    def draw_grid(self):
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                rect = pygame.Rect(
                    self.offset_x + x * self.tile_size,
                    self.offset_y + y * self.tile_size,
                    self.tile_size,
                    self.tile_size
                )
                color = (153, 76, 0) if self.grid[y][x] == 0 else (153, 153, 0)
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
'''


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()

        # Definiamo le aree
        self.menu_height = 100
        self.menu_rect = pygame.Rect(0, 0, self.screen_width, self.menu_height)
        self.game_rect = pygame.Rect(0, self.menu_height, self.screen_width, self.screen_height - self.menu_height)

        # Parametri della griglia
        self.grid_size = 10
        self.tile_size = 25

        # Calcolo l'offset per centrare la griglia NEL SOLO GAME_RECT
        self.offset_x = self.game_rect.x + (self.game_rect.width - self.grid_size * self.tile_size) // 2
        self.offset_y = self.game_rect.y + (self.game_rect.height - self.grid_size * self.tile_size) // 2

        # Creo la griglia di Tile
        self.grid = []
        for y in range(self.grid_size):
            row = []
            for x in range(self.grid_size):
                tile_x = self.offset_x + x * self.tile_size
                tile_y = self.offset_y + y * self.tile_size
                row.append(Tile(tile_x, tile_y, self.tile_size))
            self.grid.append(row)

        # Bottoni azione (esempio)
        self.font = pygame.font.SysFont('Arial', 24)
        self.buttons = []
        self.create_buttons()

        # Azione selezionata
        self.selected_action = None
        self.points = 0

    def create_buttons(self):
        actions = ["Piantare", "Distruggere", "Altro"]
        for i, action in enumerate(actions):
            btn_width, btn_height = 150, 40
            x = 20 + i * (btn_width + 20)
            y = (self.menu_height - btn_height) // 2
            rect = pygame.Rect(x, y, btn_width, btn_height)
            self.buttons.append((rect, action))

    def draw_menu(self):
        pygame.draw.rect(self.screen, (180, 180, 180), self.menu_rect)
        for rect, text in self.buttons:
            color = (0, 0, 255) if self.selected_action == text else (100, 100, 255)
            pygame.draw.rect(self.screen, color, rect)
            label = self.font.render(text, True, (255, 255, 255))
            label_rect = label.get_rect(center=rect.center)
            self.screen.blit(label, label_rect)

    def draw_grid(self):
        for row in self.grid:
            for tile in row:
                tile.draw(self.screen)

    def update_grid(self):
        for row in self.grid:
            for tile in row:
                tile.update()

    def run(self, events):
        self.update_grid()
        self.draw_menu()
        self.draw_grid()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Se clicco sopra (nel menu)
                if self.menu_rect.collidepoint(x, y):
                    for rect, action in self.buttons:
                        if rect.collidepoint(x, y):
                            self.selected_action = action
                            print(f"Azione selezionata: {action}")

                # Se clicco sotto (nella griglia)
                elif self.game_rect.collidepoint(x, y):
                    for row in self.grid:
                        for tile in row:
                            if tile.rect.collidepoint(x, y):
                                if self.selected_action == "Piantare" and tile.state == 0:
                                    tile.plant()
                                elif self.selected_action == "Distruggere" and tile.state != 0:
                                    tile.harvest()
                                elif tile.ready:
                                    tile.harvest()
                                    self.points += 10
                                    print(f"Raccolto! Punti: {self.points}")

        return True
