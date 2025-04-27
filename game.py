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

        pygame.draw.rect(self.screen, (220, 220, 220), self.side_panel)

        for event in events:
            self.menu.handle_event(event)
            points_gained, harvest = self.grid.handle_event(event, self.menu.selected_action, self.menu.selected_plant)

            self.points += points_gained
            if harvest:
                self.harvest_counts[harvest] = self.harvest_counts.get(harvest, 0) + 1

        return True
