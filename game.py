import pygame
from game_menu import GameMenu
from grid import Grid

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()

        self.menu_height = 100
        self.menu = GameMenu(screen, self.screen_width, self.menu_height)

        self.game_rect = pygame.Rect(0, self.menu_height, self.screen_width, self.screen_height - self.menu_height)
        self.grid_size = 10
        self.tile_size = 25

        self.offset_x = self.game_rect.x + (self.game_rect.width - self.grid_size * self.tile_size) // 2
        self.offset_y = self.game_rect.y + (self.game_rect.height - self.grid_size * self.tile_size) // 2

        self.grid = Grid(screen, self.grid_size, self.tile_size, self.offset_x, self.offset_y)

        self.points = 0

    def run(self, events):
        self.grid.update()

        self.menu.draw(self.points)
        self.grid.draw()

        for event in events:
            self.menu.handle_event(event)
            points_gained = self.grid.handle_event(event, self.menu.selected_action)
            self.points += points_gained

        return True
