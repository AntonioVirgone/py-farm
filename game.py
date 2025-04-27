import pygame
from game_menu import GameMenu
from grid import Grid

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()

        self.menu_height = 100
        self.menu = GameMenu(screen, self.screen_width, self.menu_height)

        self.side_panel_width = 200
        self.side_panel = pygame.Rect(self.screen_width - self.side_panel_width, self.menu_height,
                                      self.side_panel_width, self.screen_height - self.menu_height)

        self.game_area = pygame.Rect(0, self.menu_height,
                                     self.screen_width - self.side_panel_width, self.screen_height - self.menu_height)

        self.grid_size = 10
        self.tile_size = 40
        self.offset_x = (self.game_area.width - self.grid_size * self.tile_size) // 2
        self.offset_y = (self.game_area.height - self.grid_size * self.tile_size) // 2 + self.menu_height

        self.grid = Grid(screen, self.grid_size, self.tile_size, self.offset_x, self.offset_y)

        self.points = 0
        self.harvest_counts = {}

    def run(self, events):
        self.grid.update()

        self.menu.draw(self.points, self.harvest_counts)
        self.grid.draw()

        # --- Disegna il pannello laterale ---
        pygame.draw.rect(self.screen, (220, 220, 220), self.side_panel)

        # Mostra il raccolto nel pannello laterale
        font = pygame.font.SysFont(None, 24)
        y_offset = self.menu_height + 20
        x_offset = self.screen_width - self.side_panel_width + 20

        title = font.render("Raccolto:", True, (0, 0, 0))
        self.screen.blit(title, (x_offset, y_offset))
        y_offset += 30

        for plant, count in self.harvest_counts.items():
            text = font.render(f"{plant}: {count}", True, (0, 0, 0))
            self.screen.blit(text, (x_offset, y_offset))
            y_offset += 25

        for event in events:
            self.menu.handle_event(event)
            points_gained, harvest = self.grid.handle_event(event, self.menu.selected_action, self.menu.selected_plant)

            self.points += points_gained
            if harvest:
                self.harvest_counts[harvest] = self.harvest_counts.get(harvest, 0) + 1

        return True
